from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from .models import Transaction
from .forms import TransactionForm

def transaction_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        transactions = Transaction.objects.filter(description__icontains=search_query)
    else:
        transactions = Transaction.objects.all()

    return render(request, 'myapp/transaction_list.html', {'transactions': transactions})

def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'myapp/transaction_form.html', {'form': form})

def edit_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'myapp/transaction_form.html', {'form': form})

def delete_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transaction_list')
    return render(request, 'myapp/transaction_confirm_delete.html', {'transaction': transaction})
