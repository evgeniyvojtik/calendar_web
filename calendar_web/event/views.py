from django.shortcuts import render

# Create your views here.
from django.views import View

from event.models import Event


class MainPage(View):
    def get(self, request):
        context = {}
        context['events'] = Event.objects.all()
        return render(request, 'index.html', context)