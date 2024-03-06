from main.models import *
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, GenericAPIView
from main.serializers import *

#"""""Start CRUD Employee Model"""
# create model
class Create_Employee_Api_View(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
# end create model

# read model
class Get_All_Employee_Items(ListAPIView):
    queryset = Employee.objects.all().order_by('-id')
    serializer_class = EmployeeSerializer
#end read model

# update model
class Update_Employee_Api_View(UpdateAPIView):
    queryset = Employee.objects.all() 
    serializer_class = EmployeeSerializer
#end update model

# delete model
class Delete_Employee_Api_View(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
# end delete model
#"""""End CRUD Employee Model"""

#"""""Start CRUD Patient Model"""
# create model
class Create_Patient_Api_View(CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
# end create model

# read model
class Get_All_Patient_Items(ListAPIView):
    queryset = Patient.objects.all().order_by('-id')
    serializer_class = PatientSerializer
#end read model

# update model
class Update_Patient_Api_View(UpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
#end update model

# delete model
class Delete_Patient_Api_View(DestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
# end delete model
#"""""End CRUD Patient Model"""

#"""""Start CRUD Cassa Model"""
# create model
class Create_Cassa_Api_View(CreateAPIView):
    queryset = Cassa.objects.all()
    serializer_class = CassaSerializer
# end create model

# read model
class Get_All_Cassa_Items(ListAPIView):
    queryset = Cassa.objects.all().order_by('-id')
    serializer_class = CassaSerializer
#end read model

# update model
class Update_Cassa_Api_View(UpdateAPIView):
    queryset = Cassa.objects.all()
    serializer_class = CassaSerializer
#end update model

# delete model
class Delete_Cassa_Api_View(DestroyAPIView):
    queryset = Cassa.objects.all()
    serializer_class = CassaSerializer
# end delete model
#"""""End CRUD Cassa Model"""

#"""""Start CRUD Payment Model"""
# create model
class Create_Payment_Api_View(CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
# end create model

# read model
class Get_All_Payment_Items(ListAPIView):
    queryset = Payment.objects.all().order_by('-id')
    serializer_class = PaymentSerializer
#end read model

# update model
class Update_Payment_Api_View(UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
#end update model

# delete model
class Delete_Payment_Api_View(DestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
# end delete model
#"""""End CRUD Payment Model""

#"""""Start CRUD Comment Model"""
# create model
class Create_Comment_Api_View(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
# end create model

# read model
class Get_All_Comment_Items(ListAPIView):
    queryset = Comment.objects.all().order_by('-id')
    serializer_class = CommentSerializer
#end read model

# update model
class Update_Comment_Api_View(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
#end update model

# delete model
class Delete_Comment_Api_View(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
# end delete model
#"""""End CRUD Comment Model""

#"""""Start CRUD Operation Model"""
# create model
class Create_Operation_Api_View(CreateAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
# end create model

# read model
class Get_All_Operation_Items(ListAPIView):
    queryset = Operation.objects.all().order_by('-id')
    serializer_class = OperationSerializer
#end read model

# update model
class Update_Operation_Api_View(UpdateAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
#end update model

# delete model
class Delete_Operation_Api_View(DestroyAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
# end delete model
#"""""End CRUD Operation Model""

#"""""Start CRUD Department Model"""
# create model
class Create_Department_Api_View(CreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
# end create model

# read model
class Get_All_Department_Items(ListAPIView):
    queryset = Department.objects.all().order_by('-id')
    serializer_class = DepartmentSerializer
#end read model

# update model
class Update_Department_Api_View(UpdateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
#end update model

# delete model
class Delete_Department_Api_View(DestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
# end delete model
#"""""End CRUD Department Model""

#"""""Start CRUD Room  Model"""
# create model
class Create_Room_Api_View(CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
# end create model

# read model
class Get_All_Room_Items(ListAPIView):
    queryset = Room.objects.all().order_by('-id')
    serializer_class = RoomSerializer
#end read model

# update model
class Update_Room_Api_View(UpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
#end update model

# delete model
class Delete_Room_Api_View(DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
# end delete model
#"""""End CRUD Room Model""

#"""""Start CRUD Income Model"""
# create model
class Create_Income_Api_View(CreateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
# end create model

# read model
class Get_All_Income_Items(ListAPIView):
    queryset = Income.objects.all().order_by('-id')
    serializer_class = IncomeSerializer
#end read model

# update model
class Update_Income_Api_View(UpdateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
#end update model

# delete model
class Delete_Income_Api_View(DestroyAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
# end delete model
#"""""End CRUD Income Model""

#"""""Start CRUD Revenue Model"""
# create model
class Create_Revenue_Api_View(CreateAPIView):
    queryset = Revenue.objects.all()
    serializer_class = RevenueSerializer
# end create model

# read model
class Get_All_Revenue_Items(ListAPIView):
    queryset = Revenue.objects.all().order_by('-id')
    serializer_class = RevenueSerializer
#end read model

# update model
class Update_Revenue_Api_View(UpdateAPIView):
    queryset = Revenue.objects.all()
    serializer_class = RevenueSerializer
#end update model

# delete model
class Delete_Revenue_Api_View(DestroyAPIView):
    queryset = Revenue.objects.all()
    serializer_class = RevenueSerializer
# end delete model
#"""""End CRUD Revenue Model""

#"""""Start CRUD Info_about_clinic Model"""
# create model
class Create_Info_about_clinic_Api_View(CreateAPIView):
    queryset = Info_about_clinic.objects.all()
    serializer_class = Info_about_clinicSerializer
# end create model

# read model
class Get_All_Info_about_clinic_Items(ListAPIView):
    queryset = Info_about_clinic.objects.all().order_by('-id')
    serializer_class = Info_about_clinicSerializer
#end read model

# update model
class Update_Info_about_clinic_Api_View(UpdateAPIView):
    queryset = Info_about_clinic.objects.all()
    serializer_class = Info_about_clinicSerializer
#end update model

# delete model
class Delete_Info_about_clinic_Api_View(DestroyAPIView):
    queryset = Info_about_clinic.objects.all()
    serializer_class = Info_about_clinicSerializer
# end delete model
#"""""End CRUD Info_about_clinic Model""

#"""""Start CRUD Equipment Model"""
# create model
class Create_Equipment_Api_View(CreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
# end create model

# read model
class Get_All_Equipment_Items(ListAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
#end read model

# update model
class Update_Equipment_Api_View(UpdateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
#end update model

# delete model
class Delete_Equipment_Api_View(DestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
# end delete model
#"""""End CRUD Equipment Model""

#"""""Start CRUD Attendance Model"""
# create model
class Create_Attendance_Api_View(CreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
# end create model

# read model
class Get_All_Attendance_Items(ListAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
#end read model

# update model
class Update_Attendance_Api_View(UpdateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
#end update model

# delete model
class Delete_Attendance_Api_View(DestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
# end delete model
#"""""End CRUD Attendance Model""
