from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Employee
from .forms import TransactionForm, EmployeeForm

def landing_page(request):
    """Главная лендинг страница для отдела КИП"""
    return render(request, 'employees/landing.html')

@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})

@login_required
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    transactions = employee.transactions.order_by('-date_time')
    return render(request, 'employees/employee_detail.html', {'employee': employee, 'transactions': transactions})

@login_required
def create_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = TransactionForm()
    return render(request, 'employees/create_transaction.html', {'form': form})

@login_required
def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employees/create_employee.html', {'form': form})
