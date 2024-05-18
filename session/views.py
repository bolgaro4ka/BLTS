from django.shortcuts import render, get_object_or_404
from .models import Session

from tests.views import add_test_ans
from django.http import HttpResponse, JsonResponse

from tests.models import Tests_for_user, Test

from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    all_sessions = Session.objects.all()
    len_sessions = len(all_sessions)
    len_test=[]
    firsts_index = []
    for session in all_sessions:
        
        testp = session.test
        len_test.append(len(testp.tasks.all()))

        first_index = session.test.tasks.first().id
        firsts_index.append(first_index)
        print(session, len_test)

    all_sessions = zip(all_sessions, len_test, firsts_index)
    print(all_sessions)

    return render(request, 'session/index.html', {'all_sessions': all_sessions, 'len_sessions': len_sessions})

@login_required(login_url='/a/login')
def session(request, id):
    session = Session.objects.get(id=id)
    session.users.add(request.user)
    session.answers.add(Tests_for_user.objects.get(user = request.user, test = session.test))
    session.save()

    res = add_test_ans(request, session.test)


    answers = session.answers.all()

    all_sessions = Session.objects.all()
    len_sessions = len(all_sessions)
    len_test=[]
    firsts_index = []
    for session in all_sessions:
        
        testp = session.test
        len_test.append(len(testp.tasks.all()))

        first_index = session.test.tasks.first().id
        firsts_index.append(first_index)
        print(session, len_test)

    all_sessions = zip(all_sessions, len_test, firsts_index)
    print(all_sessions)

    return render(request, 'session/session.html', {'session': session, 'answers': answers, 'res': res, 'all_sessions': all_sessions, 'len_sessions': len_sessions, 'session_id': id})

def leaderboard(request, id):
    session = get_object_or_404(Session, id=id)

    answers = session.answers.all().order_by('-points')
    return render(request, 'leaderboard/index.html', {'answers': answers, 'session': session})

def leaderboard_api(request, id):
    session = get_object_or_404(Session, id=id)

    answers = session.answers.all().order_by('-points')
    res = len(answers)
    return JsonResponse({'len':res})