from django.db import models

class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    due_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('unpaid', 'Unpaid'), ('paid', 'Paid')])

    def __str__(self):
        return self.name
