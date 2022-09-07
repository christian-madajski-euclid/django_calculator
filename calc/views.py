from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from login.models import Login
from django.shortcuts import redirect
from django.contrib import messages

@csrf_exempt
def calc(request):
    if request.session.get('logged_in'):
        if request.method == 'GET':
            return render(request=request, template_name='calc.html', context=None)
        elif request.method == 'POST':
            if request.POST.get('a') and request.POST.get('b'):
                if request.POST.get('operation') == '+':
                    return redirect(f'/calc/add/?a={request.POST.get("a")}&b={request.POST.get("b")}')
                elif request.POST.get('operation') == "-":
                    return redirect(f'/calc/sub/?a={request.POST.get("a")}&b={request.POST.get("b")}')
                if request.POST.get('operation') == '*':
                    return redirect(f'/calc/mul/?a={request.POST.get("a")}&b={request.POST.get("b")}')
                if request.POST.get('operation') == '/':
                    return redirect(f'/calc/div/?a={request.POST.get("a")}&b={request.POST.get("b")}')
                if request.POST.get('operation') == '**':
                    return redirect(f'/calc/exp/?a={request.POST.get("a")}&b={request.POST.get("b")}')
                else:
                    messages.add_message(request, messages.ERROR, "Operation not supported by calculator!")
                    return redirect('/calc/')
            else:
                messages.error(request, "ERROR: Two numbers required to perform calculations!")
                return redirect('/calc/')
        else:
            messages.add_message(request, messages.ERROR, "Request type not supported (only GET and POST)!")
            return redirect('/calc/')
    else:
        messages.add_message(request, messages.ERROR, "Must be logged in to use calculator!")
        return redirect('/')
    
def add(request):
    if request.session.get('logged_in'):
        if request.method == 'GET':
            try:
                a_float, b_float = float(request.GET.get('a')), float(request.GET.get('b'))
            except ValueError:
                messages.error(request, "ERROR: Calculator requires int and float values only!")
                return redirect('/calc/')
            else:
                try:
                    c = a_float + b_float
                except OverflowError:
                    messages.error(request, "ERROR: Result too large for Python to handle!")
                    return redirect('/calc/')
                else:
                    output_data = {'a': str(a_float), 'b': str(b_float), 'operator': '+', 'result': str(c)}
                    
                    return render(request=request, template_name='calc.html', context=output_data)
        else:
            return redirect('/calc/')
    else:
        messages.error(request, "ERROR: Must be logged in to use calculator!")
        return redirect('/')

def sub(request):
    if request.session.get('logged_in'):
        if request.method == 'GET':
            try:
                a_float, b_float = float(request.GET.get('a')), float(request.GET.get('b'))
            except ValueError:
                messages.error(request, "ERROR: Calculator requires int and float values only!")
                return redirect('/calc/')
            else:
                try:
                    c = a_float - b_float
                except OverflowError:
                    messages.error(request, "ERROR: Result too large for Python to handle!")
                    return redirect('/calc/')
                else:
                    output_data = {'a': str(a_float), 'b': str(b_float), 'operator': '-', 'result': str(c)}
                    return render(request=request, template_name='calc.html', context=output_data)
        else:
            return redirect('/calc/')
    else:
        messages.error(request, "ERROR: Must be logged in to use calculator!")
        return redirect('/')

def mul(request):
    if request.session.get('logged_in'):
        if request.method == 'GET':
            try:
                a_float, b_float = float(request.GET.get('a')), float(request.GET.get('b'))
            except ValueError:
                messages.error(request, "ERROR: Calculator requires int and float values only!")
                return redirect('/calc/')
            else:
                try:
                    c = a_float * b_float
                except OverflowError:
                    messages.error(request, "ERROR: Result too large for Python to handle!")
                    return redirect('/calc/')
                else:
                    output_data = {'a': str(a_float), 'b': str(b_float), 'operator': '*', 'result': str(c)}
                    return render(request=request, template_name='calc.html', context=output_data)
        else:
            return redirect('/calc/')
    else:
        messages.error(request, "ERROR: Must be logged in to use calculator!")
        return redirect('/')

def div(request):
    if request.session.get('logged_in'):
        if request.method == 'GET':
            try:
                a_float, b_float = float(request.GET.get('a')), float(request.GET.get('b'))
            except ValueError:
                messages.error(request, "ERROR: Calculator requires int and float values only!")
                return redirect('/calc/')
            else:
                # additional check to avoid ZeroDivisionError
                if b_float == 0.0:
                    messages.error(request, "ERROR: Cannot divide by zero!")
                    return redirect('/calc/')
                else:
                    try:
                        c = a_float / b_float
                    except OverflowError:
                        messages.error(request, "ERROR: Result too large for Python to handle!")
                        return redirect('/calc/')
                    else:
                        output_data = {'a': str(a_float), 'b': str(b_float), 'operator': '/', 'result': str(c)}
                        return render(request=request, template_name='calc.html', context=output_data)
        else:
            return redirect('/calc/')
    else:
        messages.error(request, "ERROR: Must be logged in to use calculator!")
        return redirect('/')

def exp(request):
    if request.session.get('logged_in'):
        if request.method == 'GET':
            try:
                a_float, b_float = float(request.GET.get('a')), float(request.GET.get('b'))
            except ValueError:
                messages.error(request, "ERROR: Calculator requires int and float values only!")
                return redirect('/calc/')
            else:
                try:
                    c = a_float ** b_float
                except OverflowError:
                    messages.error(request, "ERROR: Result too large for Python to handle!")
                    return redirect('/calc/')
                else:
                    output_data = {'a': str(a_float), 'b': str(b_float), 'operator': '**', 'result': str(c)}
                    return render(request=request, template_name='calc.html', context=output_data)
        else:
            return redirect('/calc/')
    else:
        messages.error(request, "ERROR: Must be logged in to use calculator!")
        return redirect('/')