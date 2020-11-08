from django.urls import path, include
# from django.contrib.auth import views #login, logout
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

urlpatterns = [
    # path('login', 'django.contrib.auth.views.LoginView', {'template_name':'accounts/login.html'}, name = 'login'),
    path('/login/', LoginView.as_view(), name='login'),
    path('/register/', LoginView.as_view(), name='register')
]
