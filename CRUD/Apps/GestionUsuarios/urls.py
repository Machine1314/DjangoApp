from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('delete/<int:usuario_id>/', views.delete, name='delete'),
    path('update/<int:usuario_id>/', views.update, name='update'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
