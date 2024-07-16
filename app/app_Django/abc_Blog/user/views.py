from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from django.urls import reverse_lazy
from user.forms import SignUpForm

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'Login/register.html'
    success_url = reverse_lazy('login') 
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.fullname = form.cleaned_data.get('fullname')
        user.save()
        return super().form_valid(form)

def login(request):
    return HttpResponse('esto es el login')

def index(request):
    return render(request, 'index.html')