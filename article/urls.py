#!/usr/bin/env python
# coding=utf-8

from django.conf.urls import include, url

urlpatterns = [
        url(r'^lists/(?P<block_id>\d+)', 'article.views.article_list', name = 'article_list'),
        url(r'^create/(?P<block_id>\d+)','article.views.article_create', name = 'article_create'),
        url(r'^detail/(?P<article_id>\d+)', 'article.views.article_detail', name='article_detail'),
]
