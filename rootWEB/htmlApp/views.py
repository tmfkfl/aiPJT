from django.shortcuts import render

# Create your views here.

def index(request):
    print(">>>>>>>>debug, client url http://127.0.0.1:8000/html/index, index() call~~")
    return render(request,'html/index.html')

def tag(request):
    print(">>>>>>>>>>debug, client url http://127.0.0.1:8000/html/basic_tag, basic_tag() call~~")
    return render(request, 'html/tag.html')

def kts(request):
    print(">>>>>>>>>>debug, client url http://127.0.0.1:8000/html/kts_tag, kts_tag() call~~")
    return render(request, 'html/kts.html')


def main(request):
    print(">>>>>>>>debug, client url http://127.0.0.1:8000/html/main, main() call~~")
    return render(request,'html/main.html')

def form(request):
    print(">>>>>>>>debug, client url http://127.0.0.1:8000/html/form_tag, form() call~~")
    return render(request,'html/form.html')

def login(request):
    print(">>>>>>>>debug, client url http://127.0.0.1:8000/html/login, login() call~~")
    # return render(request,'html/form.html')
    # 1. 사용자의 아이디, 패스워드를 얻어와야한다.
    # 2. model -select
    # 3. 사용자 인증에 따른 화면분기(ok, fail)
    id = request.GET['user_id']
    pwd = request.GET['user_pwd']
    print('>>>>>>debug, params :', id, pwd)
    if id == 'kts' and pwd == 'kts' :
        context = {'nikName' : 'tmfkfl'}
        return render(request , 'html/ok.html', context)
    else:
        context = {'id': id}
        return render(request , 'html/fail.html', context)

def table(request):
    print(">>>>>>>>debug, client url http://127.0.0.1:8000/html/table_form, table_form() call~~")
    return render(request,'html/tableform.html')

def loginform(request):
    print(">>>>>>>>debug, client url http://127.0.0.1:8000/html/form_tag, form() call~~")
    return render(request,'html/loginform.html')


def login2(request):
    print(">>>>>>>>debug, client url http://127.0.0.1:8000/html/login2, login2() call~~")

    id = request.GET['user_id']
    pwd = request.GET['user_pwd']
    print('>>>>>>debug, params :', id, pwd)
    if id == 'kts' and pwd == 'kts' :
        context = {'nikName' : 'tmfkfl'}
        return render(request , 'html/oklogin.html', context)
    else:
        context = {'id': id}
        return render(request , 'html/fail.html', context)

