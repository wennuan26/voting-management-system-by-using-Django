from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import PeopleRegistrationForm
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'pages/index.html')
class PeopleLoginView(LoginView):
    template_name = 'people_login.html'

people_login = PeopleLoginView.as_view()

def register_people(request):
    if request.method == 'POST':
        form = PeopleRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('/')
    else:
        form = PeopleRegistrationForm()
    return render(request, 'people_register.html', {'form': form})