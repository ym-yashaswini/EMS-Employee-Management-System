# Generated by Django 4.0.2 on 2022-04-05 15:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('Employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('Password', models.CharField(max_length=100)),
                ('First_Name', models.CharField(max_length=150)),
                ('Last_Name', models.CharField(max_length=15)),
                ('Email_Id', models.CharField(default='', max_length=50, unique=True)),
                ('Phone_Number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('Emergency_Contact_Name', models.CharField(max_length=15)),
                ('Emergency_Contact_Number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('Gender', models.CharField(max_length=1)),
                ('Marital_Status', models.CharField(max_length=20, null=True)),
                ('Alternate_Email_Id', models.CharField(max_length=50, null=True)),
                ('IsOwner', models.BooleanField(default=False, max_length=3)),
                ('Status_In_Company', models.CharField(default='Active', max_length=9)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name='holidays_available',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Holiday_Date', models.DateField()),
                ('Holiday_Reason', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'holidays_available',
            },
        ),
        migrations.CreateModel(
            name='leave_available',
            fields=[
                ('Casual_Available', models.IntegerField()),
                ('Sick_Available', models.IntegerField()),
                ('Casual_Booked', models.IntegerField(default=0)),
                ('Sick_Booked', models.IntegerField(default=0)),
                ('Employee', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='login.employee')),
            ],
            options={
                'db_table': 'leave_available',
            },
        ),
        migrations.CreateModel(
            name='work_details',
            fields=[
                ('Employee', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='login.employee')),
                ('Designation', models.CharField(default='', max_length=20)),
                ('Date_of_Joining', models.DateField()),
                ('CTC', models.DecimalField(decimal_places=2, max_digits=7)),
                ('Department', models.CharField(max_length=20)),
                ('Employee_Status', models.CharField(max_length=20)),
                ('Reporting_To', models.CharField(max_length=20)),
                ('Employee_Type', models.CharField(max_length=20)),
                ('Work_Phone', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
            ],
            options={
                'db_table': 'work_details',
            },
        ),
        migrations.CreateModel(
            name='Paystubs_Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Basic_Salary', models.DecimalField(decimal_places=2, max_digits=7)),
                ('Account_Number', models.IntegerField()),
                ('Bank_Name', models.CharField(max_length=45)),
                ('Institution_Code', models.CharField(max_length=45)),
                ('Month_Salary_Paid', models.CharField(max_length=20)),
                ('Tax_Applied', models.CharField(default='13%', max_length=45)),
                ('Employee', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='login.employee')),
            ],
            options={
                'db_table': 'Paystubs_Services',
            },
        ),
        migrations.CreateModel(
            name='leave_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Leave_Reason', models.CharField(max_length=1000)),
                ('Leave_Type', models.CharField(max_length=100)),
                ('From_Date', models.CharField(max_length=15)),
                ('To_Date', models.CharField(max_length=15)),
                ('Status', models.CharField(max_length=35)),
                ('Employee', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='login.employee')),
            ],
            options={
                'db_table': 'leave_details',
            },
        ),
        migrations.CreateModel(
            name='attendance_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Punch_In', models.TimeField()),
                ('Punch_Out', models.TimeField(null=True)),
                ('Date_col', models.DateField()),
                ('Day_col', models.CharField(max_length=9)),
                ('Working_hours', models.TimeField(null=True)),
                ('Work_Notes', models.CharField(max_length=1000, null=True)),
                ('Employee', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='login.employee')),
            ],
            options={
                'db_table': 'attendance_status',
            },
        ),
    ]