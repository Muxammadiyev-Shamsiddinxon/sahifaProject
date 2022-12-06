from django.urls import path
from .views import HomePageView, AboutPageView, SozlamalarPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('sozlamalar/', SozlamalarPageView.as_view(), name='sozlamalar'),
]
