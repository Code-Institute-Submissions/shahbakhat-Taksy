from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core import views

from core.passenger import  views as passenger_views
from core.driver import  views as driver_views



passenger_urlpatterns = [
    path('',passenger_views.home, name="home")
]

driver_urlpatterns = [
    path('',driver_views.home, name="home")
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),

    path('login/',auth_views.LoginView.as_view(template_name="login.html")),
    path('logout/',auth_views.LogoutView.as_view(next_page="/")),
    path('sign-up/',views.sign_up),

    path('passenger/',include((passenger_urlpatterns, 'passenger'))),
    path('driver/',include((driver_urlpatterns, 'driver'))),

]
