from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from boards.forms import PostForm
from boards.models import Post
from django.contrib import messages
def error(request):
    return render(request, 'accounts/error.html')

#@login_required(login_url='/login')
def create(request):
    if request.method =='GET':
        postForm = PostForm()

        return render(request, 'board/create.html',{'postForm':postForm})
    elif request.method == 'POST':
        # post = Post()
        # post.title = request.POST.get('title')
        postForm = PostForm(request.POST)
        context = {
            'postForm':postForm,'has_error':False
        }

        post = Post()
        post.title = request.POST.get('title')

        if len(post.title)<5:
            messages.add_message(request,messages.ERROR,'제목은 5글자 이상이어야 합니다.')
            context['has_error']=True

        post.contents = request.POST.get('contents')
        post.writer = request.user
        if context['has_error']:
            return render(request, 'board/create.html', context,status = 400)
        post.save()
        return redirect('/board/read'+str(post.id))

# @login_required(login_url='/login')
# def read(request):
#     if request.method =='GET':
#         return render(request, 'board/create.html')
#     elif request.method == 'POST':
#         post = Post()
#         ids = request.POST.get('id')
#         post = Post.objects.get(id=ids)
#         if len(post.title)<5:
#             #에러페이지로 redirect
#             pass
#         else:
#             return redirect('/board/read'+str(post.id))

def atlistGet(request,bid):
    post = Post.objects.get(id=bid)
    print(post) # 이 윗부분이 내용 출력

    context = {'works':post,'bid':bid}
    return render(request,'board/list.html',context)


#@login_required(login_url='/login')
def deleteGet(request,bid):
    post = Post.objects.get(id=bid)
    if request.user != post.writer:
        return redirect('/login')

    post.delete()
    return redirect('/login')


def updateGet(request,bid):
    post = Post.objects.get(id=bid)
    if request.user != post.writer:
        return redirect('/board')
    if request.method == "GET":
        postForm = PostForm(instance=post)

        context = {
                   'postForm':postForm
                   }
        return render(request, 'board/update.html',context)
    elif request.method=="POST":
        postForm = PostForm(request.POST)
        print(postForm)
        if(postForm.is_valid()):
            post = postForm.save(commit=False)
            post.writer = request.user
            post.save()
        return redirect('/board')
def loginBoard(request):
    return render(request,'accounts/login.html')