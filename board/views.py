from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

from .models import *
import os



def home(request):
    return render(request, 'board/home.html', {})


def join(request):
    if request.method == 'GET':
        return render(request, 'board/join.html', {})
    else:
        id = request.POST['id']
        pw = request.POST['pw']
        name = request.POST['name']

        m = Member(id=id, pw=pw, name=name)
        m.save()

        return render(request, 'board/join_result.html',
                      {'id': id, 'name': name})


def id_check(request):
    id = request.POST['id']
    try:
        Member.objects.get(id=id)
    except Member.DoesNotExist as e:
        pass

        res = {'id': id, 'msg': '가입가능'}
        return JsonResponse(res)
    else:
        res = {'id': id, 'msg': '가입불가'}
        return JsonResponse(res)


def login(request):
    if request.method == 'GET':

        return render(request, 'board/login.html', {})
    else:
        id = request.POST['id']
        pw = request.POST['pw']

        try:
            Member.objects.get(id=id, pw=pw)
        except Member.DoesNotExist:
            return redirect('login')

        else:
            request.session['id'] = id
            return redirect('/board/home')


def board1(request):
    page = request.GET['page']
    board_list = boardDb.objects.order_by('-id')
    paginator = Paginator(board_list, 10)
    page_info = paginator.page(page)
    return render(request, 'board/board1.html',{'page_info':page_info})




def writePage(request):
    return render(request, 'board/writePage.html', {})


def upload1(request):
    if request.method == 'GET':
        return render(request, '', {})
    else:
        upload_file = request.FILES['my_file']

        login_id = request.session['id']

    try:
        os.mkdir(login_id)
    except FileExistsError:
        pass

    with open(login_id + '/' + upload_file.name,
              'wb') as file:
        for chunk in upload_file.chunks():
            file.write(chunk)

    return HttpResponse('완료' + upload_file.name)

def insert(request):
    if request.method == 'GET':

        return render(request, 'board/writePage.html', {})
    else:
        title = request.POST['title']
        content = request.POST['content']

        boardDb.objects.create(title='title', content='content')

        return render(request, 'board/board1.html',{})





