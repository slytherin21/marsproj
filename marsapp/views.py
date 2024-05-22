from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Trainer
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
import sqlite3
from django.contrib.auth.models import User
from .models import customuser
from marsapp.models import customuser
from django.urls import reverse
from django.contrib import  messages, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from django.http import HttpResponseNotFound
from .models import Profile

# Create your views here.

def index(request):

    trainers = Trainer.objects.all()
    return render(request, 'index.html', {'trainers':trainers})

def team(request):
    return render(request, 'team.html')

def signup(request):
    try:
        if request.method == "POST":
            firstname = request.POST.get('first_name')
            lastname = request.POST.get('last_name')
            email = request.POST.get('email')
            age = request.POST.get('age')
            height = request.POST.get('height')
            weight = request.POST.get('weight')
            password = request.POST.get('password')
            cnfpassword = request.POST.get('cnfpassword')
            print(firstname,lastname,email,age,password,height,weight,password,cnfpassword)
            # Create a new user object
            if password == cnfpassword:
                if customuser.objects.filter(email=email).exists():
                    print("email already used")
                    messages.info(request,'Email already used')
                    return redirect('signup')
                else:
                    user = customuser.objects.create_user(age=age,
                                                        height=height,weight=weight,
                                                        first_name=firstname, last_name=lastname, 
                                                        email=email, password=password, username=email)
                    user.save()
                    Profile.objects.create(user=user)
                    print('user created')
                    return redirect('login')
            else:
                print("password not matching ")  
                return redirect(reverse('index'))
    except Exception as e:
        print("An error occurred:", e)
    return render(request, 'signup.html')

def login(request):
    try:
        print('intry')
        if request.method == "POST":
            print('inpost')
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = auth.authenticate(username=email,password=password)

            if user is not None:
                print("loggedin")
                auth.login(request, user)
                return redirect('index')
            else:
                print("invalid credential")
                messages.info(request,'invalid credential')
                return redirect('login')
        else:
            print('moyemoye')
            return render(request, 'login.html')
    except Exception as e:
        print("An error occurred:", e)
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def profile(request):
    profile = request.user.profile
    if request.method == "POST":
        form = ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
        
    else:
        form = ProfileForm(instance=profile)
    print("Hello",form)
    return render(request, 'profile.html', {'form': form, 'profile':profile})

    
    #return render(request, 'profile.html', {'form': form, 'profile': profile})
def bmi(request):
    bmi=''
    try:
        if request.method=="POST":
            height = eval(request.POST.get('height'))
            height= height/100 # changed cm to m
            weight = eval(request.POST.get('weight'))
            age = request.POST.get('age')
            bmi = round(weight/(height*height),2)

            with sqlite3.connect('db.sqlite3') as conn:
                cur = conn.cursor()
                cur.execute('CREATE TABLE IF NOT EXISTS bmi (height INTEGER, weight INTEGER, age INTEGER, bmi INTEGER) ')
                cur.execute('''insert into bmi (height, weight, age, bmi ) Values (?,?,?,?)''', (height,weight,age,bmi))
                conn.commit()


        
    except Exception as e:
        bmi="invalid input"
    print(bmi)

    return render(request, 'bmi-calculator.html', {'bmi':bmi} )

def about(request):
    trainers = Trainer.objects.all()
    return render(request, 'about-us.html', {'trainers':trainers})

def classdetail(request):
    return render(request,'class-details.html')

def services(request):
    return render(request,'services.html')

def classtimetable(request):
    return render(request,'class-timetable.html')

def gallery(request):
    return render(request,'gallery.html')

def contact(request):
    return render(request,'contact.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def blogdetails(request):
    return render(request, 'blog-details.html')

def login_view(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Log in the user
            return redirect('home')  # Redirect to the home page after login
    else:
        form = AuthenticationForm()
    return render(request, 'login_popup.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Create the user account
            return redirect('home')  # Redirect to the home page after signup
    else:
        form = UserCreationForm()
    return render(request, 'signup_popup.html', {'form': form})

def profilenew(request):
    return render(request, 'profilenew.html')