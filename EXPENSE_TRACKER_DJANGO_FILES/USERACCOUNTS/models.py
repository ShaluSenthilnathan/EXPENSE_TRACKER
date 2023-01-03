# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bankdata(models.Model):
    userid = models.ForeignKey('Userinfo',on_delete=models.CASCADE,default=None,db_column='USERID', blank=True,null=True)  # Field name made lowercase.
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
        
    def __str__(self):
        return self.expense_acronym


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Incomesources(models.Model):
    userid = models.ForeignKey('Userinfo',on_delete=models.CASCADE,default=None,db_column='USERID', blank=True,null=True)  # Field name made lowercase.
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
    userid = models.ForeignKey('Userinfo',on_delete=models.CASCADE,default=None,db_column='USERID', blank=True,null=True)  # Field name made lowercase.
    expense_no = models.IntegerField(db_column='EXPENSE_NO', primary_key=True)  # Field name made lowercase.
    date_of_expense = models.DateField(db_column='DATE_OF_EXPENSE', blank=True, null=True)  # Field name made lowercase.
    expense_acronym = models.ForeignKey('Category',on_delete=models.CASCADE,default=None,db_column='EXPENSE_ACRONYM', blank=True,null=True)  # Field name made lowercase.
    expense_desc = models.CharField(db_column='EXPENSE_DESC', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mode_of_payment = models.CharField(db_column='MODE_OF_PAYMENT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    amount_spent = models.IntegerField(db_column='AMOUNT_SPENT', blank=True, null=True)  # Field name made lowercase.

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
    
    def __str__(self):
        return self.user_id