from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
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
    
    # Получение количества записей на страницу из параметра запроса
    per_page = request.GET.get('per_page', '10')
    try:
        per_page = int(per_page)
        if per_page not in [10, 50, 100]:
            per_page = 10
    except ValueError:
        per_page = 10
    
    # Пагинация
    paginator = Paginator(transactions, per_page)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'employees/employee_detail.html', {
        'employee': employee, 
        'page_obj': page_obj,
        'per_page': per_page
    })

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
