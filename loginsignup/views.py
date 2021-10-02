from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def login_page(request):
    return render(request,'login.html')
    
def signup_page(request):
    return render(request,'signup.html')

def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        username = request.POST['username']
        gmail = request.POST['gmail']
        password = request.POST['password']

        if User.objects.filter(email = gmail).exists():
            messages.error(request, "Sorry E-mail is taken")
            return redirect('/signup_page/')

        elif User.objects.filter(username = username).exists():
            messages.error(request, "Sorry Username is taken")
            return redirect('/signup_page/')
        else:
            user = User.objects.create_user(first_name = name ,email = gmail ,username = username ,password= password)
            user.save()
            messages.info(request,"Account Created Successfully")
            return redirect('/login_page/')

    else:
        return render(request,'signup.html')
    
def login(request):
    if request.method == 'POST':
        login_username = request.POST['usernameL']
        login_password = request.POST['passwordL']
        user = auth.authenticate(username = login_username,password = login_password)

        if user is not None:
            auth.login(request,user)
            messages.info(request,'You Logged IN')
            return redirect('/')
        else:
            messages.error(request,'Invalid Credentails')
            return redirect('/login_page/')
    else:
        return redirect('/login_page/')

def logout(request):
    auth.logout(request)
    messages.info(request,"You Logged Out")
    return redirect('/')

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return redirect('/login_page/')
