#coding:utf-8
from django.shortcuts import render_to_response,redirect
from django.contrib.auth.models import User
from django.template import RequestContext
from django.core.urlresolvers import reverse
# Create your views here.

def user_register(request):
    if request.method == 'GET':
        return render_to_response('usercenter_register.html',{},context_instance=RequestContext(request))
    else:
        username = request.POST['username'].strip()
        password = request.POST['password'].strip()
        re_password = request.POST['repassword'].strip()
        email = request.POST['email'].strip()
        
        error = ''
        if not username or not password or not re_password or not email:
            error = u'以上内容均不能为空'
        if password != re_password:
            error = u'两次输入密码不一致'
        if User.objects.filter(username = username).count()>0:
            error = u'该用户已存在'

        if not error:
            user = User.objects.create_user(username=username, password=password,email=email)

        else:
            return render_to_response('usercenter_register.html',{'error':error},context_instance = RequestContext(request))

    return redirect(reverse('login'))

