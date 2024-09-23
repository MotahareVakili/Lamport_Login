from django.urls import path
from .views import login_view, signup_view, change_pass_view, home_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('change/', change_pass_view, name='change'),
    path('home/', home_view, name='home'),

]
