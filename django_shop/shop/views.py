from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User


def main_page(request):
    return render(request, 'shop/main_page.html')


def registration(request):
    if request.method == 'GET':
        return render(request, 'registration/registration.html')
    user = User.objects.create_user(username, email, password)
    user.save()
    return render(request, 'registration/registration.html')
