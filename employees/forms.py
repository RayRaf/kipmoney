from django import forms
from .models import Transaction, Employee

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['employee', 'amount', 'description']
        labels = {
            'employee': 'Сотрудник',
            'amount': 'Сумма (₽)',
            'description': 'Описание',
        }

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name']
        labels = {
            'name': 'Имя',
        }