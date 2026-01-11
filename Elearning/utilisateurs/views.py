from django.shortcuts import render
from .forms import Userform,Profileform
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def accueil(request):
    return render(request, 'utilisateurs/index.html')

def register(request):
    registered = False
    if request.method == "POST":
        user_form = Userform(data=request.POST)
        profile_form = Profileform(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
            return HttpResponseRedirect('login')
        else:
            print(user_form.errors, profile_form.errors)
    
    else:
        user_form = Userform()
        profile_form = Profileform()

    content = {
        'registered': registered,
        'form1': user_form,
        'form2': profile_form,
    }
    
    return render(request, 'utilisateurs/register.html', content)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("L'utilisateur est desactive")
        else:
            return HttpResponse("Nom d'utilisateur ou mot de passe incorrect")
    else:
        return render(request, 'utilisateurs/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
