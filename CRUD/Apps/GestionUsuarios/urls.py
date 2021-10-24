from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('home/', views.home, name='home'),
    path('historias/<int:proyecto_id>', views.historias, name='historias'),
    path('addHistoria/', views.addHistoria, name='addHistoria'),
    path('updateHistoria/<int:id>/', views.updateHistoria, name='updateHistoria'),
    path('addMember/', views.addMember, name='addMember'),
    path('delete/<int:usuario_id>/', views.delete, name='delete'),
    path('addProject/', views.addProject, name='addProject'),
    path('update/<int:usuario_id>/', views.update, name='update'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]


