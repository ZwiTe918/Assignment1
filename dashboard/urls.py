from django.urls import path
from . import views

urlpatterns = [
    path('', views.addministratorDashboard, name='addministratorDashboard'),
    path('', views.coordinator, name='coordinator'),
    path('', views.coordinatorDashboard, name='coordinatorDashboard'),
    path('', views.gradebook, name='gradebook'),
    path('', views.projectManagementDashboard, name='projectManagementDashboard'),
    path('', views.regAdmin, name='regAdmin'),
    path('', views.adminCreateCoordinator, name='adminCreateCoordinator'), 
    path('', views.adminCreatestudent, name='adminCreatestudent'),
    path('', views.adminCreateSupervisor, name='adminCreateSupervisor'),
    path('', views.StudentDashboard, name='StudentDashboard'),
    path('', views.supervisorDashboard, name='supervisorDashboard')
]