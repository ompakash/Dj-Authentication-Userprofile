from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('login_page/',views.login_page),
    path('signup_page/',views.signup_page),
    path('signup/',views.signup),
    path('login/',views.login),
    path('logout/',views.logout ),
    path('profile/',views.profile ),
]
