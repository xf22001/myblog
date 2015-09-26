#-*- coding:utf-8 -*-
"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Add an import:  from blog import urls as blog_urls
	2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from myblog import settings

urlpatterns = [

	# Examples:

	url(r'^admin/', include(admin.site.urls)),

	url(r'^$', 'blog.viewsindex.index', name='index'),
	url(r'^channel/$', 'blog.viewsindex.channel',{"cid":1}, name='channel'),
	url(r'^test/$', 'blog.viewsindex.test', name='test'),
	url(r'^media/(?P<path>.*)','django.views.static.serve',{'document_root': settings.BASE_DIR + '/blog/static/'}),
	url(r'^static/(?P<path>.*)','django.views.static.serve',{'document_root': settings.BASE_DIR + '/blog/static/'}),
	
	url(r'^channel/(?P<cid>\d+)$', 'blog.viewsindex.channel', name='channel'),
	
	url(r'^accounts/login/$', 'blog.viewsuser.login', name='login'),
	url(r'^accounts/logout/$', 'blog.viewsuser.logout', name='logout'),
	url(r'^accounts/register/$', 'blog.viewsuser.register', name='register'),
	
	url(r'^(?P<uid>\d+)/pub/accounts/$', 'blog.viewsuserprofile.base', name='profilebase'),
	url(r'^(?P<uid>\d+)/pub/accounts/avatar/$', 'blog.viewsuserprofile.avatar', name='profileavatar'),
	url(r'^(?P<uid>\d+)/pub/accounts/contact/$', 'blog.viewsuserprofile.contact', name='profilecontact'),
	url(r'^(?P<uid>\d+)/pub/accounts/info/$', 'blog.viewsuserprofile.info', name='profileinfo'),
	url(r'^(?P<uid>\d+)/pub/accounts/security/$', 'blog.viewsuserprofile.security', name='profilesecurity'),
	
	url(r'^(?P<uid>\d+)/pub/config/$', 'blog.viewsblog.blog', name='configblog'),
	


	#文章显示部分
	url(r'^(?P<uid>\d+)/$', 'blog.viewsarticle.home', name='userhome'),
	url(r'^(?P<uid>\d+)/category/(?P<cid>\d+)$', 'blog.viewsarticle.category', name='articlecategory'),
	url(r'^(?P<uid>\d+)/show/(?P<aid>\d+)$', 'blog.viewsarticle.show', name='articleshow'),

	#文章管理部分
	url(r'^(?P<uid>\d+)/pub/article/list/$', 'blog.viewsarticle.list',name='articlelist'),
	url(r'^(?P<uid>\d+)/pub/article/list/draft/$', 'blog.viewsarticle.listdraft',name='articlelistdraft'),
	url(r'^(?P<uid>\d+)/pub/article/list/category/(?P<cid>\d+)$', 'blog.viewsarticle.listcategory',name='articlelistcategory'),
	url(r'^(?P<uid>\d+)/pub/article/add/$', 'blog.viewsarticle.add',name='articleadd'),
	url(r'^(?P<uid>\d+)/pub/article/edit/(?P<aid>\d+)$', 'blog.viewsarticle.edit', name='articleedit'),
	url(r'^(?P<uid>\d+)/pub/article/delete/(?P<aid>\d+)$', 'blog.viewsarticle.delete', name='articledelete'),

	#分类管理部分
	url(r'^(?P<uid>\d+)/pub/category/$', 'blog.viewscategory.index', name='category'),
	url(r'^(?P<uid>\d+)/pub/category/edit/(?P<cid>\d*)$', 'blog.viewscategory.edit', name='categoryedit'),
	url(r'^(?P<uid>\d+)/pub/category/delete/(?P<cid>\d*)$', 'blog.viewscategory.delete', name='categorydelete'),
]
