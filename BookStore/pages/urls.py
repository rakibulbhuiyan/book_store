from django.urls import path
from pages.views import Homeview

urlpatterns = [
    path('', Homeview.as_view(), name='home'),

]
