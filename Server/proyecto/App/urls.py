from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),  
    path('registro',views.registro,name='registro'), 
    path('login',views.login,name='login'), 
    path('login_view', views.login_view, name="login_view"),
    path('logout',views.logout,name='logout'),
    path('enviar-usuario/', views.enviar_nombre_usuario, name='enviar-usuario'), 
    path('create_user/', views.create_user, name='create_user'),
]