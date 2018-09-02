from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from .forms import LoginForm,RegisterForm,AcountForm,UserinfoForm,Userform,ChangepasswordForm
from django.contrib.auth import authenticate,login,logout
from .models import Account,Userinfo
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView

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
            user = User.objects.filter(username=registform.cleaned_data['username'])
            if user:
                #已存在用户
                return JsonResponse({"code":20002})
            new_user = registform.save(commit=False)
            new_user.set_password(registform.cleaned_data['password'])
            new_user.save()
            new_acount = acountform.save(commit=False)
            new_acount.user = new_user
            new_acount.save()
            new_userinfo = Userinfo()
            new_userinfo.user = new_user
            new_userinfo.save()
            return JsonResponse({"code":20001})
        else:
            return JsonResponse({"code":20004})

    else:
        registform = RegisterForm()
        acountform = AcountForm()
        return render(request,'account/register.html',{'registform':registform,'acountform':acountform})

@login_required(login_url='/account/login')
def myself(request):
    """
    个人主页
    :param request:
    :return:
    """
    if request.method == "POST":
        userform = Userform(request.POST)
        accountform = AcountForm(request.POST)
        if request.user:
            if userform.is_valid()&accountform.is_valid():
                usero = request.user
                account = Account.objects.filter(user=usero)
                account.update(**accountform.cleaned_data)
                usero.email = userform.cleaned_data['email']
                usero.save()
                return HttpResponseRedirect(reverse('account:myself'))
            else:
                users = request.user
                account = Account.objects.get(user=users)
                return render(request, 'blog/myself.html', {"users": users, "account": account,
                                                            "userform": userform, "accountform": accountform})
        else:
            return HttpResponseRedirect(reverse('account:login'))
    else:
        users = request.user
        account = Account.objects.get(user=users)
        return render(request,'blog/myself.html',{"users":users,"account":account})


@login_required(login_url='/account/login')
def userinfo(request):
    """
    用户详情
    :param request:
    :return:
    """
    if request.method == "POST":
        userinfoform = UserinfoForm(request.POST)
        if userinfoform.is_valid():
            cleandata = userinfoform.cleaned_data
            userinfo = Userinfo.objects.filter(user=request.user)
            userinfo.update(**cleandata)
            return HttpResponseRedirect(reverse('account:userinfo'))
        else:
            userinfo = Userinfo.objects.get(user=request.user)
            return render(request,'blog/userinfo.html',{"userinfo":userinfo,
                                                        "userinfoform":userinfoform})
    else:
        if request.user:
            userinfo = Userinfo.objects.get(user=request.user)
            return render(request,'blog/userinfo.html',{"userinfo":userinfo})


@login_required(login_url='/account/login')
def modifypassword(request):
    """
    修改密码
    :param request:
    :return:
    """
    if request.method == "POST":
        changepasswordform = ChangepasswordForm(request.POST)
        if changepasswordform.is_valid():
            old_password = request.POST.get('old_password')
            new_password = changepasswordform.cleaned_data['new_password']
            user = authenticate(username=request.user.username,password=old_password)
            if user:
                user.set_password(new_password)
                user.save()
                return HttpResponseRedirect(reverse('account:login'))
            else:
                return render(request, 'account/modifypasword.html', {"error": "原密码错误"})
        else:
            return render(request,'account/modifypasword.html',{"changepasswordform":changepasswordform})

    else:
        return render(request,'account/modifypasword.html')


@login_required(login_url='/account/login')
def my_image(request):
    """
    编辑头像
    :param request:
    :return:
    """
    if request.method == "POST":
        if request.user:
            img = request.POST['img']
            new_userinfo = Userinfo.objects.get(user=request.user)
            new_userinfo.photo = img
            new_userinfo.save()
            return HttpResponse('1')
        else:
            return HttpResponseRedirect(reverse('account:login'))
    else:
        return render(request,'blog/my_image.html')

