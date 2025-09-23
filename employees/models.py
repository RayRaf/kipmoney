from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_balance(self):
        return self.transactions.aggregate(total=models.Sum('amount'))['total'] or 0

class Transaction(models.Model):
    employee = models.ForeignKey(Employee, related_name='transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_time = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.employee.name} - {self.amount} on {self.date_time}"
