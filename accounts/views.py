from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email taken")
                return redirect('register')
            else:
                user=User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password1, email=email)
                user.save()
                auth.login(request, user)
                return redirect('/')
        else:
            messages.info(request, "password is not matching")
            return redirect('register')
    else:
        return render(request, 'register.html')




def login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user= auth.authenticate(username=username, password= password)

        if user is not None:
            auth.login(request, user)
            return redirect('/',{'name': username})
        else:
            messages.info(request, "Username or Password is incorrect")
            return redirect('login')

    else:
        return render(request, 'login.html')



def logout(req):
    auth.logout(req)
    return redirect('/')



def change(req):

    if req.method == 'POST':
        username = req.POST['username']
        email = req.POST['email']
        password1 = req.POST['password1']
        password2 = req.POST['password2']


        if password1 == password2:

            user=User.objects.create_user(username=username,email=email, password=password1)
            user.save()
            return redirect('login')
        else:
            messages.info(req, "password is not matching")
            return redirect('change')




    else:
        return render(req, 'change.html')
