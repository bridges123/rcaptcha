from django.shortcuts import render
from django.views.generic import View
from .forms import LoginForm, RegisterForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView
from rcaptcha.settings import CLIENT_ID, SECRET_CODE
from .models import *

import requests


def getdata(request):
    if request.is_ajax():
        if request.method == 'POST':
            result = float(request.POST.get('result'))
            cur_user = Customer.objects.get(user=request.user)
            cur_record = cur_user.record
            cur_record_delay = cur_user.record_delay
            if cur_user.delay :
                if result < cur_record_delay or cur_record_delay == 0:
                    cur_user.record_delay = round(result, 3)
            else:
                if result < cur_record or cur_record == 0:
                    cur_user.record = round(result, 3)
            cur_user.all_time += result
            cur_user.count += 1
            cur_user.avg = round(cur_user.all_time / cur_user.count, 3)
            cur_user.save()
            return HttpResponse('ok')


def index(request):
    customer = {}
    if request.user.is_authenticated:
        if request.method == 'GET':
            customer = {
                'customer': Customer.objects.get(user=request.user)
            }
    return render(request, 'main/index.html', customer)


def log_in(request):
    # return HttpResponseRedirect('https://oauth.vk.com/authorize?client_id=' + CLIENT_ID + '&display=page&redirect_uri=http://rodinacaptcha.xyz/profile&scope=offline&response_type=code&v=5.52')
    req = requests.get()


def tops(request):
    return HttpResponseRedirect('tops/record')


def tops_record(request):
    customers = {}
    if request.user.is_authenticated:
        if request.method == 'GET':
            getedited = []
            geted = Customer.objects.order_by('record')
            cnt = 1
            for get in geted:
                if cnt <= 10:
                    if get.record != 0.0:
                        getedited.append({'user': get, 'num': cnt})
                        cnt += 1
                else:
                    break
            if cnt <= 10:
                for get in geted:
                    if cnt <= 10:
                        if get.record == 0.0:
                            getedited.append({'user': get, 'num': cnt})
                            cnt += 1
                    else:
                        break
            customers = {
                'customers': getedited
            }
    return render(request, 'main/tops.html', customers)


def tops_record_delay(request):
    customers = {}
    if request.user.is_authenticated:
        if request.method == 'GET':
            getedited = []
            geted = Customer.objects.order_by('record_delay')
            cnt = 1
            for get in geted:
                if cnt < 10:
                    if get.record_delay != 0.0:
                        getedited.append({'user': get, 'num': cnt})
                        cnt += 1
                else:
                    break
            if cnt <= 10:
                for get in geted:
                    if cnt <= 10:
                        if get.record_delay == 0.0:
                            getedited.append({'user': get, 'num': cnt})
                            cnt += 1
                    else:
                        break
            customers = {
                'customers': getedited
            }
    return render(request, 'main/tops.html', customers)


def tops_average(request):
    customers = {}
    if request.user.is_authenticated:
        if request.method == 'GET':
            getedited = []
            geted = Customer.objects.order_by('avg')
            cnt = 1
            for get in geted:
                if cnt < 10:
                    if get.avg != 0.0:
                        getedited.append({'user': get, 'num': cnt})
                        cnt += 1
                else:
                    break
            if cnt <= 10:
                for get in geted:
                    if cnt <= 10:
                        if get.avg == 0.0:
                            getedited.append({'user': get, 'num': cnt})
                            cnt += 1
                    else:
                        break
            customers = {
                'customers': getedited
            }
    return render(request, 'main/tops.html', customers)


def tops_count(request):
    customers = {}
    if request.user.is_authenticated:
        if request.method == 'GET':
            getedited = []
            geted = Customer.objects.order_by('-count')
            cnt = 1
            for get in geted:
                if cnt < 10:
                    if get.count != 0.0:
                        getedited.append({'user': get, 'num': cnt})
                        cnt += 1
                else:
                    break
            if cnt <= 10:
                for get in geted:
                    if cnt <= 10:
                        if get.count == 0.0:
                            getedited.append({'user': get, 'num': cnt})
                            cnt += 1
                    else:
                        break
            customers = {
                'customers': getedited
            }
    return render(request, 'main/tops.html', customers)


class LoginView(View):

    def get(self, req, *args, **kwargs):
        form = LoginForm(req.POST or None)
        context = {
            'form': form
        }
        return render(req, 'main/profile.html', context)

    def post(self, req, *args, **kwargs):
        form = LoginForm(req.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(req, user)
                return HttpResponseRedirect('/')
        return render(req, 'main/profile.html', {'form': form})


class RegisterView(View):

    def get(self, req, *args, **kwargs):
        form = RegisterForm(req.POST or None)
        context = {
            'form': form
        }
        return render(req, 'main/register.html', context)

    def post(self, req, *args, **kwargs):
        form = RegisterForm(req.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            new_user = form.save(commit=False)
            new_user.username = username
            new_user.save()
            new_user.set_password(password)
            new_user.save()

            Customer.objects.create(
                user=new_user,
                record=0,
                count=0,
                all_time=0
            )

            user = authenticate(username=username, password=password)
            login(req, user)
            return HttpResponseRedirect('/')
        context = {'form': form}
        return render(req, 'main/register.html', context)


class ProfileView(View):

    def get(self, request, *args, **kwargs):
        customer = Customer.objects.get(user=request.user)
        if customer.count != 0:
            customer.avg = round(customer.all_time / customer.count, 3)
            customer.save()
        return render(request, 'main/profile.html', {'customer': customer})

    def post(self, request, *args, **kwargs):
        customer = Customer.objects.get(user=request.user)
        customer.delay = request.POST.get('delay')
        customer.capKey = request.POST.get('capKey')
        customer.save()
        return HttpResponseRedirect('/profile')
