from django.urls import path

from event.views import MainPage, EventView, delete_event

urlpatterns = [
        path('add_event', EventView.as_view(), name='add_event'),
        path('delete_event/<int:id>/', delete_event, name='delete_event'),
        path('', MainPage.as_view(), name='the-main-page'),

]