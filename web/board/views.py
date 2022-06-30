#from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from board.forms import PostForm
from board.models import Post, PostImage
from reply2.forms import ReplyForm


def mainPage(request):
    post = Post.objects.prefetch_related('postimage_set')
    print(post)  # 이 윗부분이 내용 출력


    # context = {'works': post, 'replyForm': replyForm, 'bid': bid}
    # return render(request, 'board/listAt.html', context)

    allPost = Post.objects.all().order_by('-id')
    print(allPost)
    context = {
        'works': allPost,
    }

    return render(request, 'board/index.html',context)

def createGet(request):
    if request.method == "GET":
        postForm = PostForm()
        return render(request,'board/create.html',{'postForm':postForm})
    elif request.method == "POST":
        postForm = PostForm(request.POST)

        if postForm.is_valid():
            post = postForm.save(commit=False)
            post.writer = request.user
            post.save()
            for image in request.FILES.getlist('image',None):
                postImage = PostImage()
                postImage.image = image
                postImage.post = post
                postImage.save()

        # post = postForm.save(commit=False)
        # post.title = request.POST.get('title',None)
        # post.contents = request.POST.get('contents',None)
        # post.writer = request.user
        # post.save()

        return redirect('/board')
    else:
        return redirect('/board')

def atlistGet(request,bid):
    post = Post.objects.prefetch_related('reply_set','postimage_set').get(id=bid)
    print(post) # 이 윗부분이 내용 출력
    replyForm = ReplyForm() #이건 새로 댓글 받아야 하니까 넣은거

    context = {'works':post,'replyForm':replyForm,'bid':bid}
    return render(request,'board/listAt.html',context)

@login_required(login_url='/kakaologin')
def deleteGet(request,bid):
    post = Post.objects.get(id=bid)
    if request.user != post.writer:
        return redirect('/board')

    post.delete()
    return redirect('/board')

@login_required(login_url='/kakaologin')
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


def like(request, bid):
    post = Post.objects.get(id=bid)
    user = request.user

    if post.like.filter(id=user.id).exists():
        post.like.remove(user)
        return JsonResponse({'message':'deleted','like_cnt':post.like.count()})
    else:
        post.like.add(user)
        return JsonResponse({'message': 'added','like_cnt':post.like.count()})