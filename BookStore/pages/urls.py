from django.urls import path
from pages.views import Homeview, AboutPageView

urlpatterns = [
    path('', Homeview.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),

]
