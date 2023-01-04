from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import DiabetesForm

# Create your views here.
def landing(request):
    return render(request, 'landing.html')

def home(request):
    return render(request, 'home.html')

def questionaire(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DiabetesForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DiabetesForm()

    return render(request, 'questionaire.html', {'form': form})
