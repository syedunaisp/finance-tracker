from django.shortcuts import render, redirect
from .forms import TransactionForm
from django.contrib.auth.decorators import login_required
from .models import Transaction

@login_required
def transaction_add(request):
    print("Transaction add view accessed via", request.method)
    if request.method == 'POST':
        print("POST request received")
        form = TransactionForm(request.POST, request.FILES)
        if form.is_valid():
            print("Form is valid")
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('dashboard')
        else:
            print("Form errors:", form.errors)
    else:
        print("Not a POST request")
        form = TransactionForm()
    return render(request, 'transaction_add.html', {'form': form})

@login_required
def transaction_view(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    return render(request, 'transaction_history.html', {
        'transactions': transactions
    })

@login_required
def dashboard(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    return render(request, 'dashboard.html', {'transactions': transactions})