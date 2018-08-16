from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from .forms import LoginForm,RegisterForm,AcountForm
from django.contrib.auth import authenticate,login,logout
from .models import Account
from django.contrib.auth.models import User
# Create your views here.


def user_login(request):
    """
    登录
    :param request:
    :return:
    """
    if request.method == "POST":
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            formdata = loginform.cleaned_data
            username = formdata['username']
            password = formdata['password']
            user = authenticate(username=username,password=password)
            if user:
                login(request,user)
                return HttpResponseRedirect(reverse('blog:index'))
            else:
                return render(request,'account/login.html',{'message':'username or password error'})
        else:
            return render(request,'account/login.html',{'message':'username or password error'})

    if request.method == "GET":
        return render(request,'account/login.html')



def user_logout(request):
    """
    退出
    :param request:
    :return:
    """
    logout(request)
    return HttpResponseRedirect(reverse('blog:index'))


def register(request):
    """
    注册
    :param request:
    :return:
    """
    if request.method == "POST":
        registform = RegisterForm(request.POST)
        acountform = AcountForm(request.POST)
        if registform.is_valid()*acountform.is_valid():
            new_user = registform.save(commit=False)
            new_user.set_password(registform.cleaned_data['password'])
            new_user.save()
            new_acount = acountform.save(commit=False)
            new_acount.user = new_user
            new_acount.save()
            return HttpResponseRedirect(reverse('blog:index'))
        else:
            return render(request,'account/register.html',{'message':'error'})

    else:
        registform = RegisterForm()
        acountform = AcountForm()
        return render(request,'account/register.html',{'registform':registform,'acountform':acountform})