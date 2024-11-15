# myapp/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Main page
    path('signup/', views.signup, name='signup'),  # Signup page
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Login page
    path('logout/', views.custom_logout, name='logout'),  # Logout redirects to LOGOUT_REDIRECT_URL
    path("support/", views.support, name="support"),
]
