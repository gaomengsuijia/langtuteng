from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from .forms import LoginForm,RegisterForm,AcountForm,UserinfoForm,Userform,ChangepasswordForm,RestpasswordForm,ForgetpasswordForm
from django.contrib.auth import authenticate,login,logout
from .models import Account,Userinfo,Emailactivecode
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import base64
import os
from langtuteng import settings
import random
from django.views.generic.base import View
from utils.send_email import Sendemail
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
            print(img)
            img = img.split(',')[1]
            #将base64的图片解码，保存到硬盘
            img_name = 'userphone\\' + request.user.username + str(random.randint(1,100)) + '.png'
            img_path = os.path.join(settings.MEDIA_ROOT,img_name)
            print(img_path)
            with open(img_path, 'wb') as f:
                baseimg = base64.b64decode(img)
                f.write(baseimg)
            new_userinfo = Userinfo.objects.get(user=request.user)
            new_userinfo.photo = settings.MEDIA_URL + img_name
            new_userinfo.save()
            return HttpResponse('1')
        else:
            return HttpResponseRedirect(reverse('account:login'))
    else:
        return render(request,'blog/my_image.html')



class Forgetpassword(View):
    """
    忘记密码
    """
    def get(self,request,*args,**kwargs):
        forgetpasswordform = ForgetpasswordForm()
        print(forgetpasswordform)
        return render(request,'account/forgetpassword.html',{'forgetpasswordform':forgetpasswordform})


    def post(self,request,*args,**kwargs):
        forgetpasswordform = ForgetpasswordForm(request.POST)
        if forgetpasswordform.is_valid():
            #检查username是否存在
            user = User.objects.filter(username=forgetpasswordform.cleaned_data['username'])
            if user:
                #发送邮件
                email = user[0].email
                if email:
                    try:
                        Sendemail(sendtype='forgetpassword').send(email)
                    except Exception:
                        return render(request,'account/forgetpassword.html',{'message':'发送失败','forgetpasswordform':forgetpasswordform})
                    return render(request,'account/sendemailsuccess.html')

                else:
                    return render(request, 'account/forgetpassword.html', {'message': '邮件为空，请联系管理员','forgetpasswordform':forgetpasswordform})
            else:
                return render(request,'account/forgetpassword.html',{'message':'用户名不存在','forgetpasswordform':forgetpasswordform})
        else:
            return render(request,'account/forgetpassword.html',{'message':'邮件和用户名不合法','forgetpasswordform':forgetpasswordform})




class Resetpassword(View):
    """
    post修改密码
    """
    def get(self,request,email_code):
        """
        点击邮箱里面的链接激活
        :param request:
        :param email_code:
        :return:
        """
        email = Emailactivecode.objects.filter(email_code=email_code,is_delete=0)
        if email:
            # Emailactivecode.objects.filter(email_code=email_code).update(is_delete=1)
            return render(request,'account/resetpassword.html',{'email_code':email_code,'email':email[0].email})
        return HttpResponseRedirect(reverse('account:login'))

    def post(self,request,*args,**kwargs):
        restpasswordForm = RestpasswordForm(request.POST)
        if restpasswordForm.is_valid():
            email = restpasswordForm.cleaned_data['email']
            captcha = restpasswordForm.cleaned_data['captcha']
            captcha_code = Emailactivecode.objects.filter(email=email,email_code=captcha,is_delete=0)
            if captcha_code:
                #重置密码
                newpassword = restpasswordForm.cleaned_data['password1']
                users = User.objects.filter(email=email)
                for user in users:
                    user.set_password(newpassword)
                    user.save()
                #将激活码置为失效
                captcha_code.update(is_delete=1)
                return render(request,'account/resetsuccess.html')
            else:
                return HttpResponseRedirect(reverse('account:login'))

        else:
            email = restpasswordForm.cleaned_data['email']
            captcha = restpasswordForm.cleaned_data['captcha']
            return render(request,'account/resetpassword.html',{'email_code':captcha,'email':email,'restpasswordForm':restpasswordForm})






