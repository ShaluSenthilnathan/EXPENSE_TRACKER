from django import forms 
from USERACCOUNTS.models import *


class UserinfoTask(forms.ModelForm):
    class Meta:
        model = Userinfo
        fields = ['user_id','username','gender','age','email','phone_no','working_or_not']

class IncomesourcesTask(forms.ModelForm):
    class Meta:
        model = Incomesources
        fields = ['userid','source_id','monthly_income','rental_income','intrest_amount','other_sources','total_cash','bank_balance','net_amount']
        
class MonthlyExpensesTask(forms.ModelForm):
    class Meta:
        model = MonthlyExpenses
        fields = ['userid','expense_no','date_of_expense','expense_acronym','expense_desc','mode_of_payment']
        
class BankdataTask(forms.ModelForm):
    class Meta:
        model = Bankdata
        fields = ['userid','bank_name','deposit_no','deposit_amount','maturity_date','emi_number','emi_amount','loan_no','withdrawable_amount','total_asset']