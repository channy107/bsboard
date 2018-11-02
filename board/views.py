from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *

def home(request):

    return render(request, 'board/home.html', {})

def join(request):
    if request.method == 'GET':
        return render(request,'board/join.html',{})
    else:
        id = request.POST['id']
        pw = request.POST['pw']
        name = request.POST['name']

        m = Member(id=id, pw=pw, name=name)
        m.save()

        return render(request,'board/join_result.html',
                      {'id':id,'name':name})

def id_check(request):
    id = request.POST['id']
    try:
        Member.objects.get(id=id)
    except Member.DoesNotExist as e:
        pass

        res={'id':id, 'msg':'가입가능'}
        return JsonResponse(res)
    else:
        res={'id':id, 'msg':'가입불가'}
        return JsonResponse(res)

def login(request):
    if request.method == 'GET':

        return render(request, 'board/login.html', {})
    else:
        id = request.POST['id']
        pw = request.POST['pw']

        try:
            Member.objects.get(id=id,pw=pw)
        except Member.DoesNotExist:
            return redirect('login')

        else:
            request.session['id']=id
            return redirect('/board/home')

def board1(request):

    return render(request, 'board/board1.html', {})

def writePage(request):

    return render(request, 'board/writePage.html', {})