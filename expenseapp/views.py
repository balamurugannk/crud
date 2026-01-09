from django.shortcuts import render,redirect,get_object_or_404
from .models import *

def index(request):
    expen = Expense.objects.all()
    return render(request, 'expenseapp/index.html', {'expense': expen})


def add(request):

    return render(request, 'expenseapp/add.html')
def add_expense(request):
    if request.method == "POST":
        expense_id = request.POST['expense_id']
        date = request.POST['date']
        category = request.POST['category']
        amount = request.POST['amount']
        description = request.POST['description']
        payment_mode = request.POST['payment_mode']
        merchant_name = request.POST['merchant_name']
        location = request.POST['location']
        notes = request.POST['notes']
        created_by = request.POST['created_by']

        if all([date, category, amount]):
            Expense.objects.create(
                expense_id=expense_id,
                date=date,
                category=category,
                amount=amount,
                description=description,
                payment_mode=payment_mode,
                merchant_name=merchant_name,
                location=location,
                notes=notes,
                created_by=created_by
            )
            return redirect('/')

    return render(request, 'expenseapp/add.html')



def update(request,id):

    expen=Expense.objects.get(id=id)
    return render(request, 'expenseapp/update.html', {'expen': expen })


def update_expense(request, id):
    expen = get_object_or_404(Expense, pk=id)

    if request.method == "POST":
        expen.date = request.POST.get('date')
        expen.category = request.POST.get('category')
        expen.amount = request.POST.get('amount')
        expen.description = request.POST.get('description')
        expen.payment_mode = request.POST.get('payment_mode')
        expen.merchant_name = request.POST.get('merchant_name')
        expen.location = request.POST.get('location')
        expen.notes = request.POST.get('notes')
        expen.created_by = request.POST.get('created_by')
        expen.save()
        return redirect('/')

    return render(request, 'expenseapp/update.html', {'expense': expen})


def delete_expense(request,id):
    expen=Expense.objects.get(id=id)
    expen.delete()
    return redirect('/')