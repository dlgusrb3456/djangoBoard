from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from board.forms import PostForm
from board.models import Post, PostImage

def read(request,bid):
    allPost = Post.objects.prefetch_related('postimage_set').get(id=bid)
    context = {
        'post':allPost
    }
    return render(request,'board/read.html',context)

def mainPage(request):
    allPost = Post.objects.all().order_by('-id')
    context = {
        'works': allPost,
    }

    return render(request, 'board/main.html',context)



def createGet(request):
    if request.method == "GET":
        postForm = PostForm()
        return render(request,'board/create.html',{'postForm':postForm})
    elif request.method == "POST":

        postForm = PostForm(request.POST)
        if postForm.is_valid():
            post = postForm.save(commit=False)
            post.save()
            for image in request.FILES.getlist('image',None):
                postImage = PostImage()
                postImage.image = image
                postImage.post = post
                postImage.save()

        return redirect('/board/mainpage')
    else:
        return redirect('/board/mainpage')




