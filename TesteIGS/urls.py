"""
URL configuration for TesteIGS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from IGS_Employee_Manager import views

urlpatterns = [
    path('admin/', admin.site.urls),

    ### API route for employee data
    path('employee/', views.StaffMemberView.as_view(), name='staff_list'),

    ### API route for department data
    path('department/', views.DepartmentView.as_view(), name='department_list'),

    ### URL to public site
    path('public/', views.public_list, name='public_site')
]
