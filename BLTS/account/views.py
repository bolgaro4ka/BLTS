from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404
from django.views.decorators.clickjacking import xframe_options_exempt
from .forms import LoginForm, RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'account/index.html')

def login_view(request):
    if request.method == 'POST':
        error={}
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("/")
                else:
                    
                    error["name"]="Disabled account"
                    error["message"] = "Пользователь заблокирован. Обратитесь к администратору"

                    return HttpResponse('Disabled account')
            else:
                error["name"] = "Invalid login"
                error["message"] = "Неверное имя пользователя или пароль"
                return render(request, 'errors.html', {'error': error})
    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # Create a new user object but avoid saving it yet
            new_user = form.save(commit=False)
            # Set the chosen password
            new_user.set_password(form.cleaned_data['password'])
            # Save the User object
            new_user.save()


            user = authenticate(username=cd['username'], password=cd['password'])
            # Create the user profile
            login(request, user)
            return redirect("/")
    else:
        form = RegistrationForm()
    return render(request, 'account/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect("/")