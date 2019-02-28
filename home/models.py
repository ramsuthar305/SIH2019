from django.db import models

# Create your models here.
class HOME(models.Model):
    Company_name = models.CharField(max_length=200)
    Caption = models.CharField(max_length=500)
    Back_img = models.CharField(max_length=200)
    Curosal1 = models.CharField(max_length=200)
    Curosal2 = models.CharField(max_length=200)
    News_title = models.CharField(max_length=200)
    News_img = models.CharField(max_length=200)
    News_des = models.CharField(max_length=500)

class HEAD(models.Model):
    App_link = models.CharField(max_length=200)
    Login_link = models.CharField(max_length=200)

class ABOUTUS(models.Model):
    About_us = models.CharField(max_length=2000)
    Aim = models.CharField(max_length=200)
    Content = models.CharField(max_length=2000)
    Image = models.CharField(max_length=100)
    Developer = models.CharField(max_length=400)

class FOOTER(models.Model):
    Disclaimer= models.CharField(max_length=2000)
    Email = models.CharField(max_length=50)
    Phone = models.CharField(max_length=50)
    Facebook = models.CharField(max_length=50)
    Twitter = models.CharField(max_length=50)
    Google = models.CharField(max_length=50)
    Instagram = models.CharField(max_length=50)
    Terms = models.CharField(max_length=1000)

class ARTICLE(models.Model):
    Sr_no = models.CharField(max_length=20)
    Heading = models.CharField(max_length=1000)
    Description = models.CharField(max_length=4000)
    User = models.CharField(max_length=100)
    Time_date = models.CharField(max_length=20)
    tags = models.CharField(max_length=1000)

class REGISTER(models.Model):
    First_name = models.CharField(max_length=40)
    Last_name = models.CharField(max_length=40)
    Email = models.CharField(max_length=40)
    Password = models.CharField(max_length=40)
    Institution = models.CharField(max_length=40)
    Phone = models.CharField(max_length=20)
    Date = models.CharField(max_length=10)
    Gender = models.CharField(max_length=10)
    OTP = models.CharField(max_length=20)


class NewPage(models.Model):
    slider_heading = models.CharField(max_length=10000)
    slider_caption = models.CharField(max_length=10000)
    image_link = models.CharField(max_length=10000)

    heading = models.CharField(max_length=10000)
    image1_link = models.CharField(max_length=10000)
    contents = models.CharField(max_length=10000,default='SOME STRING')


class Question(models.Model):
    Question=models.CharField(max_length=100000)
    Answer=models.CharField(max_length=10000000)
    
    likes=models.IntegerField(max_length=10000)
    dislikes=models.IntegerField(max_length=10000)
    reports=models.IntegerField(max_length=10000)
    tags=models.CharField(max_length=1000000)

class Answer(models.Model):
    aid=models.AutoField(primary_key=True)
    likes=models.IntegerField(max_length=10000)
    dislikes=models.IntegerField(max_length=10000)
    reports=models.IntegerField(max_length=10000)
    tags=models.CharField(max_length=1000000)

class comment(models.Model):
    cid=models.AutoField(primary_key=True)
    likes=models.IntegerField(max_length=10000)
    dislikes=models.IntegerField(max_length=10000)
    reports=models.IntegerField(max_length=10000)

    


