from django.shortcuts import render,redirect
from django.http import HttpResponse
from website.models import Contact
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout

# Create your views here.


def Home(request):
        return render(request, 'index.html')

def contact(request):
        return render(request, 'contact-us.html')

def features(request):
        return render(request, 'features.html')

def services(request):
        return render(request, 'services.html')

def vehicles(request):
        return render(request, 'vehicles.html')

def contactdetails(request):
        if request.method == "POST":
            name_1 = request.POST.get("name")
            email_1 = request.POST.get("email")
            subject_1 = request.POST.get("subject")
            text_1 = request.POST.get("para")
            print(email_1, name_1, subject_1, text_1)
        ins1 = Contact(name_1=name_1, email=email_1, subject=subject_1, textarea=text_1)
        ins1.save()


        return HttpResponse("done")


def signup(request):
    return render(request, 'signup.html')

def handelsignup(request):
    if request.method == 'POST':
        username = request.POST['fullname']
        dob = request.POST['dob']
        email = request.POST['email']
        mobile_no = request.POST['mobile_no']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # Check for errorneous inputs
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('/home/')
        if pass1 != pass2:
            messages.error(request, "Passwords do not match to the confirm password")
            return redirect('/home/')

        # create user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.date_of_bearth = dob
        myuser.mobile_number = mobile_no
        myuser.pass_2 = pass2
        myuser.save()
        messages.success(request, "Your account has been successfully create")
        return redirect('/home/')

    else:
        return HttpResponse("404 not found")


def handel_login(request):
    if request.method == 'POST':
        login_username = request.POST['login_username']
        login_password = request.POST['login_password']
        user =authenticate(username=login_username,password=login_password)
        if user is not None:
             login(request,user)
             messages.success(request,"succesfully logged in")
             return redirect("/home/")
        else:
            messages.error(request,"wrong username or password")
            return redirect("/home/")