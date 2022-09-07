from django.template import loader
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from login.models import Login
from django.shortcuts import redirect
from django.contrib import messages

def index(request):
    if request.session.get('logged_in'):
        return redirect('/calc/')
    else:
        return render(request=request, template_name="index.html", context=None)

@csrf_exempt
def check_login(request):
    if request.method == 'POST':
        form_email = request.POST.get("email")
        try:
            requested_user = Login.objects.get(email=form_email)
        except Login.DoesNotExist:
            messages.error(request, "ERROR: Email is not associated with an account. Click \"Register\" to sign up.")
            return redirect('/')
        else:
            form_pass = request.POST.get("password")
            if requested_user.password == form_pass:
                request.session['logged_in'] = True
                messages.success(request, f"SUCCESS: Logged in as {request.POST.get('email')}")
                return redirect('/calc/')
            else:
                messages.error(request, "ERROR: Password not valid for given email!")
                return redirect('/')

def register(request):
    return render(request=request, template_name="register.html", context=None)

@csrf_exempt
def check_register(request):
    # check if email field is empty
    if not request.POST.get('email'):
        messages.error(request, "ERROR: No email was given!")
        return redirect('/register/')
    elif not request.POST.get('password'):
        messages.error(request, 'ERROR: No password was given!')
        return redirect('/register/')
    else:
        # check if email is already in use
        try:
            check_email = Login.objects.get(email=request.POST.get('email'))
            messages.error(request, "ERROR: Cannot create new account. Email already exists in database!")
        except Login.DoesNotExist:
            new_user = Login(email=request.POST.get('email'), password=request.POST.get('password'))
            new_user.save()
            messages.success(request, f"SUCCESS: New user with email {request.POST.get('email')} has been created.")
            return redirect('/')
        else:
            return redirect('/register/')

def logout(request):
    request.session.flush()
    messages.success(request, "SUCCESS: Logged out of calculator")
    return redirect('/')