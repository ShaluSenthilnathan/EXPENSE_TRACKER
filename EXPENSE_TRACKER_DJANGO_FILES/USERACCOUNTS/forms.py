from django import forms 
from USERACCOUNTS.models import Userinfo,Incomesources


class UserinfoTask(forms.ModelForm):
    class Meta:
        model = Userinfo
        fields = ['user_id','username','gender','age','email','phone_no','working_or_not']

class IncomesourcesTask(forms.ModelForm):
    class Meta:
        model = Incomesources
        fields = ['userid','source_id','monthly_income','rental_income','intrest_amount','other_sources','total_cash','bank_balance','net_amount']