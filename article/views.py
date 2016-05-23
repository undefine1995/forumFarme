#coding:utf-8
from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.contrib import messages
from django.template import RequestContext
from django.contrib.auth.models import User
from models import Article
from block.models import Block

# Create your views here.

def article_list(request, block_id):
    b_id = int(block_id)
    block = Block.objects.get(id = b_id)
    articles = Article.objects.filter(block = block).order_by('-last_timestmp')
    return render_to_response('article_list.html', {'articles':articles,"b":block, 'title':u'文章列表'}, context_instance = RequestContext(request))

def article_create(request, block_id):
    b_id = int(block_id)
    block = Block.objects.get(id = b_id)
    if request.method == "GET":
        return render_to_response('article_create.html',{'blo':block}, context_instance = RequestContext(request))
    else:
        title = request.POST['title'].strip()
        content = request.POST['content'].strip()
        if not title or not content:
            messages.add_message(request,messages.ERROR,u'标题和内容均不能为空')
            return render_to_response('article_create.html',{'blo':block,'title':title,'content':content}, context_instance = RequestContext(request))
        ower = User.objects.all()[0]
        new_article = Article(title = title, content = content, block = block, ower = ower)
        new_article.save()
        messages.add_message(request, messages.INFO, u'添加成功')
        return redirect(reverse('article_list',args=[b_id,]))
