from django.urls import path
from django.contrib.auth import views as auth_views
from usuarios import views as usuarios_views

urlpatterns = [
    path('registrar/', usuarios_views.registrar, name='registrar'),
    path('perfil/', usuarios_views.perfil, name='perfil'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

]