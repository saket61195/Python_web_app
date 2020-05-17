from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"invalid details")
            return redirect('login')
    else:
        return render(request,'login.html')

    

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        psw = request.POST['psw']
        psw_repeat = request.POST['psw_repeat']

        if psw == psw_repeat:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    first_name= first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=psw
                    )
                user.save()
                print("user created")
        else:
            messages.info(request,'password not match')
            print('Password is not matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')



def logout(request):
    auth.logout(request)
    return redirect("/")
