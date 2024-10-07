"""
URL configuration for courseregister_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from core_app.views.course import CourseListAPIView, CourseDetailAPIView
from core_app.views.department import DepartmentListViewAPI, DepartmentDetailAPIView
from core_app.views.professor import ProfessorListViewAPI, ProfessorDetailAPIView
from core_app.views.student import StudentListViewAPI, StudentDetailAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('course',CourseListAPIView.as_view()),
    path('course/<int:pk>',CourseDetailAPIView.as_view()),
    path('department',DepartmentListViewAPI.as_view()),
    path('department/<int:pk>',DepartmentDetailAPIView.as_view()),
    path('professor',ProfessorListViewAPI.as_view()),
    path('professor/<int:pk>',ProfessorDetailAPIView.as_view()),
    path('student',StudentListViewAPI.as_view()),
    path('student/<int:pk>',StudentDetailAPIView.as_view()),
]
