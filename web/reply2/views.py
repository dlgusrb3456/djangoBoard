from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from board.models import Post
from reply2.forms import ReplyForm
from reply2.models import Reply

@login_required(login_url='/kakaologin')
def create(request,rid):

    if request.method == "POST":
        replyForm = ReplyForm(request.POST)
        if replyForm.is_valid():
            reply = replyForm.save(commit=False)
            post = Post()
            post.id = rid
            reply.post = post
            reply.writer = request.user
            reply.save()
        return redirect('/listAt/' + str(post.id))


def list(request):
    replys = Reply.objects.all().order_by('-id')
    replyForm = ReplyForm()
    return render(request, 'reply/list.html', {'replys':replys,'replyForm': replyForm})

def read(request, rid):
    reply = Reply.objects.get(id=rid)

    return render(request, 'reply/read.html', {'reply':reply})

@login_required(login_url='/kakaologin')
def delete(request, rid,bid):
    reply = Reply.objects.get(id=rid)
    if request.user != reply.writer:
        return redirect('/listAt/'+str(bid))
    reply.delete()

    return redirect('/listAt/'+str(bid))

@login_required(login_url='/kakaologin')
def update(request, rid,bid):
    reply = Reply.objects.get(id=rid)

    if request.user != reply.writer:
        return redirect('/listAt/'+str(bid))

    if request.method == "GET":
        replyForm = ReplyForm(instance=reply)
        return render(request, 'reply/create.html', {'replyForm': replyForm})
    elif request.method == "POST":
        replyForm = ReplyForm(request.POST, instance=reply)
        if replyForm.is_valid():
            reply = replyForm.save(commit=False)
            reply.writer = request.user
            reply.save()
        return redirect('/listAt/'+str(bid))