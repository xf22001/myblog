# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
	name=models.CharField(max_length=80)
	sortnum=models.IntegerField(default=10)
	articles=models.IntegerField(default=0)
	user_id=models.IntegerField(default=0)

	def __str__(self):
		return self.name.encode('utf-8')

class Article(models.Model):
	channel1_id=models.IntegerField(default=0)
	channel2_id=models.IntegerField(default=0)
	category=models.ForeignKey(Category)
	title=models.CharField(max_length=200)
	pic=models.CharField(max_length=80)
	tags=models.CharField(max_length=120)
	summary=models.CharField(max_length=500)
	content=models.TextField()
	createtime=models.DateTimeField('create time', default=timezone.now())
	views=models.IntegerField(default=0)
	comments=models.IntegerField(default=0)
	goods=models.IntegerField(default=0)
	bads=models.IntegerField(default=0)
	status=models.IntegerField(default=1)	   #1发布；0草稿
	user_id=models.IntegerField(default=1)
	username=models.CharField(max_length=80)
	ishome=models.IntegerField(default=0)	   #1发布；0草稿
	isrecommend=models.IntegerField(default=0)	   #1发布；0草稿
	istop=models.IntegerField(default=0)	   #1发布；0草稿
	isoriginal=models.IntegerField(default=1)	   #1发布；0草稿
	cancomment=models.IntegerField(default=1)	   #1发布；0草稿
	password=models.CharField(max_length=80)	   #1发布；0草稿

	def __str__(self):
		return self.title.encode('utf-8')

class Comment(models.Model):
	article=models.ForeignKey(Article)
	user_id=models.IntegerField(default=0)
	username=models.CharField(max_length=80)
	content=models.TextField()
	createtime=models.DateTimeField('create time', default=timezone.now())
	goods=models.IntegerField(default=0)
	bads=models.IntegerField(default=0)
	reply_id=models.IntegerField(default=0)

	def __str__(self):
		return self.content.encode('utf-8')
	
  
class UserProfile(models.Model):
	user=models.ForeignKey(User, unique=True)
	#头像
	avatar=models.ImageField(upload_to='avatar')

	#基本信息
	nickname=models.CharField(max_length=80)
	realname=models.CharField(max_length=80)
	gender=models.IntegerField(default=0)
	birthday=models.DateTimeField('birthday', default=timezone.now())
	birthcity=models.CharField(max_length=80)
	residecity=models.CharField(max_length=80)

	#个人信息
	affectivestatus=models.IntegerField(default=0)
	lookingfor=models.IntegerField(default=0)
	bloodtype=models.IntegerField(default=0)
	site=models.CharField(max_length=80)
	bio=models.CharField(max_length=255)
	interest=models.CharField(max_length=255)
	sightml=models.CharField(max_length=255)
	timeoffset=models.CharField(max_length=80)
   
	#联系方式
	qq=models.CharField(max_length=80)
	msn=models.CharField(max_length=80)
	taobao=models.CharField(max_length=80)
	email=models.CharField(max_length=80)
	phone=models.CharField(max_length=80)
	mobile=models.CharField(max_length=80)
	address=models.CharField(max_length=80)
	zipcode=models.CharField(max_length=80)

	def __str__(self):
		return self.nickname.encode('utf-8')

class Blog(models.Model):
	user_id=models.IntegerField(default=0)
	domain=models.CharField(max_length=200)
	title=models.CharField(max_length=200)
	description=models.CharField(max_length=200)
	keywords=models.CharField(max_length=200)
	about=models.CharField(max_length=500)
	announcement=models.CharField(max_length=500)
	modules=models.CharField(max_length=200)
	template=models.CharField(max_length=50)
	css=models.CharField(max_length=500)
	headhtml=models.CharField(max_length=500)
	footerhtml=models.CharField(max_length=500)
	todayviews=models.IntegerField(default=0)
	totalviews=models.IntegerField(default=0)
	articles=models.IntegerField(default=0)
	comments=models.IntegerField(default=0)
	createtime=models.DateTimeField('create time', default=timezone.now())

	def __str__(self):
		return self.title.encode('utf-8')

class Channel(models.Model):
	parent_id=models.IntegerField(default=0)
	name=models.CharField(max_length=80)
	sortnum=models.IntegerField(default=10)
	articles=models.IntegerField(default=0)
	users=models.IntegerField(default=0)
	user_id=models.IntegerField(default=0)
	username=models.CharField(max_length=80)
	isenable=models.IntegerField(default=1)

	def __str__(self):
		return self.name.encode('utf-8')
