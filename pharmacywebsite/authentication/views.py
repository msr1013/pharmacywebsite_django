from django.shortcuts import reverse, redirect, render
from django.views import View
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.


class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')

    def post(self, request):
        req_username = request.POST.get('username')
        req_password = request.POST.get('password')

        if req_username and req_password:
            user = auth.authenticate(
                username=req_username, password=req_password)
            auth.login(request, user)
            return redirect('medicines')
        return redirect("login")


# class LoginView(View):
#     def get(self, request):
#         form = AuthenticationForm()
#         return render(request, 'authentication/login.html', {'form': form})

#     def post(self, request):
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             auth.login(request, form.get_user())
#             return redirect(request, 'medicines/index.html')
#         return redirect("login")


class RegisterView(View):
    def get(self, request):
        # return HttpResponse("Hello Workd")
        return render(request, 'authentication/register.html')

    def post(self, request):
        req_email = request.POST.get('email')
        req_password = request.POST.get('password')
        req_username = request.POST.get('username')

        if not req_username:
            messages.error(request, 'Username field is required')
            return redirect('register')

        user = User.objects.filter(username=req_username).exists()
        if not user:
            user = User.objects.filter(email=req_email)
            if not user:
                user = User.objects.create_user(
                    email=req_email, username=req_username)
                user.set_password(req_password)
                user.is_active = False
                user.save()

                send_mail(
                    'Account Creation',  # Subject
                    'Congratulations! Your account has been created successfully.',  # message body
                    'imsr1013@gmail.com',  # sender
                    [user.email]  # receiver
                )
                return render(request, 'authentication/register.html')
            messages.error(request, 'Email already taken, try another')
            return render(request, 'authentication/register.html')
        messages.error(request, 'Username already taken, try another')
        return render(request, 'authentication/register.html')
