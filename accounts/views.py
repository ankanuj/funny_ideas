from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import *

def index(request):
    if request.user.is_authenticated:
        user = request.user
        profile = Profile.objects.get(user = request.user)
        post = Post.objects.all()
        context={
            'user':user,
            'post':post,
            'profile':profile,
        }
        if request.method=='POST':
            if user.is_authenticated:
                user_id = request.user.id
                heading = request.POST['heading']
                content = request.POST['content']
                posts=Post(heading=heading,content=content ,user_id=user_id)
                posts.save()
                return redirect('home')
            else:
                return redirect('home')
        return render(request,'blog/index.html',context)
    return render(request,'blog/index.html')

def about(request):         
    return render(request,'blog/about.html')

@login_required(login_url='home')
def profile(request):
    profile = Profile.objects.get(user = request.user)
    content = {
        'profile':profile,
    }
    if request.method=='POST':
        profile_photo = request.FILES['profile_photo']	
        profile.profile_photo = profile_photo
        profile.save()
        return redirect('profile')
    else:
        return render(request,'accounts/profile.html',content)

    return render(request,'accounts/profile.html',content)


@login_required(login_url='home')
def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect('home')


