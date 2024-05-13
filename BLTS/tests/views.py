from django.shortcuts import render
from .models import *
from django.views.decorators.clickjacking import xframe_options_exempt
from .models import Test, Theme, Task, Answer_from_user, Tests_for_user
from .forms import TestSmallForm
from django.shortcuts import redirect
# Create your views here.
def index(request):
    return render(request, 'tests/index.html')
def listOfTests(request):
    tests = Test.objects.all()
    len_of_tests = len(tests)
    firsts_index = []
    lens = []
    for item in tests:
        print(len(item.tasks.all()))
        lens.append(len(item.tasks.all()))
        first_index_task = item.tasks.first().id
        firsts_index.append(first_index_task)
        print(first_index_task)

    print(zip(tests, lens, firsts_index))
    return render(request, 'tests/list-of-courses.html', {'tests': zip(tests, lens, firsts_index), 'len_of_tests': len_of_tests})

def test_view(request, id_test):
    tasks = Test.objects.get(id=id_test).tasks.all()
    complete = Answer_from_user.objects.filter(user=request.user)
    answers = Answer_from_user.objects.all()

    corrects=[]
    for item in complete:
        corrects.append(item.task)
        
    ans = Answer_from_user.objects.all().filter(user = request.user).filter( task = Test.objects.get(id=id_test).tasks.get(id=int(request.GET['id_task'])))[0].answer if Answer_from_user.objects.all().filter(user = request.user).filter( task = Test.objects.get(id=id_test).tasks.get(id=int(request.GET['id_task']))).exists() else ''
    if request.method == 'POST':
        form = TestSmallForm(request.POST)
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
            return redirect(f'/t/{id_test}/?id_task={request.GET["id_task"]}&output=embed')
    else:
        form = TestSmallForm()

    if request.method == 'GET':
        test = Test.objects.get(id=id_test).tasks.get(id=int(request.GET['id_task']))
        id_task = int(request.GET['id_task'])
        
        return render(request, 'tests/index.html', {'task': test, 'tasks': tasks, 'len': len(tasks), 'id_task': id_task, 'id_test': id_test, 'form': form, 'complete': complete, 'answers': answers, 'corrects': corrects, 'ans': ans})
    
@xframe_options_exempt

def test_view_iframe(request):
    if request.method == 'GET':
        print(Test.objects.get(id=int(request.GET['id_task'])).tasks.all())
        test = Test.objects.get(id=int(request.GET['id_task'])).tasks.get(id=int(request.GET['id_task']))
        return render(request, 'tests/task.html', {'task': test})
    
def end_view(request, id_test):
    test=Test.objects.get(id=id_test)
    tasks = test.tasks.all()

    
    answers = Answer_from_user.objects.all().filter(user = request.user).filter(task__in = tasks)
    
    res = 0

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

    print(answers, '()', tasks)
    



    return render(request, 'tests/end.html', {'res': res})
    