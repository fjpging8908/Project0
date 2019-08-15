
import  json
from django.core import serializers
from django.shortcuts import render

from EventManager.forms import EventCreateForm
from EventManager.models import  Event,Category
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.generic import  CreateView, ListView, UpdateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.urls import reverse_lazy


def home(request):
    if request.user.is_authenticated:
        return redirect('/EventManager/event_view')
    else:
        return redirect('/EventManager/login')



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'Pages/registration/signup.html', {
        'form': form
    })

class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'secret_page.html'

class Event_View (ListView):
    model = Event
    template_name = 'Pages/event_list.html'
    context_object_name = 'Events'

    def get_queryset(self):
        new_context = Event.objects.filter(
            user=self.request.user
        ).order_by('-id')
        return new_context


class Event_Create (CreateView):
    model = Event
    fields = ('name','category','place','address','startDate','finishDate','eventType')
    template_name = 'Pages/event_form.html'
    success_url = reverse_lazy('Event_View')

    def post(self, request, *args, **kwargs):
        form = EventCreateForm(request.POST)
        if form.is_valid():
            event = form.save()
            event.user = self.request.user
            event.save()
            return HttpResponseRedirect(reverse_lazy('Event_View'))
        return redirect('/EventManager/Event_View')

class Event_Update(UpdateView):
        model = Event
        fields = ('name', 'category', 'place', 'address', 'startDate', 'finishDate', 'eventType')
        template_name = 'Pages/event_form.html'
        success_url = reverse_lazy('Event_View')

@csrf_exempt
def Event_Delete(request,id):
    ev= Event.objects.get(id=id)
    if ev is not None:
        ev.delete()
        return redirect('home')

# Create your views here.
@csrf_exempt
def getEvent(request):
    Event_List = Event.objects.all()
    context={'Event_List': Event_List}
    return render(request,'Pages/index.html',context)



@csrf_exempt
def Index(request):
    return render(request,'Pages/index.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'Pages/registration/login.html', {'form': form})
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print(user)
                login(request, user)
                return redirect('home')
            else:
                print('User not found')
        else:
            # If there were errors, we render the form with these
            # errors
            return render(request, 'Pages/registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    count = User.objects.count()
    return redirect('/EventManager/login')


@login_required
def secret_page(request):
    return render(request, 'secret_page.html')
