# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bankdata(models.Model):
    userid = models.ForeignKey('Userinfo', models.DO_NOTHING, db_column='USERID', blank=True, null=True)  # Field name made lowercase.
    bank_name = models.CharField(db_column='BANK_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    deposit_no = models.IntegerField(db_column='DEPOSIT_NO', primary_key=True)  # Field name made lowercase.
    deposit_amount = models.IntegerField(db_column='DEPOSIT_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    maturity_date = models.DateField(db_column='MATURITY_DATE', blank=True, null=True)  # Field name made lowercase.
    emi_number = models.IntegerField(db_column='EMI_NUMBER', blank=True, null=True)  # Field name made lowercase.
    emi_amount = models.IntegerField(db_column='EMI_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    loan_no = models.IntegerField(db_column='LOAN_NO', blank=True, null=True)  # Field name made lowercase.
    withdrawable_amount = models.IntegerField(db_column='WITHDRAWABLE_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    total_asset = models.BigIntegerField(db_column='TOTAL_ASSET', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bankdata'


class Category(models.Model):
    expense_acronym = models.CharField(db_column='EXPENSE_ACRONYM', primary_key=True, max_length=1)  # Field name made lowercase.
    expense_category = models.CharField(db_column='EXPENSE_CATEGORY', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'category'


class Incomesources(models.Model):
    userid = models.ForeignKey('Userinfo', models.DO_NOTHING, db_column='USERID', blank=True, null=True)  # Field name made lowercase.
    source_id = models.IntegerField(db_column='SOURCE_ID', primary_key=True)  # Field name made lowercase.
    monthly_income = models.IntegerField(db_column='MONTHLY_INCOME', blank=True, null=True)  # Field name made lowercase.
    rental_income = models.IntegerField(db_column='RENTAL_INCOME', blank=True, null=True)  # Field name made lowercase.
    intrest_amount = models.IntegerField(db_column='INTREST_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    other_sources = models.IntegerField(db_column='OTHER_SOURCES', blank=True, null=True)  # Field name made lowercase.
    total_cash = models.IntegerField(db_column='TOTAL_CASH', blank=True, null=True)  # Field name made lowercase.
    bank_balance = models.BigIntegerField(db_column='BANK_BALANCE', blank=True, null=True)  # Field name made lowercase.
    net_amount = models.BigIntegerField(db_column='NET_AMOUNT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'incomesources'


class MonthlyExpenses(models.Model):
    userid = models.ForeignKey('Userinfo', models.DO_NOTHING, db_column='USERID', blank=True, null=True)  # Field name made lowercase.
    expense_no = models.IntegerField(db_column='EXPENSE_NO', primary_key=True)  # Field name made lowercase.
    date_of_expense = models.DateField(db_column='DATE_OF_EXPENSE', blank=True, null=True)  # Field name made lowercase.
    expense_acronym = models.ForeignKey(Category, models.DO_NOTHING, db_column='EXPENSE_ACRONYM', blank=True, null=True)  # Field name made lowercase.
    expense_desc = models.CharField(db_column='EXPENSE_DESC', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mode_of_payment = models.CharField(db_column='MODE_OF_PAYMENT', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'monthly_expenses'


class Userinfo(models.Model):
    user_id = models.CharField(db_column='USER_ID', primary_key=True, max_length=6)  # Field name made lowercase.
    username = models.CharField(db_column='USERNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='GENDER', max_length=1, blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='AGE', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    phone_no = models.BigIntegerField(db_column='PHONE_NO', blank=True, null=True)  # Field name made lowercase.
    working_or_not = models.CharField(db_column='WORKING_OR_NOT', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userinfo'
