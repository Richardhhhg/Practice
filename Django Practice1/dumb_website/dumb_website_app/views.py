from django.shortcuts import render
from django.http import HttpResponse
from .forms import InputForm

# Create your views here.
def home(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['input']
            return render(request, 'success.html', {'input': name})
    else:
            form = InputForm()
    return render(request, 'input_form.html', {'form': form})
