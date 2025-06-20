from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def tradehistory(request):
    return render(request, 'tradehistory.html')

def portfolio(request):
    return render(request, 'portfolio.html')