from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import HOME, HEAD, ABOUTUS, FOOTER, ARTICLE, REGISTER
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from .models import NewPage
import time


Account_name = ""
flag = 0
# Create your views here.
def tag_gen(tmp):
	ps=PorterStemmer()
	question=[]
	answer=[]
	
	qid=tmp
	question.append(tmp.Heading)
	answer.append(tmp.Description)
	answer1=" ".join(answer)
	question1=" ".join(question)
	question1=question1.lower()
	answer1=answer1.lower()
	answer=word_tokenize(answer1)

	stop=set(stopwords.words('english'))
	faltu=[',','.','hello','hi']
	for w in faltu:
		stop.add(w)
	question=word_tokenize(question1)
	tags=[]
	for word in question:
		m=ps.stem(word)
		tags.append(m)
	words=''
	partial_token=[]
	for words in tags:
		if words not in stopf:
			partial_token.append(words)
	tags=[]
	for words in partial_token:
		if words not in tags:
			tags.append(words)

	taga=[]
	for word in answer:
		taga.append(ps.stem(word))
	partial_token=[]
	for words in taga:
		if words not in stop:
			partial_token.append(words)
	words=''
	for words in partial_token:
		if words not in tags:
			tags.append(words)
	return tags

def login(request):
	global Account_name
	global flag 
	if request.method == "POST":
		data = request.POST
		if data['login_popup']:		
			em = data['email']
			pa = data['password']
			r = REGISTER.objects.filter(Email=em, Password=pa)
			if(len(r)>0):
				flag=1
				Account_name=r[0].First_name
				print(Account_name)


		return redirect("/home/")

def home(request):
	global Account_name
	if request.method =="POST":
		print("in here")
		data = request.POST
		try:
			if data['sub_popup']:
				print("in sub popup")
				article = ARTICLE(Heading = data['head1'], Description = data['des1'], User = Account_name)
				article.save()
				tmp=ARTICLE.objects.all().last()
				l=tag_gen(tmp)
				l1 = " ".join(l)
				tmp = ARTICLE.objects.all().last()
				tmp.tags = l1
				a=time.ctime()
				a=a[0:10]+a[19:]
				tmp.Time_date=a
				tmp.save()

		except Exception as e:
			print("exception",e)	
	length=0
	context = {}
	
	home = HOME.objects.all()
	l = len(home)
	tmp=ARTICLE.objects.all()
	context = {'company_name':home[l-1].Company_name, 'caption':home[l-1].Caption,
	 'back_img': home[l-1].Back_img, 'curosal1': home[l-1].Curosal1,
	  'curosal2': home[l-1].Curosal2, 'news_title': home[l-1].News_title,
	   'news_img': home[l-1].News_img, 'News_des': home[l-1].News_des, 'account_name':Account_name}
	tmp=(ARTICLE.objects.all()).reverse()
	if len(tmp)!=length:
		context["tmp"]=tmp
		length=len(tmp)
	print(Account_name)
	return render(request,'home.html',context)

	

def about(request):
	context = {}
	aboutus = ABOUTUS.objects.all()
	l = len(aboutus)
	context = {'about_us': aboutus[l-1].About_us, 'aim': aboutus[l-1].Aim, 'content': aboutus[l-1].Content, 'image': aboutus[l-1].Image, 'developer': aboutus[l-1].Developer }
	return render(request,'aboutus.html',context)

def forum(request):
	return render(request, 'forum.html',{})

def news(request):
	return render(request, 'latest_news.html',{})



def user_profile(request):
	return render(request, 'profile.html',{})

def admin_home(request):
	if request.method == "POST":
		data = request.POST
		home = HOME(Company_name = data['company_name'], Caption = data['caption'], Back_img = data['back_img'], Curosal1 = data['curosal1'], Curosal2 = data['curosal2'], News_title = data['news_title'], News_img = data['news_img'], News_des = data['news_des'])
		home.save()
	return render(request, 'admin_home.html',{})

def admin_header(request):
	if request.method =='POST':
		data = request.POST
		head = HEAD(App_link = data['app_link'], Login_link = data['login_link'])
		head.save()
		head1=HEAD.objects.all()
		l = len(head1)
		context = {'applink':head1[l-1].App_link, 'loginlink': head1[l-1].Login_link}
		return render(request, 'header.html', context)
	return render(request, 'admin_header.html',{})

def admin_navbar(request):
	return render(request, 'admin_navbar.html',{})

def admin_footer(request):
	if request.method=="POST":
		data = request.POST
		foot = FOOTER(Disclaimer=data['disclaimer'], Email=data['email'], Phone=data['phone'], Facebook=data['facebook'], Twitter=data['twitter'], Google=data['google'], Instagram=data['instagram'], Terms=data['terms'])
		foot.save()
		foot1 = FOOTER.objects.all()
		l = len(foot1)
		context = {'disclaimer':foot1[l-1].Disclaimer, 'email':foot1[l-1].Email, 'phone':foot1[l-1].Phone, 'facebook':foot1[l-1].Facebook, 'twitter':foot1[l-1].Twitter, 'google':foot1[l-1].Google, 'instagram':foot1[l-1].Instagram, 'terms': foot1[l-1].Terms}
		return render(request, 'footer.html', context)
	return render(request, 'admin_footer.html',{})

def admin_latestnews(request):
	return render(request, 'admin_latestnews.html',{})

def admin_profilepage(request):
	return render(request, 'admin_profilepage.html',{})

def admin_aboutus(request):
	if request.method == 'POST':
		data = request.POST
		aboutus = ABOUTUS(About_us = data['about_us'], Aim = data['aim'], Content = data['content'], Image = data['image'], Developer = data['developer'])
		aboutus.save()
	return render(request, 'admin_aboutus.html',{})

def admin_registerpage(request):
	return render(request, 'admin_registerpage.html',{})

def admin_category(request):
	return render(request, 'admin_category.html',{})

def register(request):
	if request.method=="POST":
		data = request.POST
		pass1 = data['password']
		pass2 = data['password1']
		if pass1==pass2:
			reg = REGISTER(First_name = data['first_name'], Last_name = data['last_name'], Gender = data['gender'], 
			Email = data['email'], Password = data['password'], Institution = data['institution'], Phone = data['phone'],
			Date = data['date'], OTP = data['otp'])
			reg.save()
			return render(request,'home.html',{})
		else:
			context = {'print_status': "Both passwords don't match. Enter again!!!" }
			return render(request, 'register.html', context )
	return render(request,'register.html',{})

def header(request):
	return render(request, 'header.html', {})

def logout(request):
	global Account_name
	Account_name = ""
	return redirect('/home/')


def news(request):
	print("****************")
	if request.POST.get('Signup') == "Submit":
	    data=request.POST
	    recent=NewPage(slider_heading=data["slider_heading"], slider_caption=data["slider_caption"], image_link=data["image_link"], heading=data["heading"], image1_link=data["image1_link"],contents=data["contents"])
	    recent.save()
	'''context={'slider_heading':recent.slider_heading}
	context={'slider_caption':recent.slider_caption}
	context={'image_link':recent.image_link}
	print(recent.slider_heading)'''

	new=NewPage.objects.all()
	id = len(new)
	print(new[id-1])
	data1=new[id-1].slider_heading
	data2=new[id-1].slider_caption
	data3=new[id-1].image_link
	print(data3)
	print(new[id-1].image1_link)
	context={'slider_heading': data1, 'slider_caption': data2, 'image_link': data3, 'obj_list':new}
	print(data1)
	return render(request, "latest_news.html",  context)

def question_page(request):
	return render(request,"answer.html",{})

def read_more(request):
	return render(request,"article.html",{})