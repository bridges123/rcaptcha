from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name="main"),
    path('log-in', log_in, name='log-in'),
    path('login', LoginView.as_view(), name="login"),
    path('getdata', getdata, name="getdata"),
    path('register', RegisterView.as_view(), name="register"),
    path('logout', LogoutView.as_view(next_page='/'), name='logout'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('tops', tops, name='tops'),
    path('tops/record', tops_record, name='tops_record'),
    path('tops/record-delay', tops_record_delay, name='tops_record_delay'),
    path('tops/average', tops_average, name='tops_average'),
    path('tops/count', tops_count, name='tops_count')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
