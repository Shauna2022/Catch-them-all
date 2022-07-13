from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from main_app.models import Cards
from .forms import SellingForm

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cards_index(request):
  cards = Cards.objects.all()
  return render(request, 'cards/index.html', { 'cards': cards})



def cards_detail(request, card_id):
  cards = Cards.objects.get(id=card_id)
  selling_form = SellingForm()
  return render(request, 'cards/detail.html', {
    'cards': cards, 'selling_form': selling_form
  })
def add_selling(request, card_id):
   pass

def add_selling(request, card_id):
  form = SellingForm(request.POST)
  if form.is_valid():
    new_selling = form.save(commit=False)
    new_selling.card_id = card_id
    new_selling.save()
  return redirect('detail', card_id=card_id)

class CardCreate(CreateView):
  model = Cards
  fields = ['name', 'type', 'hp', 'move_name_1', 'move_name_2', 'weakness_type', 'card_type' ]
  success_url = '/cards/'

class CardUpdate(UpdateView):
  model = Cards
  fields = '__all__'
  success_url = '/cards/'

class CardDelete(DeleteView):
  model = Cards
  success_url = '/cards/'