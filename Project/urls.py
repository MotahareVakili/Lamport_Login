from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

import Lamport

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Lamport/', include('Lamport.urls')),
    path('', RedirectView.as_view(url='Lamport/login/', permanent=False)),
    path('', RedirectView.as_view(url='Lamport/login/', permanent=False)),

]
