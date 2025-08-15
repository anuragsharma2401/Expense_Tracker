from django.db import models

# Create your models here.

class CurrentBalance(models.Model):
    current_balance = models.FloatField(default=0)
    username = models.CharField(max_length=200,null=True,blank=True,unique=True)
    def __str__(self):
        return f"{self.username}"
    

class TrackingHistory(models.Model):
    username = models.ForeignKey(CurrentBalance, to_field="username",on_delete=models.CASCADE)
    amount = models.FloatField(editable=False)
    expense_type = models.CharField(max_length=100,choices=(('CREDIT','CREDIT'),('DEBIT','DEBIT')))
    description = models.CharField(max_length=200)
    # username = models.CharField(max_length=200,null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"The amount is ₹{self.amount} for {self.description} expense type is {self.expense_type}"
       
class RequestLogs(models.Model):
    request_info = models.TextField()
    request_path = models.CharField(max_length=100)   
    request_method = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)    