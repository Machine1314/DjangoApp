from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('home/', views.home, name='home'),
    path('teams/', views.teams, name='teams'),
    path('tables/', views.tables, name='tables'),
    path('callSP/', views.callSP, name='callSP'),
    path('metrica/<int:proyecto_id>', views.metrica, name='metrica'),
    path('historias/<int:proyecto_id>', views.historias, name='historias'),
    path('addHistoria/<int:proy>', views.addHistoria, name='addHistoria'),
    path('updateHistoria/<int:id>/', views.updateHistoria, name='updateHistoria'),
    path('addTarea/<int:hist>', views.addTarea, name='addTarea'),
    path('updateTarea/<int:id>/', views.updateTarea, name='updateTarea'),
    path('addBug/<int:hist>', views.addBug, name='addBug'),
    path('updateBug/<int:id>/', views.updateBug, name='updateBug'),
    path('addMember/', views.addMember, name='addMember'),
    path('updateMember/<int:member_id>', views.updateMember, name='updateMember'),
    path('deleteMember/<int:member_id>', views.deleteMember, name='deleteMember'),
    path('delete/<int:usuario_id>/', views.delete, name='delete'),
    path('addProject/', views.addProject, name='addProject'),
    path('updateProject/<int:proyecto_id>', views.updateProject, name='updateProject'),
    path('addTeam/', views.addTeam, name='addTeam'),
    path('updateTeam/<int:id>', views.updateTeam, name='updateTeam'),
    path('deleteTeam/<int:id>', views.deleteTeam, name='deleteTeam'),
    path('addRol/', views.addRol, name='addRol'),
    path('updateRol/<int:id>/', views.updateRol, name='updateRol'),
    path('deleteRol/<int:id>/', views.deleteRol, name='deleteRol'),
    path('addStatus/', views.addStatus, name='addStatus'),
    path('updateStatus/<int:id>/', views.updateStatus, name='updateStatus'),
    path('deleteStatus/<int:id>/', views.deleteStatus, name='deleteStatus'),
    path('update/<int:usuario_id>/', views.update, name='update'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]


