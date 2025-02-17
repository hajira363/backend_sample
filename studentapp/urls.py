from django.urls import path
# from . import views
from .views import StudentListCreate,StudentRetrieveUpdateDistroy,FirstFiveStudent


urlpatterns=[
    path('students/',StudentListCreate.as_view(),name='student-list-create'),
    path('students/<int:pk>',StudentRetrieveUpdateDistroy.as_view(),name='student-detail'),
    path('students/first5/',FirstFiveStudent.as_view(),name='first-five-students'),
]
