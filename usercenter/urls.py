#!/usr/bin/env python
# coding=utf-8
from django.conf.urls import include, url

urlpatterns = [
    url(r'^register$','usercenter.views.user_register',name='usercenter_register'),
    url(r'^logout','django.contrib.auth.views.logout_then_login',name='logout_then_login'),
]
