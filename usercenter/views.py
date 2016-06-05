#coding:utf-8
from django.shortcuts import render_to_response,redirect
from django.contrib.auth.models import User
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.http import HttpResponse
from models import ActivateCode

import datetime
import uuid
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
            user.is_active = False
            user.save()

            new_code = str(uuid.uuid4()).replace('-','')
            code_record = ActivateCode(ower = user, Code = new_code, expiry_ti = datetime.datetime.now() + datetime.timedelta(days = 2))
            code_record.save()

            activate_link = "http://%s%s" % (request.get_host(),reverse("usercenter_activate",args=[new_code]))
            send_mail(u'激活邮件', u'您的激活链接为: %s' % activate_link, '897665949@qq.com',[email], fail_silently=False)

        else:
            return render_to_response('usercenter_register.html',{'error':error},context_instance = RequestContext(request))

    return redirect(reverse('login'))

def activate(request, code):
    query = ActivateCode.objects.filter(Code = code, expiry_ti__gte = datetime.datetime.now())
    if query.count()>0:
        code_record = query[0]
        code_record.ower.is_active = True
        code_record.ower.save()
        return HttpResponse("激活成功")
    else:
        return HttpResponse("激活失败")
