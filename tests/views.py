from django.shortcuts import render
from .models import *
from django.views.decorators.clickjacking import xframe_options_exempt
from .models import Test, Theme, Task, Answer_from_user, Tests_for_user
from .forms import TestSmallForm, TestBigForm, SearchForm
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'tests/index.html')


def req_data(tests):

    len_of_tests = len(tests)
    firsts_index = []
    lens = []
    for item in tests:
        print(len(item.tasks.all()))
        lens.append(len(item.tasks.all()))
        first_index_task = item.tasks.first().id
        firsts_index.append(first_index_task)
        print(first_index_task)

    iter_arr = zip(tests, lens, firsts_index)

    return {'len_of_tests': len_of_tests, 'tests': iter_arr}

def listOfTests(request):

    if request.method == 'GET' and 'sort' in request.GET:
        filter_search = request.GET['sort']

        if filter_search == 'time':
            tests = Test.objects.all().order_by('-updated_at')

        elif filter_search == 'desc':
            tests = Test.objects.all().order_by('-title')

        elif filter_search == 'name':
            tests = Test.objects.all().order_by('title')
            
        elif filter_search == 'clear':
            tests = Test.objects.all()

    else:
        tests = Test.objects.all()


    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            tests = tests.filter(title__icontains=form.cleaned_data['search'].lower())
            req = req_data(tests)
            return render(request, 'tests/list-of-courses.html', {'tests': req["tests"], 'len_of_tests': req["len_of_tests"], 'form': form})
        
    else:
        form = SearchForm()
    
    return render(request, 'tests/list-of-courses.html', {'tests': req_data(tests)["tests"], 'len_of_tests': req_data(tests)["len_of_tests"], 'form': form})

@login_required(login_url='/a/login' )
def test_view(request, id_test):
    tasks = Test.objects.get(id=id_test).tasks.all()
    complete = Answer_from_user.objects.filter(user=request.user)
    answers = Answer_from_user.objects.all()

    try:
        task_id = request.GET['id_task']
    except KeyError:
        error={}
        error["name"] = 'Отстуствует необходимый GET атрибут: task_id'
        error["message"] = 'Попробуйте перезайти на тест/сессию со страницы списка тестов/сессий'
        error["img"] = 'https://http.cat/503'
        return render(request, 'errors.html', {'error': error})

    try:
        session_id = request.GET['session']
    except KeyError:
        session_id = None

    print('Session! ', session_id)

    corrects=[]
    for item in complete:
        corrects.append(item.task)

    id_task = int(request.GET['id_task'])

    task = Task.objects.get(id=id_task)
        
    ans = Answer_from_user.objects.all().filter(user = request.user).filter( task = Test.objects.get(id=id_test).tasks.get(id=int(request.GET['id_task'])))[0].answer if Answer_from_user.objects.all().filter(user = request.user).filter( task = Test.objects.get(id=id_test).tasks.get(id=int(request.GET['id_task']))).exists() else ''
    if request.method == 'POST':

        form = TestBigForm(request.POST) if task.extend_ans_field else TestSmallForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if Answer_from_user.objects.all().filter(user = request.user).filter( task = Test.objects.get(id=id_test).tasks.get(id=int(request.GET['id_task']))).exists():
                new_ans = Answer_from_user.objects.all().filter(user = request.user).filter( task = Test.objects.get(id=id_test).tasks.get(id=int(request.GET['id_task'])))[0]
                new_ans.answer = cd['answer']
            else:
                new_ans = Answer_from_user.objects.create(
                    user = request.user,
                    task = Test.objects.get(id=id_test).tasks.get(id=int(request.GET['id_task'])),
                    answer = cd['answer'],
                    checked = True if Test.objects.get(id=id_test).tasks.get(id=int(request.GET['id_task'])).auto_check else False
                )
            new_ans.save()
            return redirect(f'/t/{id_test}/?id_task={request.GET["id_task"]}{"&session="+session_id if session_id else ""}')
    else:
        form = TestBigForm() if task.extend_ans_field else TestSmallForm()

    if request.method == 'GET':
        test = Test.objects.get(id=id_test).tasks.get(id=int(request.GET['id_task']))
        
        if task.extend_ans_field:
            return render(request, 'tests/indexb.html', {'task': test, 'tasks': tasks, 'len': len(tasks), 'id_task': id_task, 'id_test': id_test, 'form': form, 'complete': complete, 'answers': answers, 'corrects': corrects, 'ans': ans, 'session_id': session_id if session_id else ''})
        
        return render(request, 'tests/index.html', {'task': test, 'tasks': tasks, 'len': len(tasks), 'id_task': id_task, 'id_test': id_test, 'form': form, 'complete': complete, 'answers': answers, 'corrects': corrects, 'ans': ans, 'session_id': session_id if session_id else ''})
    
@xframe_options_exempt

def test_view_iframe(request):
    if request.method == 'GET':
        print(Test.objects.get(id=int(request.GET['id_task'])).tasks.all())
        test = Test.objects.get(id=int(request.GET['id_task'])).tasks.get(id=int(request.GET['id_task']))
        return render(request, 'tests/task.html', {'task': test})


def add_test_ans(request, test):
    tasks = test.tasks.all()
    res=0
    answers = Answer_from_user.objects.all().filter(user = request.user).filter(task__in = tasks)

    for item in answers:
        if item.task.auto_check and item.answer.lower() in item.task.right_answers.lower():
            res+=int(item.task.points)
    
    if Tests_for_user.objects.all().filter(user = request.user).filter(test = test).exists():
        a=Tests_for_user.objects.all().filter(user = request.user).filter(test = test)[0]
        a.ans.set(answers)
        a.points = res
        
    else:
        a=Tests_for_user.objects.create(user = request.user, test = test, points = res)
        a.ans.set(answers)
    a.save()

    return res

@login_required(login_url='/a/login')
def end_view(request, id_test):
    test=Test.objects.get(id=id_test)
    try: session_id = request.GET['session']
    except KeyError: session_id = None

    res = add_test_ans(request, test)
    
    if session_id:
        print('session detected') 
    return render(request, 'tests/end.html', {'res': res, 'session_id': session_id if session_id else ''})
    
