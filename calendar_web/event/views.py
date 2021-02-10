from django.shortcuts import render, redirect
from django.views import View
from event.forms import EventForm
from event.models import Event


class MainPage(View):
    def get(self, request):
        context = {}
        context['events'] = Event.objects.all()
        context['form'] = EventForm()
        return render(request, 'index.html', context)

class EventView(View):
    def post(self, request):
        form = EventForm(data=request.POST)
        ef = form.save(commit=False)
        ef.user = request.user
        ef.save()
        return redirect('the-main-page')

def delete_event(request, id):
    if request.user.is_authenticated:
        event = Event.objects.get(id=id)
        if request.user == event.user:
            event.delete()
        return redirect('the-main-page')

class UpdateEvent(View):
    def get(self, request):
        pass

    def post(self, request):
        pass
