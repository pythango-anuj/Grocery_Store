from django.shortcuts import render,redirect,HttpResponse
from .models import custom_user_model
from .forms import RegistrationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request,*args,**kwargs):
    return render(request,'account/home.html')

def register_view(request,*args,**kwargs):
    logout(request)
    if request.method == 'POST':
        print(request.POST)
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')
        else:
            return HttpResponse('<h1>Invalid Credential !! or Password is too Weak!!</h1>')
    else:
        form = RegistrationForm()
        args = {'form':form}
        return render(request,'account/register.html',args)

def login_view(request,*args,**kwargs):
    logout(request)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('Index')
        else:
            return HttpResponse('<h1>User Does not Exist</h1>')
    return render(request,'account/login.html')

def logout_view(request,*args,**kwargs):
    logout(request)
    return redirect('Home')
