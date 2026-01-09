from django.shortcuts import render,redirect,get_object_or_404
from openpyxl import Workbook
from django.http import HttpResponse
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


# UPDATE VIEW
def update_expense(request, id):
    expense = get_object_or_404(Expense, id=id)

    if request.method == "POST":
        expense.expense_id = request.POST.get('expense_id')
        expense.date = request.POST.get('date')
        expense.category = request.POST.get('category')
        expense.amount = request.POST.get('amount')
        expense.description = request.POST.get('description')
        expense.payment_mode = request.POST.get('payment_mode')
        expense.merchant_name = request.POST.get('merchant_name')
        expense.location = request.POST.get('location')
        expense.notes = request.POST.get('notes')
        expense.created_by = request.POST.get('created_by')

        expense.save()
        return redirect('/')

    return render(request, 'expenseapp/update.html', {'expense': expense})



def delete_expense(request,id):
    expen=Expense.objects.get(id=id)
    expen.delete()
    return redirect('/')

def export_expenses_excel(request):
    # Create workbook and sheet
    wb = Workbook()
    ws = wb.active
    ws.title = "Expenses"

    # Header row
    ws.append([
        "Expense ID",
        "Date",
        "Category",
        "Amount",
        "Description",
        "Payment Mode",
        "Merchant Name",
        "Location",
        "Notes",
        "Created By"
    ])
    for e in Expense.objects.all():
        ws.append([
            e.expense_id,
            e.date.strftime("%d-%m-%Y"),
            e.category,
            float(e.amount),
            e.description,
            e.payment_mode,
            e.merchant_name,
            e.location,
            e.notes,
            e.created_by
        ])

    # Response as Excel file
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="expense_report.xlsx"'

    wb.save(response)
    return response