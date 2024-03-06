from main.models import *
from main.serializers import *
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response

#"""""Start filter Employee Model"""""
# start filter Employee.user.username
@api_view(['GET'])
def filter_employee_by_user_username_view(request):
    username = request.GET.get('username')
    try:
        users = Employee.objects.filter(user__username=username).order_by('-id')
        if users:
            ser = EmployeeSerializer(users, many=True)
            return Response(ser.data)
        else:
            message = 'No such employee found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such employee found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# end filter Employee.user.username

# start  filter Employee.status
@api_view(['GET'])
def filter_employee_by_status_view(request):
    status = request.GET['status']
    try:
        employees = Employee.objects.filter(status=status).order_by('-id')
        if status:
            ser = EmployeeSerializer(employees, many=True)
            return Response(ser.data)
        else:
            message = 'No such employee found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such employee found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# end  filter Employee.status

# start  filter Employee.work_time
@api_view(['GET'])
def filter_employee_by_work_time_view(request):
    time = request.GET['work_time']
    try:
        employees = Employee.objects.filter(work_time=time).order_by('-id')
        if employees:
            ser = EmployeeSerializer(employees, many=True)
            return Response(ser.data)
        else:
            message = 'No such employee found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such employee found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# end filter Employee.work_time

# start  filter Employee.experience
@api_view(['GET'])
def filter_employee_by_experience_view(request):
    experience = request.GET['experience']
    try:
        employees = Employee.objects.filter(experience=experience).order_by('-id')
        if employees:
            ser = EmployeeSerializer(employees, many=True)
            return Response(ser.data)
        else:
            message = 'No such employee found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such employee found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# end filter Employee.experience

# start filter Employee.department
@api_view(['GET'])
def filter_employee_by_department_view(request):
    department = request.GET['name']
    try:
        employees = Employee.objects.filter(department__name=department).order_by('-id')
        if employees:
            ser = EmployeeSerializer(employees, many=True)
            return Response(ser.data)
        else:
            message = 'No such employee found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
        return Response(data)
    except:
           message = 'No such employee found'
           status = 500
           data = {
               'status': status,
               'message': message
           }
           return Response(data)
# start filter Employee.salary
@api_view(['GET'])
def filter_employee_by_salary_view(request):
    small_amount = request.GET['small_amount']
    large_amount = request.GET['large_amount']
    try:
        employees = Employee.objects.filter(salary__gte=small_amount, salary__lte=large_amount).order_by('-id')
        if employees:
            ser = EmployeeSerializer(employees, many=True)
            return Response(ser.data)
        else:
            message = 'No such employee found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
            message = 'No such employee found'
            status = 500
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
# end filter Employee.salary

# start filter Employee.room.number
@api_view(['GET'])
def filter_employee_by_room_view(request):
    number = request.GET['number']
    try:
        employees = Employee.objects.filter(room__number=number).order_by('-id')
        if employees:
            ser = EmployeeSerializer(employees, many=True)
            return Response(ser.data)

        else:
            message = 'No such employee found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such employee found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# end filter Employee.room.number
#"""""End filter Employee Model"""""

#"""""Start filter Patient Model"""""
# start filter Patient.doctor.user.username
@api_view(['GET'])
def filter_patient_by_doctor_view(request):
    username = request.GET['username']
    try:
        patients = Patient.objects.filter(doctor__user__username=username).order_by('-id')
        if patients:
            ser = PatientSerializer(patients, many=True)
            return Response(ser.data)
        else:
            message = 'No such patient found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such patient found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# end filter Patient.doctor.user.username

# start filter Patient.full_name
@api_view(['GET'])
def filter_patient_by_full_name_view(request):
    full_name = request.GET['full_name']
    try:
        patients = Patient.objects.filter(full_name=full_name).order_by('-id')
        if patients:
            ser = PatientSerializer(patients, many=True)
            return Response(ser.data)
        else:
            message = 'No such patient found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such patient found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# end filter Patient.full_name

# start filter Patient.gender
@api_view(['GET'])
def filter_patient_by_gender_view(request):
    gender = request.GET['gender']
    try:
        patients = Patient.objects.filter(gender=gender).order_by('-id')
        if patients:
            ser = PatientSerializer(patients, many=True)
            return Response(ser.data)
        else:
            message = 'No such patient found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such patient found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# end filter Patient.gender

# start filter Patient.phone_number
@api_view(['GET'])
def filter_patient_by_phone_number_view(request):
    phone_number = request.GET['phone_number']
    try:
        if phone_number.isdigit():
            if len(phone_number) == 9:
                status = 400
                message = 'Error : Example 912345678'
                date = {
                'status': status,
                'message': message
                }
                return Response(date)
            else:
                try:
                    patients = Patient.objects.filter(phone_number=phone_number).order_by('-id')
                    if patients:
                        ser = PatientSerializer(patients, many=True)
                        return Response(ser.data)
                    else:
                        message = 'No such patient found'
                        status = 400
                        data = {
                            'status': status,
                            'message': message
                        }
                        return Response(data)
                except:
                    message = 'No such patient found'
                    status = 500
                    data = {
                        'status': status,
                        'message': message
                    }
                    return Response(data)
        else:
            status = 400
            message = 'The phone number must consist of numbers only'
            date = {
                'status': status,
                'message': message
            }
            return Response(date)
    except Exception as err:
        return Response(f'{err}')
# end filter Patient.phone_number

# start filter Patient.room.number
@api_view(['GET'])
def filter_patient_by_room_view(request):
    number = request.GET['number']
    try:
        patients = Patient.objects.filter(room__number=number).order_by('-id')
        if patients:
            ser = PatientSerializer(patients, many=True)
            return Response(ser.data)
        else:
            message = 'No such patient found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such patient found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# end filter Patient.room.number

# start filter Patient.payment_status
@api_view(['GET'])
def filter_patient_by_payment_status_view(request):
    payment_status = request.GET['payment_status']
    try:
        patients = Patient.objects.filter(payment_status=payment_status).order_by('-id')
        if patients:
            ser = PatientSerializer(patients, many=True)
            return Response(ser.data)
        else:
            message = 'No such patient found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)

    except:
        message = 'No such patient found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# end filter Patient.payment_status
#"""""End filter Patient Model"""""

#"""""Start filter Room Model"""""
# start filter Room.name
@api_view(['GET'])
def filter_room_by_name_view(request):
    name = request.GET['name']
    try:
        rooms = Room.objects.filter(name=name).order_by('-id')
        if rooms:
            ser = RoomSerializer(rooms, many=True)
            return Response(ser.data)
        else:
            message = 'No such room found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such room found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# end filter Room.name

# start filter Room.cost
@api_view(['GET'])
def filter_room_by_cost_view(request):
    small_cost = request.GET['small_cost']
    large_cost = request.GET['large_cost']
    try:
        rooms = Room.objects.filter(cost__gte=small_cost, cost__lte=large_cost)
        if rooms:
            ser = RoomSerializer(rooms, many=True)
            return Response(ser.data)
        else:
            message = 'No such room found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such room found'
        status = 500
        data = {
            'status': status,
            'message': message
        }
        return Response(data)
# end filter Room.cost

# start filter Room.department.name
@api_view(['GET'])
def filter_room_by_department_view(request):
    name = request.GET['name']
    try:
        rooms = Room.objects.filter(department__name=name).order_by('-id')
        if rooms:
            ser = RoomSerializer(rooms, many=True)
            return Response(ser.data)
        else:
            message = 'No such room found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such room found'
        status = 500
        data = {
            'status': status,
            'message': message,
        }
        return Response(data)
# end filter Room.department.name

# start filter Room.capacity
@api_view(['GET'])
def filter_room_by_capacity_view(request):
    small_capacity = request.GET['small_capacity']
    large_capacity = request.GET['large_capacity']
    try:
        rooms = Room.objects.filter(capacity__gte=small_capacity, capacity__lte=large_capacity).order_by('-id')
        if rooms:
            ser = RoomSerializer(rooms, many=True)
            return Response(ser.data)
        else:
            message = 'No such room found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such room found'
        status = 500
        data = {
            'status': status,
            'message': message,
        }
        return Response(data)
# end filter Room.capacity

# start filter Room.status
@api_view(['GET'])
def filter_room_by_status_view(request):
    status = request.GET['status']
    try:
        rooms = Room.objects.filter(status=status).order_by('id')
        if rooms:
            ser = RoomSerializer(rooms, many=True)
            return Response(ser.data)
        else:
            message = 'No such room found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such room found'
        status = 500
        data = {
            'status': status,
            'message': message,
        }
        return Response(data)
# end filter Room.status

# start filter Room.is_booked
@api_view(['GET'])
def filter_room_by_is_booked_view(request):
    is_booked = request.GET['is_booked']
    try:
        rooms = Room.objects.filter(is_booked=is_booked).order_by('id')
        if rooms:
            ser = RoomSerializer(rooms, many=True)
            return Response(ser.data)
        else:
            message = 'No such room found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such room found'
        status = 500
        data = {
            'status': status,
            'message': message,
        }
        return Response(data)
# end filter Room.is_booked

# start filter Room.equipment.name
@api_view(['GET'])
def filter_room_by_equipment_view(request):
    name = request.GET['name']
    try:
        rooms = Room.objects.filter(equipment__name=name).order_by('-id')
        if rooms:
            ser = RoomSerializer(rooms, many=True)
            return Response(ser.data)
        else:
            message = 'No such room found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such room found'
        status = 500
        data = {
            'status': status,
            'message': message,
        }
        return Response(data)
# end filter Room.equipment.name
#"""""End filter Room Model"""""

#"""""Start filter Payment Model"""""
# start filter Payment.patient.full_name
@api_view(['GET'])
def filter_payment_by_patient_view(request):
    full_name = request.GET['full_name']
    try:
        payments = Payment.objects.filter(patient__full_name=full_name).order_by('-id')
        if payments:
            ser = PaymentSerializer(payments, many=True)
            return Response(ser.data)
        else:
            message = 'No such payment found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such payment found'
        status = 500
        data = {
            'status': status,
            'message': message,
        }
        return Response(data)
# end filter Payment.patient.full_name

# start filter Payment.created_at
@api_view(['GET'])
def filter_payment_by_created_at_view(request):
    created_at = request.GET['created_at']
    try:
        payments = Payment.objects.filter(created_at=created_at).order_by('-id')
        if payments:
            ser = PaymentSerializer(payments, many=True)
            return Response(ser.data)
        else:
            message = 'No such payment found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such payment found'
        status = 500
        data = {
            'status': status,
            'message': message,
        }
        return Response(data)
# start filter Payment.created_at

# start filter Payment.payment_type
@api_view(['GET'])
def filter_payment_by_payment_type_view(request):
    payment_type = request.GET['payment_type']
    try:
        payments = Payment.objects.filter(payment_type=payment_type).order_by('-id')
        if payments:
            ser = PaymentSerializer(payments, many=True)
            return Response(ser.data)
        else:
            message = 'No such payment found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such payment found'
        status = 500
        data = {
            'status': status,
            'message': message,
        }
        return Response(data)
# end filter Payment.payment_type
#"""""End filter Payment Model"""""

#"""""Start filter Comment Model"""""
# start filter Comment.status
@api_view(['GET'])
def filter_comment_by_status_view(request):
    status = request.GET['status']
    try:
        comments = Comment.objects.filter(status=status)
        if comments:
            ser = CommentSerializer(comments, many=True)
            return Response(ser.data)
        else:
            message = 'No such comment found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such comment found'
        status = 500
        data = {
            'status': status,
            'message': message,
        }
        return Response(data)
# end filter Comment.status
#"""""End filter Comment Model"""""

#"""""Start filter Income Model"""""
# start filter Income.amount
@api_view(['GET'])
def filter_income_by_amount_view(request):
    small_amount = request.GET['small_amount']
    large_amount = request.GET['large_amount']
    try:
        incomes = Income.objects.filter(amount__gte=small_amount, amount__lte=large_amount).order_by('-id')
        if incomes:
            ser = IncomeSerializer(incomes, many=True)
            return Response(ser.data)
        else:
            message = 'No such income found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such income found'
        status = 500
        data = {
            'status': status,
            'message': message,
        }
        return Response(data)
# start filter Income.amount

# start filter Income.data
@api_view(['GET'])
def filter_income_by_data_view(request):
    data = request.GET['data']
    try:
        incomes = Income.objects.filter(created_at=data).order_by('-id')
        if incomes:
            ser = IncomeSerializer(incomes, many=True)
            return Response(ser.data)
        else:
            message = 'No such income found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such income found'
        status = 500
        data = {
            'status': status,
            'message': message,
        }
        return Response(data)
# end filter Income.data
#"""""End filter Income Model"""""

#"""""Start filter Revenue Model"""""
# start filter Revenue.amount
@api_view(['GET'])
def filter_revenue_by_amount_view(request):
    small_amount = request.GET['small_amount']
    large_amount = request.GET['large_amount']
    try:
        revenues = Revenue.objects.filter(amount__gte=small_amount, amount__lte=large_amount).order_by('-id')
        if revenues:
            ser = RevenueSerializer(revenues, many=True)
            return Response(ser.data)
        else:
            message = 'No such revenue found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such revenue found'
        status = 500
        data = {
            'status': status,
            'message': message,
        }
        return Response(data)
# start filter Revenue.amount

# start filter Revenue.data
@api_view(['GET'])
def filter_revenue_by_data_view(request):
    data = request.GET['data']
    try:
        revenues = Revenue.objects.filter(created_at=data).order_by('-id')
        if revenues:
            ser = RevenueSerializer(revenues, many=True)
            return Response(ser.data)
        else:
            message = 'No such revenue found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such revenue found'
        status = 500
        data = {
            'status': status,
            'message': message,
        }
        return Response(data)
# end filter Revenue.data
#"""""End filter Revenue Model"""""

#"""""Start filter Operation Model"""""
# start filter Operation.data and start_time
@api_view(['GET'])
def filter_operation_by_data_and_start_time_view(request):
    data = request.GET['data']
    small_time = request.GET['small_time']
    large_time = request.GET['large_time']
    try:
        operations = Operation.objects.filter(data=data, start_time__gte=small_time, start_time__lte=large_time).order_by('-id')
        if operations:
            ser = OperationSerializer(operations, many=True)
            return Response(ser.data)
        else:
            message = 'No such operation found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such operation found'
        status = 500
        data = {
            'status': status,
            'message': message,
        }
        return Response(data)
# end filter Operation.data and start_time

#start filter Operation.start_time and end_time
@api_view(['GET'])
def filter_operation_by_start_and_end_time_view(request):
    small_start_time = request.GET['small_start_time']
    large_end_time = request.GET['large_end_time']
    try:
        operations = Operation.objects.filter(start_time__gte=small_start_time, end_time__lte=large_end_time).order_by('-id')
        if operations:
            ser = OperationSerializer(operations, many=True)
            return Response(ser.data)
        else:
            message = 'No such operation found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such operation found'
        status = 500
        data = {
            'status': status,
            'message': message,
        }
        return Response(data)
# end filter Operation.start_time and end_time

# start filter Operation.patient.full_name
@api_view(['GET'])
def filter_operation_by_patient_view(request):
    full_name = request.GET['full_name']
    try:
        operations = Operation.objects.filter(patient__full_name=full_name).order_by('-id')
        if operations:
            ser = OperationSerializer(operations, many=True)
            return Response(ser.data)
        else:
            message = 'No such operation found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such operation found'
        status = 500
        data = {
            'status': status,
            'message': message,
        }
        return Response(data)
# end filter Operation.patient.full_name

# start filter Operation.room.number
@api_view(['GET'])
def filter_operation_by_room_view(request):
    number = request.GET['number']
    try:
        operations = Operation.objects.filter(room__number=number).order_by('-id')
        if operations:
            ser = OperationSerializer(operations, many=True)
            return Response(ser.data)
        else:
            message = 'No such operation found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such operation found'
        status = 500
        data = {
            'status': status,
            'message': message,
        }
        return Response(data)
# end filter Operation.room.number
#"""""End filter Operation Model"""""

#"""""Start filter Department Model"""""
# start filter Department.name
@api_view(['GET'])
def filter_department_by_name_view(request):
    name = request.GET['name']
    try:
        departments = Department.objects.filter(name=name).order_by('-id')
        if departments:
            ser = DepartmentSerializer(departments, many=True)
            return Response(ser.data)
        else:
            message = 'No such department found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such department found'
        status = 500
        data = {
            'status': status,
            'message': message,
        }
        return Response(data)
# end filter Department.name
#"""""End filter Department Model"""""

#"""""Start filter Equipment Model"""""
# start filter Equipment.name
@api_view(['GET'])
def filter_equipment_by_name_view(request):
    name = request.GET['name']
    try:
        equipments = Equipment.objects.filter(name=name).order_by('-id')
        if equipments:
            ser = EquipmentSerializer(equipments, many=True)
            return Response(ser.data)
        else:
            message = 'No such equipment found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such equipment found'
        status = 500
        data = {
            'status': status,
            'message': message,
        }
        return Response(data)
# end filter Equipment.name
#"""""End filter Equipment Model"""""

#"""""Start filter Attendance Model"""""
# start filter Attendance.employee
@api_view(['GET'])
def filter_attendance_by_employee_view(request):
    employee = request.GET['employee']
    try:
        attendances = Attendance.objects.filter(employee=employee).order_by('-id')
        if attendances:
            ser = AttendanceSerializer(attendances, many=True)
            return Response(ser.data)
        else:
            message = 'No such attendance found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such attendance found'
        status = 500
        data = {
            'status': status,
            'message': message,
        }
        return Response(data)
# start filter Attendance.employee

# start filter Attendance.data
@api_view(['GET'])
def filter_attendance_by_data_view(request):
    data= request.GET['data']
    try:
        attendances = Attendance.objects.filter(data=data).order_by('-id')
        if attendances:
            ser = AttendanceSerializer(attendances, many=True)
            return Response(ser.data)
        else:
            message = 'No such attendance found'
            status = 400
            data = {
                'status': status,
                'message': message
            }
            return Response(data)
    except:
        message = 'No such attendance found'
        status = 500
        data = {
            'status': status,
            'message': message,
        }
        return Response(data)
# start filter Attendance.data
#"""""End filter Attendance Model"""""
