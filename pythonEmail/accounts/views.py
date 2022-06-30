import email

import requests
from django.contrib.auth import login

from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accounts.models import User


def func1(request):
    email = EmailMessage('test','test',to=['dlgusrb3456@naver.com'])
    result = email.send()
    return HttpResponse(result)


def loginPage(request):
    return render(request,'kakao/login.html')

def getcode(request):
    code = request.GET.get('code') #uri로 준 code 받기

    data = {
        'grant_type':'authorization_code',
        'client_id':'55c6f0b85593e50d7defe0cb04627c48',
        'redirect_uri':'http://127.0.0.1:8000/oauth/redirect',
        'code':code
    }

    headers = {'Content-type':'application/x-www-form-urlencoded;charset=utf-8'}

    res = requests.post('https://kauth.kakao.com/oauth/token',data=data,headers=headers)

    token_json = res.json()
    print(token_json)

    access_token = token_json['access_token']
    headers = {'Authorization':'Bearer '+access_token,
               'Content-type':'application/x-www-form-urlencoded;charset=utf-8'}

    res = requests.get('https://kapi.kakao.com/v2/user/me',headers=headers)
    profile_json = res.json()
    print(profile_json['kakao_account']['profile']['nickname'])
    kakaoid = profile_json['id']
    print(kakaoid)

    user = User.objects.filter(email=kakaoid)

    if user.first() is not None:
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
    else:
        user = User()
        user.username = profile_json['properties']['nickname']
        user.email = kakaoid
        user.save()
        login(request, user.get_email())


    return HttpResponse(code)

def profile(request):
    return render(request,'kakao/profile.html')