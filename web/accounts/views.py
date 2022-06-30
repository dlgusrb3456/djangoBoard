import requests
from django.contrib.auth import login
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect

from accounts.models import User2

lo_access_token=''

def func1(request):
    email = EmailMessage('test','test',to=['dlgusrb3456@naver.com'])
    result = email.send()
    return HttpResponse(result)


def loginPage(request):
    return render(request,'user/login.html')

def commonLogin(request):
    return render(request, 'user/login.html')
    pass

def logoutPage(request):
    kid = request.user
    user = User2.objects.filter(username=str(kid))
    print('가져온' + user.first().email)

    #로그아웃
    # print('asdf'+str(kid))

    # data = {
    #     'target_id_type': 'user_id',
    #     'target_id': user.first().email
    # }
    # headers = {'Authorization': 'KakaoAK fd2330cf034085ea7bea87b075171887'}
    #
    # res = requests.post('https://kapi.kakao.com/v1/user/logout', data=data, headers=headers)
    # print(res.json())

    #연결 끊기
    data2 = {
        'target_id_type': 'user_id',
        'target_id': user.first().email
    }
    headers2 = {'Authorization': 'KakaoAK fd2330cf034085ea7bea87b075171887'}

    res = requests.post('https://kapi.kakao.com//v1/user/unlink', data=data2, headers=headers2)

    print(res.json())

    return redirect('/accounts/logout')



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
    print(access_token)
    lo_access_token = access_token
    headers = {'Authorization': 'Bearer '+access_token,
               'Content-type':'application/x-www-form-urlencoded;charset=utf-8'}

    res = requests.get('https://kapi.kakao.com/v2/user/me',headers=headers)
    profile_json = res.json()
    print(profile_json['kakao_account']['profile']['nickname'])
    kakaoid = profile_json['id']
    print(kakaoid)

    user = User2.objects.filter(email=kakaoid)

    if user.first() is not None:
        login(request, user.first(), backend='django.contrib.auth.backends.ModelBackend')
    else:
        nuser = User2()
        nuser.username = profile_json['properties']['nickname']
        nuser.email = kakaoid
        nuser.save()
        login(request, nuser)

    return redirect('/board')


def profile(request):
    return render(request,'kakao/profile.html')

# def logout(request):
#     auth_logout(request)
#     return redirect('/board')