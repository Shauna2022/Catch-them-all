from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from main_app.models import Cards
from .forms import SellingForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def cards_index(request):
  cards = Cards.objects.filter(user=request.user)
  return render(request, 'cards/index.html', { 'cards': cards})


@login_required
def cards_detail(request, card_id):
  cards = Cards.objects.get(id=card_id)
  selling_form = SellingForm()
  return render(request, 'cards/detail.html', {
    'cards': cards, 'selling_form': selling_form
  })

@login_required
def add_selling(request, card_id):
  form = SellingForm(request.POST)
  if form.is_valid():
    new_selling = form.save(commit=False)
    new_selling.card_id = card_id
    new_selling.save()
  return redirect('detail', card_id=card_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class CardCreate(LoginRequiredMixin, CreateView):
  model = Cards
  fields = ['name', 'type', 'hp', 'move_name_1', 'move_name_2', 'weakness_type', 'card_type' ]
  success_url = '/cards/'
  
  def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)

class CardUpdate(LoginRequiredMixin, UpdateView):
  model = Cards
  fields = '__all__'
  success_url = '/cards/'

class CardDelete(LoginRequiredMixin, DeleteView):
  model = Cards
  success_url = '/cards/'