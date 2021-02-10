from django.urls import path

from event.views import MainPage, EventView

urlpatterns = [
        path('add_event', EventView.as_view(), name='add_event'),
        path('', MainPage.as_view(), name='the-main-page'),

]