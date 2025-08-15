from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(CurrentBalance)



@admin.action(description="Mark selected expenses as Credit")
def make_credit(modeladmin,request,queryset):
    for q in queryset:
        if(q.amount<0):
            q.amount = float(q.amount)* (-1)
            q.save()
    queryset.update(expense_type="CREDIT")

@admin.action(description="Mark selected expenses as Debit")
def make_debit(modeladmin,request,queryset):
    for q in queryset:
        if(q.amount>0):
            q.amount = float(q.amount)* (-1)
            q.save() 
    queryset.update(expense_type="DEBIT")    

class Trackinghistory(admin.ModelAdmin):
    list_display = ['amount',
                    'expense_type',
                    'description',
                    'created_at',
                    'transaction_nature',
    ]
    search_fields = ['expense_type',
                     'amount',
                     'description',
                    ]
    ordering = ['-created_at']
    list_filter = ['expense_type']
    actions = [make_credit,make_debit]
    def transaction_nature(self,obj):
        if obj.amount>0:
            return "Positive"
        return "Negative"    

class CurrentBalance(admin.ModelAdmin):
    list_display = ['username',
                    'current_balance',
    ]   


admin.site.register(TrackingHistory,Trackinghistory)


admin.site.site_header = "Expense Tracker"
admin.site.site_title = "Expense Tracker"
admin.site.site_url = "Expense Tracker"
