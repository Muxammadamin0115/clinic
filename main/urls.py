from django.urls import path
from .views import *

urlpatterns = [
    #"""""Start filter Employee Urls"""""
    path('filter-employee-by-user-username/', filter_employee_by_user_username_view),
    path('filter-employee-by-status/', filter_employee_by_status_view),
    path('filter-employee-by-work-time/', filter_employee_by_work_time_view),
    path('filter-employee-by-experience/', filter_employee_by_experience_view),
    path('filter-employee-by-department/', filter_employee_by_department_view),
    path('filter-employee-by-salary-view/', filter_employee_by_salary_view),
    path('filter-employee-by-room/', filter_employee_by_room_view),
    #"""""End filter Employee Urls"""""

    #"""""Start filter Patient Urls"""""
    path('filter-patient-by-doctor-view/', filter_patient_by_doctor_view),
    path('filter-patient-by-full_name/', filter_patient_by_full_name_view),
    path('filter-patient-by-gender/', filter_patient_by_gender_view),
    path('filter-patient-by-phone-number/', filter_patient_by_phone_number_view),
    path('filter-patient-by-room/', filter_patient_by_room_view),
    path('filter-patient-by-payment-status/', filter_patient_by_payment_status_view),
    # """""Start filter Patient Urls"""""

    # """""Start filter Room Urls"""""
    path('filter-room-by-name/', filter_room_by_name_view),
    path('filter-room-by-cost/', filter_room_by_cost_view),
    path('filter-room-by-department/', filter_room_by_department_view),
    path('filter-room-by-capacity/', filter_room_by_capacity_view),
    path('filter-room-by-status/', filter_room_by_status_view),
    path('filter-room-by-is-booked/', filter_room_by_is_booked_view),
    path('filter-room-by-equipment/', filter_room_by_equipment_view),
    # """""End filter Room Urls"""""

    # """""Start filter Payment Urls"""""
    path('filter-payment-by-patient/', filter_payment_by_patient_view),
    path('filter-payment-by-created-at/', filter_payment_by_created_at_view),
    path('filter-payment-by-payment-type/', filter_payment_by_payment_type_view),
    # """""Start filter Payment Urls"""""

    # """""Start filter Comment Urls"""""
    path('filter-comment-by-status/', filter_comment_by_status_view),
    # """""End filter Payment Urls"""""

    # """""Start filter Income Urls"""""
    path('filter-income-by-amount/', filter_income_by_amount_view),
    path('filter-income-by-data/', filter_income_by_data_view),
    # """""End filter Income Urls"""""

    # """""Start filter Revenue Urls"""""
    path('filter-revenue-by-amount/', filter_revenue_by_amount_view),
    path('filter-revenue-by-data/', filter_revenue_by_data_view),
    # """""End filter Revenue Urls"""""

    # """""Start filter Operation Urls"""""
    path('filter-operation-and-data-and-start-time/', filter_operation_by_data_and_start_time_view),
    path('filter-operation-by-patient/', filter_operation_by_patient_view),
    path('filter-operation-by-room/', filter_operation_by_room_view),
    path('filter-operation-by-start-and-end-time/', filter_operation_by_start_and_end_time_view),
    # """""End filter Operation Urls"""""

    # """""Start filter Department Urls"""""
    path('filter-department-by-name/', filter_department_by_name_view),
    # """""End filter Department Urls"""""

    # """""Start filter Department Urls"""""
    path('filter-equipment-by-name/', filter_equipment_by_name_view),
    # """""End filter Department Urls"""""

    # """""Start filter Attendance Urls"""""
    path('filter-attendance-by-employee/', filter_attendance_by_employee_view),
    path('filter-attendance-by-data/', filter_attendance_by_data_view),
    # """""End filter Attendance Urls"""""
    ]


