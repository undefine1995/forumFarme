#coding:utf-8
from django.shortcuts import render
from models import Block
from django.shortcuts import render_to_response
# Create your views here.

def block_list(request):
    block = Block.objects.all().order_by('-id')
    return render_to_response("block_list.html",{'blo':block,'title':u'index'})
