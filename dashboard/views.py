from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login

# Create your views here.
def addministratorDashboard(request):
    return render(request, 'addministratorDashboard.html')

def coordinator(request):
    return render(request, 'coordinator.html')

def coordinatorDashboard(request):
    return render(request, 'coordinatorDashboard.html')

def gradebook(request):
    return render(request, 'gradebook.html')

def projectManagementDashboard(request):
    return render(request, 'projectManagementDashboard.html')

def regAdmin(request):
    return render(request, 'regAdmin.html')

def adminCreateCoordinator(request):
    return render(request, 'adminCreateCoordinator.html')

def adminCreatestudent(request):
    return render(request, 'adminCreatestudent.html')

def adminCreateSupervisor(request):
    return render(request, 'adminCreateSupervisor.html')

def StudentDashboard(request):
    return render(request, 'StudentDashboard.html')

def supervisorDashboard(request):
    return render(request, 'supervisorDashboard.html')

def index(request):
    return render(request, 'index.html')

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('customer')
            elif user is not None and user.is_employee:
                login(request, user)
                return redirect('employee')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})





