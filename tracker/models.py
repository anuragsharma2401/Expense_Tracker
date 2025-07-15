from django.db import models

# Create your models here.

class CurrentBalance(models.Model):
    current_balance = models.FloatField(default=0)

    

class TrackingHistory(models.Model):
    current_balance = models.ForeignKey(CurrentBalance, on_delete=models.CASCADE,default=1)
    amount = models.FloatField(editable=False)
    expense_type = models.CharField(max_length=100,choices=(('CREDIT','CREDIT'),('DEBIT','DEBIT')))
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"The amount is ₹{self.amount} for {self.description} expense type is {self.expense_type}"
       
class RequestLogs(models.Model):
    request_info = models.TextField()
    request_path = models.CharField(max_length=100)   
    request_method = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)    