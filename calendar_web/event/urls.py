from django.urls import path

from event.views import MainPage

urlpatterns = [
        path('', MainPage.as_view(), name='the-main-page'),

]