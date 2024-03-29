from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render

from users.models import CustomUser

# from users.forms import LoginForm, RegisterForm

# Create your views here.


def login_classic(request):
    content = {}
    return render(request, "main/authorization.html", content)


def logged_in_classic(request):
    return HttpResponse("you are logged in")


def logout_classic(request):
    return HttpResponse("you are logged out")


def register_classic(request):
    return HttpResponse("registration email sent")


def confirm_registration_classic(request):
    return HttpResponse("your user is ativated")


def password_recovery_classic(request):
    return HttpResponse("password link sent to your registration email")


def create_new_password_classic(request):
    return HttpResponse("your new password has been set")


# def login_classic(request):
# 	auth_error = None
# 	form = LoginForm()
# 	user = request.user
# 	if request.method == "POST":
# 		form = LoginForm(request.POST)
# 		if form.is_valid():
# 			auth_data = form.cleaned_data
# 			user = authenticate(
# 				request, email=auth_data["email"], password=auth_data["password"])
# 			if user:
# 				login(request, user)
# 				return redirect("main:profile")
# 			auth_error = "Данные для авторизации не верны."
# 	content = {
#             "user": user,
#             "title": "ОИП НАКС: Авторизация",
#             "form": form,
#         }
# 	if auth_error:
# 		content.update({"auth_error": auth_error})
# 	return render(request, 'main/authorization.html', content)


# def logged_in(request):
# 	content = {
# 		"user": request.user
# 	}
# 	return render(request, "main/profile.html", content)


# def logout_user(request):
# 	# return HttpResponse("Вы вышли")
# 	logout(request)
# 	return redirect("users:login")


# def register(request):
# 	auth_error = None
# 	form = RegisterForm()
# 	if request.method == "POST":
# 		form = RegisterForm(request.POST)
# 		if form.is_valid():
# 			data = form.cleaned_data
# 			p, p_con = data["password"], data["password_confirm"]
# 			if p == p_con:
# 				form.save()
# 				return redirect("main:profile")
# 			else:
# 				auth_error = "Пароли не совпадают."
# 	content = {
# 		"form": form,
# 		"auth_error": auth_error,
# 	}
# 	# import pdb; pdb.set_trace()

# 	return render(request, "main/register.html", content)
