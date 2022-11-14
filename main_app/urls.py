from . import views
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('cars/', views.cars_index, name='cars_index'),
  path('cars/<int:car_id>/', views.cars_detail, name='cars_detail'),
  path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
  path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
  path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),
  path('cars/<int:car_id>/add_maintenance/', views.add_maintenance, name='add_maintenance'),
  path('tires/create/', views.TiresCreate.as_view(), name='tires_create'),
  path('tires/<int:pk>/', views.TireDetail.as_view(), name='tires_detail'),
  path('tires/', views.TireList.as_view(), name='tires_index'),
  path('tires/<int:pk>/update/', views.TireUpdate.as_view(), name='tires_update'),
  path('tires/<int:pk>/delete/', views.TireDelete.as_view(), name='tires_delete'),
  path('cars/<int:car_id>/assoc_tire/<int:tire_id>/', views.assoc_tire, name='assoc_tire'),
  path('admin/', admin.site.urls),
  path('accounts/', include('django.contrib.auth.urls')),
  path('accounts/signup/', views.signup, name='signup'),
]
