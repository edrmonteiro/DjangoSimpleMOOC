from django.urls import path, include
from datetime import datetime
# from django.contrib.auth import views #login, logout
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from simplemooc.accounts import forms, views
from simplemooc.accounts.views import register, dashboard, edit, edit_password

urlpatterns = [
     path('/login/',
         LoginView.as_view
         (
             template_name='accounts/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('/register/', register, name='register'),
    path('/edit/', edit, name='edit'),
    path('/edit_password/', edit_password, name='edit_password'),
    path('/logout/', LogoutView.as_view(), name='logout')
]
