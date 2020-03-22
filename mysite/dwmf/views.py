from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Truck, User, Profile, Menu
from .forms import ExtendedUserCreationForm, ProfileForm, MenuForm


##########################New SignUp Form

#########################################
def home(request):
    return render(request, 'home.html')

##########################class views
class TruckCreate(LoginRequiredMixin, CreateView):
    model = Truck
    fields= ['name', 'style', ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TruckDetail(LoginRequiredMixin, DetailView):
    model = Truck


##########################view definitions here

def menu_create(request, truck_id):
    truck = Truck.objects.get(id=truck_id)
    menu_form = MenuForm()

    return render(request, 'dwmf/menu_form.html',{'truck':truck, 'menu_form': menu_form})

def menu_new(request, truck_id):
    truck = Truck.objects.get(id=truck_id)
    form = MenuForm(request.POST)

    if form.is_valid():
        new_menu = form.save(commit=False)
        new_menu.truck_id = truck.id
        new_menu.save()
    return redirect('truck_detail', pk=truck_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()
           
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('index')
        else:
            error_message = 'Invalid Signup - Please try again'
    form = ExtendedUserCreationForm()
    profile_form = ProfileForm()
    context = {'form': form, 'profile_form': profile_form,'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def profile(request):
    user = User
    return render(request, 'registration/profile.html', {'user': user})

def trucks_index(request):
    trucks = Truck.objects.all()
    return render(request, 'trucks/index.html', {'trucks': trucks })

def trucks_info(request, truck_id):
    truck = Truck.objects.get(id=truck_id)
    return render(request, 'trucks/index_detail.html', {'truck': truck})




