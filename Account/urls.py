from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='Home'),
    path('register/',views.register_view,name='Register'),
    path('login/',views.login_view,name='Login'),
    path('logout/',views.logout_view,name='Logout')
]