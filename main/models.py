from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from .validators import ImageFileValidator
import qrcode
from io import BytesIO
from django.core.files import File
from django.core.exceptions import ValidationError


# Create your models here.


class User(AbstractUser):
    phone_number = models.CharField(max_length=13, verbose_name='Telefon Raqam', unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    address = models.TextField(verbose_name='Yashash manzil')

    class Meta:
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Foydalanuvchilar'


class Employee(models.Model):
    user = models.OneToOneField(to='User', on_delete=models.CASCADE, verbose_name='User')
    status = models.CharField(choices=(
        ('1' , 'doctor'),
        ('2', 'manager'),
        ('3', 'admin'),
        ('4', 'nurse'),
        ('5', 'director'),
        ('6', 'cooker'),
        ('doctor', 'doctor'),
        ('manager', 'manager'),
        ('admin', 'admin'),
        ('nurse', 'nurse'),
        ('director', 'director'),
        ('cooker', 'cooker')
    ), verbose_name='Lavozim')
    age = models.IntegerField(verbose_name='Yosh')
    salary = models.IntegerField(verbose_name='Oylik  maoshi')
    work_time = models.TextField(verbose_name='Ish vaqti')
    room = models.ForeignKey(to='Room', on_delete=models.CASCADE, verbose_name='Xonasi')
    experience = models.IntegerField(verbose_name='Ish tajribasi')
    bio = models.TextField(verbose_name='Malumotlari')
    department = models.ForeignKey(to='Department', on_delete=models.CASCADE, verbose_name="Bo'limi")
    info_qr_code = models.ImageField(upload_to='doctor_qr_codes/', blank=True, null=True)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Xodimlar'

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            border=3,
            box_size=5,
        )
        qr.add_data(f"Your data to encode in the QR code:{self.user.username}")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        buffer = BytesIO()
        img.save(buffer)

        self.info_qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)

        super().save(*args, **kwargs)


class Patient(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='FIO')
    doctor = models.ForeignKey(to='Employee', on_delete=models.CASCADE, verbose_name='Shifokori', )
    age = models.IntegerField(verbose_name='Yosh')
    phone_number = models.CharField(max_length=13, verbose_name='Telefon Raqami', unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    address = models.TextField(verbose_name='Yashash manzili')
    photo = models.ImageField(upload_to='patient_photos', validators=[ImageFileValidator])
    extra_phone_number = models.CharField(max_length=13, verbose_name='Telefon Raqami', unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    room = models.ForeignKey(to='Room', verbose_name='Xonasi', on_delete=models.CASCADE )
    bio = models.TextField(verbose_name='Malumotlari')
    booked_room_day = models.DateField(verbose_name='Mudati')
    payment_status = models.CharField(default=3, verbose_name="To'lov xolati", choices=(
        ('1', 'pay'),
        ('2', 'pard_paid'),
        ('3', 'unpaid'),
        ('pay', 'pay'),
        ('pard_paid', 'pard_paid'),
        ('unpaid', 'unpaid'),
    ))
    gender = models.CharField(verbose_name='Jinsi', choices=(
        ('1', 'men'),
        ('2', 'women'),
        ('men', 'men'),
        ('women', 'women'),
    ))
    info_qr_code = models.ImageField(upload_to='patient_qr_codes/', blank=True, null=True)

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            border=3,
            box_size=5,
        )
        qr.add_data(
            f"Your data to encode in the QR code:{self.full_name}")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)

        self.info_qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Bemorlar'

    def __str__(self):
        return self.full_name


class Cassa(models.Model):
    total_amount = models.IntegerField(verbose_name='Summa')

    class Meta:
        verbose_name = 'Cassa'
        verbose_name_plural = 'Hisob'

    def __int__(self):
        return self.total_amount


class Payment(models.Model):
    patient = models.ForeignKey(to='Patient', on_delete=models.CASCADE, verbose_name='Bemor')
    payment_amount = models.IntegerField(verbose_name='Tolov summasi')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Vaqti')
    payment_type = models.CharField(verbose_name='Tolov turi', choices=(
        ('1', 'card'),
        ('2', 'cash'),
        ('3', 'other '),
        ('card', 'card'),
        ('cash', 'cash'),
        ('other', 'other')
    ))
    qr_code = models.ImageField(upload_to='payment_qr_codes/', blank=True, null=True)

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            border=3,
            box_size=5,
        )
        qr.add_data(f"Your data to encode in the QR code:{self.patient.full_name}")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)

        self.qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = "To'lov"

    def __str__(self):
        return self.code


class Comment(models.Model):
    patient = models.ForeignKey(to='Patient', on_delete=models.CASCADE, verbose_name='Bemor')
    status = models.CharField(default=1, choices=(
        ('1', 'comment'),
        ('2', 'camplain'),
        ('3', 'suggestion'),
        ('comment', 'comment'),
        ('camplain', 'camplain'),
        ('suggestion', 'suggestion'),
    ))
    text = models.TextField(verbose_name='Izoh')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Vaqti')

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = "Izoh"


class Operation(models.Model):
    doctors = models.ManyToManyField(to='Employee', verbose_name='Doctorlar')
    data = models.DateField(verbose_name='Sana', null=True, blank=True)
    start_time = models.TimeField(verbose_name='Boshlangan vaqti')
    end_time = models.TimeField(verbose_name='Tugash vaqti')
    patient = models.ForeignKey(to='Patient', on_delete=models.CASCADE, verbose_name='Bemor')
    room = models.ForeignKey(to='Room', on_delete=models.CASCADE, verbose_name='Xona')

    class Meta:
        unique_together = ['start_time', 'end_time', 'patient']
        unique_together = ['start_time', 'room']
        verbose_name = 'Operation'
        verbose_name_plural = "Operatsiya"

    def clean(self):
        if self.end_time and self.end_time < self.start_time:
            raise ValidationError("End_time must be after start_time time.")

    def clead(self):
        if self.room.status != "operating":
            raise ValidationError("You have not selected an operating room")


class Department(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nomi', unique=True)

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = "Bo'lim"

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nomi')
    number = models.IntegerField(null=True)
    capacity = models.IntegerField(verbose_name="Sig'imi")
    cost = models.IntegerField(verbose_name='narxi $', default=0)
    status = models.CharField(verbose_name='Tarifi', choices=(
        ('1', 'economic'),
        ('2', 'semi-deluxe'),
        ('3', 'deluxe'),
        ('4', 'pro-deluxe'),
        ('5', 'staff'),
        ('6', 'operating'),
        ('economic', 'economic'),
        ('semi-deluxe', 'semi-deluxe'),
        ('deluxe', 'deluxe'),
        ('pro-deluxe', 'pro-deluxe'),
        ('staff', 'staff'),
        ('operating', 'operating')
    ))
    is_booked = models.BooleanField(verbose_name='Bandligi', null=True, blank=True)
    department = models.ForeignKey(to='Department', on_delete=models.CASCADE, verbose_name="Bo'limi")
    equipment = models.ForeignKey(to='Equipment', verbose_name='Jihozlar', null=True, blank=True,
                                  on_delete=models.CASCADE)
    other_info = models.TextField(null=True, blank=True, verbose_name="Qo'shimcha malimotlar")

    class Meta:
        unique_together = ['number', 'department', 'status']
        unique_together = ['number', 'department']
        verbose_name = 'Room'
        verbose_name_plural = "Xona"

    def __str__(self):
        return self.name


class Income(models.Model):
    amount = models.IntegerField(verbose_name='Summa')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Vaqti', )
    reason = models.TextField(verbose_name='Sababi')

    class Meta:
        verbose_name = 'Income'
        verbose_name_plural = "Daromat"


class Revenue(models.Model):
    amount = models.IntegerField(verbose_name='Summa')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Vaqti')
    reason = models.TextField(verbose_name='Sababi')

    class Meta:
        verbose_name = 'Revenue'
        verbose_name_plural = "Xarajat"


class Info_about_clinic(models.Model):
    total_patients_number = models.IntegerField(verbose_name='Bemorlar soni')
    total_employees_number = models.IntegerField(verbose_name='Xodimlar soni')
    bio = models.TextField(verbose_name='Malumot')
    address = models.TextField(verbose_name='Manzil')
    phone_number = models.CharField(max_length=13, verbose_name='Telefon Raqam', unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])

    class Meta:
        verbose_name = 'Info_about_clinic'
        verbose_name_plural = "Klinika malumotlari"


class Equipment(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nomi')
    extra_info = models.TextField(verbose_name="Qo'shimcha malumotlar")

    class Meta:
        verbose_name = 'Equipment'
        verbose_name_plural = "Jihoz"


class Attendance(models.Model):
    employee = models.ForeignKey(to='Employee', on_delete=models.CASCADE)
    data = models.DateField()
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)

    class Meta:
        unique_together = ['employee', 'data']

    def clean(self):
        if self.check_out and self.check_out < self.check_in:
            raise ValidationError("Check-out time must be after check-in time.")

    def __str__(self):
        return f"{self.employee.full_name} - {self.data}"
