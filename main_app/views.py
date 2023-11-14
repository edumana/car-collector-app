from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Car, Tires
from .forms import MaintenanceForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Add the following import
from django.http import HttpResponse

# Define the home view
class Home(LoginView):
  template_name = 'home.html'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# Add new view
@login_required
def cars_index(request):
  cars = Car.objects.filter(user=request.user)
  return render(request, 'cars/index.html', { 'cars': cars })

@login_required
def cars_detail(request, car_id):
  car = Car.objects.get(id=car_id)
  tires_car_doesnt_have = Tires.objects.exclude(id__in = car.tires.all().values_list('id'))
  maintenance_form = MaintenanceForm()
  return render(request, 'cars/detail.html', {
    'car': car, 'maintenance_form': maintenance_form, 'tires': tires_car_doesnt_have
  })

@login_required
def add_maintenance(request, car_id):
  # create a ModelForm instance using the data in request.POST
  form = MaintenanceForm(request.POST)
  # validate the form
  if form.is_valid():
    new_maintenance = form.save(commit=False)
    new_maintenance.car_id = car_id
    new_maintenance.save()
  return redirect('cars_detail', car_id=car_id)

class CarUpdate(LoginRequiredMixin,UpdateView):
  model = Car
  fields = ['make', 'description', 'year']

class CarDelete(LoginRequiredMixin,DeleteView):
  model = Car
  success_url = '/cars/'

class CarCreate(LoginRequiredMixin,CreateView):
  model = Car
  fields = ['name', 'make', 'description', 'year']
  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

class TiresCreate(LoginRequiredMixin,CreateView):
  model = Tires
  fields = '__all__'

class TireList(LoginRequiredMixin,ListView):
  model = Tires

class TireDetail(LoginRequiredMixin,DetailView):
  model = Tires

class TireUpdate(LoginRequiredMixin,UpdateView):
  model = Tires
  fields = ['name', 'hardness']

class TireDelete(LoginRequiredMixin,DeleteView):
  model = Tires
  success_url = '/tires/'

@login_required
def assoc_tire(request, car_id, tire_id):
  Car.objects.get(id=car_id).tires.add(tire_id)
  return redirect('cars_detail', car_id=car_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('cars_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
