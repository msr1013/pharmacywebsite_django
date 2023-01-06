from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/authentication/login')
def medicine_index(request):
    return render(request, 'medicines/index.html')
