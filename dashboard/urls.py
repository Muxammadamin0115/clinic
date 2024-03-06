from django.urls import path
from .views import *
urlpatterns = [
    #""""" Start CRUD Employee Urls"""
    path('create-employee-api-view/', Create_Employee_Api_View.as_view()),
    path('get-employee-items/', Get_All_Employee_Items.as_view()),
    path('update-employee-api-view/<int:pk>/', Update_Employee_Api_View.as_view()),
    path('delete-employee-api_view/<int:pk>/', Delete_Employee_Api_View.as_view()),
    #""""" End CRUD Employee Urls"""

    # """"" Start CRUD Patient Urls"""
    path('create-patient-api-view/', Create_Patient_Api_View.as_view()),
    path('get-patient-items/', Get_All_Patient_Items.as_view()),
    path('update-patient-api-view/<int:pk>/', Update_Patient_Api_View.as_view()),
    path('delete-patient-api_view/<int:pk>/', Delete_Patient_Api_View.as_view()),
    # """"" End CRUD Patient Urls"""

    # """"" Start CRUD Cassa Urls"""
    path('create-cassa-api-view/', Create_Cassa_Api_View.as_view()),
    path('get-cassa-items/', Get_All_Cassa_Items.as_view()),
    path('update-cassa-api-view/<int:pk>/', Update_Cassa_Api_View.as_view()),
    path('delete-cassa-api_view/<int:pk>/', Delete_Cassa_Api_View.as_view()),
    # """"" End CRUD Cassa Urls"""

    # """"" Start CRUD Payment Urls"""
    path('create-payment-api-view/', Create_Payment_Api_View.as_view()),
    path('get-payment-items/', Get_All_Payment_Items.as_view()),
    path('update-payment-api-view/<int:pk>/', Update_Payment_Api_View.as_view()),
    path('delete-payment-api-view/<int:pk>/', Delete_Payment_Api_View.as_view()),
    # """"" End CRUD Payment Urls"""

    # """"" Start CRUD Comment Urls"""
    path('create-comment-api-view/', Create_Comment_Api_View.as_view()),
    path('get-comment-items/', Get_All_Comment_Items.as_view()),
    path('update-comment-api-view/<int:pk>/', Update_Comment_Api_View.as_view()),
    path('delete-comment-api-view/<int:pk>/', Delete_Comment_Api_View.as_view()),
    # """"" End CRUD Comment Urls"""

    # """"" Start CRUD Operation Urls"""
    path('create-operation-api-view/', Create_Operation_Api_View.as_view()),
    path('get-operation-items/', Get_All_Operation_Items.as_view()),
    path('update-operation-api-view/<int:pk>/', Update_Operation_Api_View.as_view()),
    path('delete-operation-api-view/<int:pk>/', Delete_Operation_Api_View.as_view()),
    # """"" End CRUD Comment Urls"""

    # """"" Start CRUD Department Urls"""
    path('create-department-api-view/', Create_Department_Api_View.as_view()),
    path('get-department-items/', Get_All_Department_Items.as_view()),
    path('update-department-api-view/<int:pk>/', Update_Department_Api_View.as_view()),
    path('delete-department-api-view/<int:pk>/', Delete_Department_Api_View.as_view()),
    # """"" End CRUD Department Urls"""

    # """"" Start CRUD Room Urls"""
    path('create-room-api-view/', Create_Room_Api_View.as_view()),
    path('get-room-items/', Get_All_Room_Items.as_view()),
    path('update-room-api-view/<int:pk>/', Update_Room_Api_View.as_view()),
    path('delete-room-api-view/<int:pk>/', Delete_Room_Api_View.as_view()),
    # """"" End CRUD Room Urls"""

    # """"" Start CRUD Income Urls"""
    path('create-income-api-view/', Create_Income_Api_View.as_view()),
    path('get-income-items/', Get_All_Income_Items.as_view()),
    path('update-income-api-view/<int:pk>/', Update_Income_Api_View.as_view()),
    path('delete-income-api-view/<int:pk>/', Delete_Income_Api_View.as_view()),
    # """"" End CRUD Income Urls"""

    # """"" Start CRUD Revenue Urls"""
    path('create-revenue-api-view/', Create_Revenue_Api_View.as_view()),
    path('get-revenue-items/', Get_All_Revenue_Items.as_view()),
    path('update-revenue-api-view/<int:pk>/', Update_Revenue_Api_View.as_view()),
    path('delete-revenue-api-view/<int:pk>/', Delete_Revenue_Api_View.as_view()),
    # """"" End CRUD Revenue Urls"""

    # """"" Start CRUD Revenue Urls"""
    path('create-info-about-clinic-api-view/', Create_Info_about_clinic_Api_View.as_view()),
    path('get-info-about-clinic-items/', Get_All_Info_about_clinic_Items.as_view()),
    path('update-info-about-clinic-api-view/<int:pk>/', Update_Info_about_clinic_Api_View.as_view()),
    path('delete-info-about-clinic-api-view/<int:pk>/', Delete_Info_about_clinic_Api_View.as_view()),
    # """"" End CRUD Info_about_clinic Urls"""

    # """"" Start CRUD Equipment Urls"""
    path('create-equipment-api-view/', Create_Equipment_Api_View.as_view()),
    path('get-equipment-items/', Get_All_Equipment_Items.as_view()),
    path('update-equipment-api-view/<int:pk>/', Update_Equipment_Api_View.as_view()),
    path('delete-equipment-api-view/<int:pk>/', Delete_Equipment_Api_View.as_view()),
    # """"" End CRUD Equipment Urls"""

    # """"" Start CRUD Attendance Urls"""
    path('create-attendance-api-view/', Create_Attendance_Api_View.as_view()),
    path('get-attendance-items/', Get_All_Attendance_Items.as_view()),
    path('update-attendance-api-view/<int:pk>/', Update_Attendance_Api_View.as_view()),
    path('delete-attendance-api-view/<int:pk>/', Delete_Attendance_Api_View.as_view()),
    # """"" End CRUD Attendance Urls"""
]