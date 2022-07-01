# from datetime import datetime
import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect
# Create your views here.
from django.contrib import messages
# from tool.forms import loginform
# from tool.models import Attendance
from django.contrib.auth.models import AnonymousUser
from django.core.cache import cache
# from django.contrib.auth.views import logout, authenticate, login
from django.views.decorators.cache import cache_control
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

from . import models
from .forms import SignUpForm, EditProfileForm
from .models import Attendance, Times


def home(request):
    return render(request, "home.html")


def login_user(request):
    if request.method == 'POST': #if someone fills out form , Post it
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:# if user exist
            login(request, user)
            messages.success(request,(f'hii {username} You are now logined'))
            return redirect('admin') #routes to 'home' on successful login
        elif user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.success(request,('Error logging in'))

            return redirect('login') #re routes to login page upon unsucessful login
    else:
        return render(request, 'login.html', {})

#
def profile(request):
    return render(request,"profile.html")

def registeration(request):
    return render(request,"registeration.html")

def attend(request):
    attend = Attendance.objects.filter(user=request.user)

    return render(request,"attend.html", {'attend':attend})

def adminpage(request):
    user = Attendance.objects.all().values('user').distinct()
    attends = Attendance.objects.raw("SELECT DISTINCT id,username FROM auth_user")
    return render(request, "adminpage.html",{'user':user,'attends':attends})

# def login_user(request):
#     # if request.user.is_authenticated:
#     #     return render(request, 'home.html')
#     if request.method == 'POST':
#         form = loginform(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user=authenticate(request,
#                               username=cd["username"],
#                               password=cd["password"])
#             if user is not None:
#                 login(request, user)
#                 return HttpResponse("success")
#             else:
#                 # messages.success(request, f'Hi {username}, your account was created successfully')
#                 return HttpResponse("failed")
#
#     else:
#         form = loginform()
#         return render(request, 'login.html', {'form': form})
#



    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return redirect('/profile') #profile
    #     else:
    #         msg = 'Error Login'
    #         form = AuthenticationForm(request.POST)
    #         return render(request, 'profile.html', {'form': form, 'msg': msg})
    # else:
    #     form = AuthenticationForm()
    #     return render(request, 'profile.html', {'form': form})
@csrf_exempt
def insert(request):
    if request.method == "POST":
        member = Attendance(add=request.POST.get('add'), user=request.POST.get('user'))
        # , last_name=request.POST['last_name'],
        # address=request.POST['address'], user_name=request.POST['user_name'])
        member.save()

        clock_in = datetime.datetime.now()
        add_clock_in = models.Attendance.objects.create(clock_in=clock_in)
        add_clock_in.save()

        clock_out = datetime.datetime.now()
        duration = clock_out - clock_in

        add_clock_get = models.Attendance.objects.all()

    return render(request, 'registeration.html')
    # current_user = request.user
    # print(user.id)

def inserts(request):
    if request.method == "POST":
        member = Times(time=request.POST.get('time'))
        # , last_name=request.POST['last_name'],
        # address=request.POST['address'], user_name=request.POST['user_name'])
        member.save()
    return render(request, 'attend.html')

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, (f'hii {username} You are now registered'))
            return redirect('admin')
    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'registeration.html', context)

@cache_control(no_cache=True, must_revalidate=True)
def logout_user(request):
    logout(request)
    # messages.success(request,('Youre now logged out'))
    # request.session.clear()
    # session.pop()
    # user.session_set.all().delete()
    return redirect('login')
    # return render(request, "home.html")

def admin(request):
    attends = Attendance.objects.raw("SELECT DISTINCT id,username FROM auth_user")
    return render(request, "admin.html",{'attends':attends})

def basepage(request):
    return render(request, "basepage.html")

def edit(request,id):
    # if request.method == "POST":
    #     id = request.POST.get('id')
        members = Attendance.objects.filter(user=id)
        context = {'member': members, 'id': id}
        return render(request, 'edit.html', context)
        # return HttpResponse("id")

