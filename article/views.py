#coding:utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from models import Article
from block.models import Block
# Create your views here.

def article_list(request, block_id):
    b_id = int(block_id)
    block = Block.objects.get(id = b_id)
    articles = Article.objects.filter(block = block).order_by('-last_timestmp')
    return render_to_response('article_list.html', {'articles':articles,"b":block, 'title':u'文章列表'})
