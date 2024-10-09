from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



from Job_Portal_App.models import User_Model



@login_required
def homePage(req):

    return render(req, 'common/index.html')

def registerPage(req):

    if req.method == 'POST':
        user_name = req.POST.get('username')
        firstName = req.POST.get('firstName')
        lastName = req.POST.get('lastName')
        email = req.POST.get('email')
        userType = req.POST.get('userType')
        password = req.POST.get('password')
        confirmPassword = req.POST.get('confirmPassword')

        if all([user_name, firstName, lastName, email, userType, password, confirmPassword]):
    
            if password == confirmPassword:
                user = User_Model.objects.create_user(
                    username = user_name,
                    first_name = firstName,
                    last_name = lastName,
                    user_type = userType,
                    password = confirmPassword
                )
                messages.success(req, 'Registration Successful!')
                return redirect('loginPage')
            else:
                messages.warning(req, 'Password not matched!')
                return render(req,'common/registration.html')


        else:
            messages.warning(req, 'All fields are required!')
            return render(req,'common/registration.html')


    return render(req,'common/registration.html')

def loginPage(req):

    if req.method == 'POST':

        user_name = req.POST.get('username')
        password = req.POST.get('password')
        
        if all([user_name, password]):
            
            user = authenticate(username = user_name, password = password)

            if user is not None:
                login(req, user)
                messages.success(req,'Login Successful!')
                return redirect('homePage')
            else:
                messages.warning(req, 'Username or password is incorrect!')
                return redirect('loginPage')
        else:
            messages.warning(req, 'All fields are required!')
            return redirect('loginPage')


    return render(req,'common/login.html')

def logoutPage(req):

    logout(req)
    
    return redirect('loginPage')