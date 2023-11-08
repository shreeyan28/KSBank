from django.urls import path
from django.contrib.auth import views as auth_views  # Import Django's built-in auth views

from appointments import views

urlpatterns = [
    # Other URL patterns
    path('appointments/', views.appointment, name='appointments'),
    path('create_account/', views.create_account, name='create_account'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('login_success.html/', views.create_account, name='login_success.html'),  # Use Django's LoginView
]
