
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

        return redirect('login')


def id_check(request):
    id = request.POST['id']
    try:
        Member.objects.get(id=id)
    except Member.DoesNotExist as e:
        pass

        res = {'id': id, 'msg': '가입가능'}
        return JsonResponse(res)
    else:
        res = {'id': id, 'msg': '중복된 ID가 있습니다.'}
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
            return redirect('/board/afterlogin')
def afterlogin(request):
    return render(request, 'board/afterlogin.html', {})

def board1(request):
    page = request.GET.get('page')

    if not page:
        page = 1
    board_list = boardDb.objects.order_by('-id')
    paginator = Paginator(board_list, 10)
    page_info = paginator.page(page)
    return render(request, 'board/board1.html', {'page_info': page_info})

def detail(request):
    key = request.GET['content']
    content = boardDb.objects.get(id=key)
    return render(request, 'board/detail.html',{'content':content})





def writePage(request):
    if request.method == 'GET':
        return render(request, 'board/writePage.html',
                      {})
    else:
        title = request.POST['title']
        content = request.POST['content']

        upload_file=request.FILES['my_file']

        with open("board/static/board/img"+'/'+upload_file.name,'wb') as file:
            for chunk in upload_file.chunks():
                file.write(chunk)

        b = boardDb(title=title, content=content, file=upload_file.name)
        b.save()

        return redirect('/board/board1')












