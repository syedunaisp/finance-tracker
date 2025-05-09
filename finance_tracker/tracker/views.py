from django.shortcuts import render, redirect
from .forms import TransactionForm
from django.contrib.auth.decorators import login_required
from .models import Transaction

@login_required
def transaction_add(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user  
            transaction.save()
            return redirect('dashboard')
    else:
        form = TransactionForm()
    return render(request, 'transaction_add.html', {'form': form})

@login_required
def dashboard(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    return render(request, 'dashboard.html', {'transactions': transactions})