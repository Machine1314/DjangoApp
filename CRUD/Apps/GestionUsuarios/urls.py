from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('home/', views.home, name='home'),
    path('callSP/', views.callSP, name='callSP'),
    path('metrica/<int:proyecto_id>', views.metrica, name='metrica'),
    path('historias/<int:proyecto_id>', views.historias, name='historias'),
    path('addHistoria/<int:proy>', views.addHistoria, name='addHistoria'),
    path('updateHistoria/<int:id>/', views.updateHistoria, name='updateHistoria'),
    path('addTarea/<int:hist>', views.addTarea, name='addTarea'),
    path('updateTarea/<int:hist>/', views.updateTarea, name='updateTarea'),
    path('addBug/<int:hist>', views.addBug, name='addBug'),
    path('updateBug/<int:id>/', views.updateBug, name='updateBug'),
    path('addMember/', views.addMember, name='addMember'),
    path('delete/<int:usuario_id>/', views.delete, name='delete'),
    path('addProject/', views.addProject, name='addProject'),
    path('updateProject/<int:proyecto_id>', views.updateProject, name='updateProject'),
    path('update/<int:usuario_id>/', views.update, name='update'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]


