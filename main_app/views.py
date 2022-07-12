from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from main_app.models import Cards


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cards_index(request):
  cards = Cards.objects.all()
  return render(request, 'cards/index.html', { 'cards': cards})

def cards_detail(request, card_id):
  cards = Cards.objects.get(id=card_id)
  return render(request, 'cards/detail.html', { 'cards': cards })


class CardCreate(CreateView):
  model = Cards
  fields = '__all__'
  success_url = '/cards/'

class CardUpdate(UpdateView):
  model = Cards
  fields = '__all__'
  success_url = '/cards/'

class CardDelete(DeleteView):
  model = Cards
  success_url = '/cards/'