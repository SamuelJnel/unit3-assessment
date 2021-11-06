from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.db.models import Sum
from django.views.generic.edit import DeleteView
from .models import Widget
from .forms import WidgetForm




def home(request):
    widget_form = WidgetForm()
    widget = Widget.objects.all()
    count = Widget.objects.all().aggregate(Sum('quantity')) ['quantity__sum']
    return render(request, 'home.html', {'widget_form': widget_form, 'widget': widget, 'count': count})

def add_widget(request):
    form = WidgetForm(request.POST)
    if form.is_valid():
        new_widget = form.save(commit=False)
        new_widget.save()
    return redirect('home')

class WidgetDelete(DeleteView):
  model = Widget
  success_url = '/'

