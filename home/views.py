from django.shortcuts import render,redirect
from django.http import *
from chatDb.models import *
# Create your views here.

# redirecting to home page
def showHomePage(request) :
    return render(request, "home.html")

# checking if the user exists or not
def forgotPassword(request) :
    # checking if user exists or not
    if User.objects.filter(username=request.GET['username']).count() == 0:
        return redirect("/chatWebApp?fp=false")
    elif User.objects.filter(username=request.GET['username']).count() == 1:
        return redirect("/chatWebApp?fp=true")

# updating password in database
def changePassword(request):
    User.objects.filter(username=request.GET['username']).update(password=request.GET['password'])
    # password changed successfully
    return redirect("/chatWebApp?fp=changed")

# creating account in database
def createAccount(request) :
    # checking if user exists or not
    if User.objects.filter(username=request.GET['username']).count() == 0:
        User.objects.create(name=request.GET['name'],username=request.GET['username'],password=request.GET['password'])
        # account created successfully
        return redirect("/chatWebApp?accountCreated=true")
    else:
        # user already exists in database
        return redirect("/chatWebApp?accountCreated=false")

# validating the login credentials provided by the user
def validate(request) :
    # validation
    if(User.objects.filter(username=request.GET['username'],password=request.GET['password']).values("username").count()==1) :
        return redirect("/chatWebApp/dashboard?username="+request.GET['username']+"")
    elif User.objects.filter(username=request.GET['username']).values("username").count()==1:
        # password wrong but user exists
        return redirect("/chatWebApp?validate=p")
    else :
        # user does not exist or wrong username
        return redirect("/chatWebApp?validate=u")