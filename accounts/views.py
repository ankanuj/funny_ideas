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
        post = Post.objects.all().order_by('-id')
        comment =  Comment.objects.all().order_by('-id')
       

        context={
            'user':user,
            'post':post,
            'profile':profile,
            'comment':comment,
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

def terms(request):         
    return render(request,'blog/terms_and_conditions.html')

@login_required(login_url='home')
def profile(request,pk=None):
    if pk:
        user = User.objects.get(pk = pk)
    else:
        user = request.user
    profile = Profile.objects.get(user = user)
    post = Post.objects.all().filter(user_id = user.id).order_by('-date')

    content = {
        'user':user,
        'profile':profile,
        'post' : post,
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


@login_required(login_url='home')
def feedback(request):
    if request.method=='POST':
        user_id = request.user.id
        feedback = request.POST['feedback']
        feedbacks = Feedback(user_id = user_id,feedback = feedback)
        feedbacks.save()
        return redirect('home')
    else:
        return render(request,'blog/index.html')

    
def postdetail(request,pk):
    post = Post.objects.get(pk=pk)
    comment = Comment.objects.all().filter(post = post,reply=None).order_by('-id')
    user = request.user
    profile = Profile.objects.get(user = request.user)
    if request.method=='POST':
        user = request.user
        post = post
        comment = request.POST['comment']
        reply_qs = None
        comments = Comment(user=user,post=post,comment=comment,reply=reply_qs)
        comments.save()
        return redirect('comment',pk=pk)
    context = {
            'comment':comment,
            'profile':profile,
            'user':user,
            'post':post,
        }
    return render(request,'accounts/comment.html',context)


def edit_post(request,pk):
    user = request.user
    post = Post.objects.get(pk=pk)
    profile = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        user_id = user.id
        heading = request.POST['heading']
        content = request.POST['content']
        update = Post(pk=pk,heading=heading,content=content,user_id=user_id)
        update.save()
        return redirect('home')

    context = {
        'profile':profile,
        'user':user,
        'post':post,
    }
    return render(request,'accounts/edit_post.html',context)





def delete_post(request,pk):
    user = request.user
    post = Post.objects.get(pk=pk)
    profile = Profile.objects.get(user = request.user)
    if request.method=='POST':
        post.delete()
        return redirect('home')
    context = {
        'profile':profile,
        'user':user,
        'post':post,
    }
    return render(request,'accounts/delete_post.html',context)


def create_reply(request,pk):
    post = Post.objects.get(pk=pk)
    if request.method=='POST':
        user = request.user
        post = post
        comment = request.POST['comment']
        reply_id = request.POST['comment_id']
        reply_qs = None
        if reply_id is not None:
            reply_qs = Comment.objects.get(id=reply_id)
        comments = Comment(user=user,post=post,comment=comment,reply=reply_qs)
        comments.save()
        return redirect('comment',pk=pk)
    else:
        return render(request,'accounts/comment.html')


def debate(request):
    debate = Debate.objects.all()
    context = {
        'debate':debate,
    }
    return render(request,'debate/debate.html',context)

def debate_details(request):
    if 'online_classes' in request.path :
        debate = Debate.objects.all().filter(topic = 'online class').order_by('-id')
    elif 'tour_of_duty' in request.path:
        debate = Debate.objects.all().filter(topic = 'Tour of Duty').order_by('-id')
    elif 'extend_lockdown' in request.path:
        debate = Debate.objects.all().filter(topic = 'Extend Lockdown').order_by('-id')

    context = {
        'debate':debate,
    }
    if request.method == 'POST':
        comment = request.POST['comment']
        topic = request.POST['topic']
        side = request.POST['side']
        user_id = request.user.id
        db = Debate(user_id = user_id , topic=topic , comment=comment,side=side)
        db.save()
        return render(request,'debate/debate_details.html',context)
    
    return render(request,'debate/debate_details.html',context)


def edit_debate(request, pk):
    debate = Debate.objects.get(pk=pk)
    if request.method == 'POST':
        comment = request.POST['comment']
        topic = debate.topic
        side = request.POST['side']
        user_id = request.user.id
        db = Debate(pk=pk,user_id = user_id , topic=topic , comment=comment,side=side)
        db.save()
        if debate.topic == 'online class':
            return redirect('debate_details_1')
        elif debate.topic == 'Tour of Duty':
            return redirect('debate_details_2')
        elif debate.topic == 'Extend Lockdown':
            return redirect('debate_details_3')
    

    context = {
        'debate':debate,

    }

    return render(request,  'debate/edit_debate.html',context)



def delete_debate(request,pk):
    user = request.user
    debate = Debate.objects.get(pk=pk)
    if request.method=='POST':
        if debate.topic == 'online class':
            debate.delete()
            return redirect('debate_details_1')
        elif debate.topic == 'Tour of Duty':
            debate.delete()
            return redirect('debate_details_2')
        elif debate.topic == 'Extend Lockdown':
            debate.delete()
            return redirect('debate_details_3')

    context = {
       
        'debate':debate,
    }
    return render(request,'debate/delete_debate.html',context)

