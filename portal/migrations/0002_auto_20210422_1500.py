# Generated by Django 3.1.2 on 2021-04-22 09:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_calendar_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=4, verbose_name='Year')),
                ('period', models.CharField(max_length=2, verbose_name='Period')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date')),
                ('month', models.CharField(max_length=10, verbose_name='Month')),
                ('status', models.TextField(verbose_name='Status')),
                ('is_active', models.CharField(default='Y', max_length=1, verbose_name='Is Active')),
                ('is_deleted', models.CharField(default='N', max_length=1, verbose_name='Is Deleted')),
                ('created_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Created Date Time')),
                ('created_by', models.IntegerField(default=0, verbose_name='Created By')),
                ('updated_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Updated Date Time')),
                ('updated_by', models.IntegerField(default=0, verbose_name='Updated By')),
                ('sub_application_id', models.CharField(max_length=20, verbose_name='Sub-Application ID')),
                ('application_id', models.CharField(max_length=20, verbose_name='Application ID')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_calendar_mst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share_id', models.IntegerField(default=0, verbose_name='Share ID')),
                ('calendar_type_id', models.IntegerField(default=0, verbose_name='Calendar Type ID')),
                ('is_active', models.CharField(default='Y', max_length=1, verbose_name='Is Active')),
                ('is_deleted', models.CharField(default='N', max_length=1, verbose_name='Is Deleted')),
                ('created_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Created Date Time')),
                ('created_by', models.IntegerField(default=0, verbose_name='Created By')),
                ('updated_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Updated Date Time')),
                ('updated_by', models.IntegerField(default=0, verbose_name='Updated By')),
                ('sub_application_id', models.CharField(max_length=20, verbose_name='Sub-Application ID')),
                ('application_id', models.CharField(max_length=20, verbose_name='Application ID')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_employee_mst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15, verbose_name='First name')),
                ('middle_name', models.CharField(max_length=15, verbose_name='Middle name')),
                ('last_name', models.CharField(max_length=15, verbose_name='Last name')),
                ('employee_seq_no', models.CharField(max_length=40, verbose_name='Employee Seq No')),
                ('email', models.EmailField(max_length=30, verbose_name='Email')),
                ('password', models.CharField(max_length=20, verbose_name='Password')),
                ('phone', models.CharField(max_length=10, verbose_name='Phone Number')),
                ('pincode', models.CharField(max_length=6, verbose_name='Pincode')),
                ('address1', models.CharField(max_length=200, verbose_name='Address 1')),
                ('address2', models.CharField(max_length=200, verbose_name='Address 2')),
                ('address3', models.CharField(max_length=200, verbose_name='Address 3')),
                ('gender', models.CharField(max_length=10, verbose_name='Gender')),
                ('is_active', models.CharField(default='Y', max_length=1, verbose_name='Is Active')),
                ('is_deleted', models.CharField(default='N', max_length=1, verbose_name='Is Deleted')),
                ('created_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Created Date Time')),
                ('created_by', models.IntegerField(default=0, verbose_name='Created By')),
                ('updated_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Updated Date Time')),
                ('updated_by', models.IntegerField(default=0, verbose_name='Updated By')),
                ('sub_application_id', models.CharField(max_length=20, verbose_name='Sub-Application ID')),
                ('application_id', models.CharField(max_length=20, verbose_name='Application ID')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_term_mst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share_id', models.IntegerField(default=0, verbose_name='Share ID')),
                ('term_code', models.CharField(max_length=10, verbose_name='Term Code')),
                ('term_description', models.TextField(verbose_name='Term Description')),
                ('is_active', models.CharField(default='Y', max_length=1, verbose_name='Is Active')),
                ('is_deleted', models.CharField(default='N', max_length=1, verbose_name='Is Deleted')),
                ('created_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Created Date Time')),
                ('created_by', models.IntegerField(default=0, verbose_name='Created By')),
                ('updated_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Updated Date Time')),
                ('updated_by', models.IntegerField(default=0, verbose_name='Updated By')),
                ('sub_application_id', models.CharField(max_length=20, verbose_name='Sub-Application ID')),
                ('application_id', models.CharField(max_length=20, verbose_name='Application ID')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_user_mst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15, verbose_name='First name')),
                ('middle_name', models.CharField(max_length=15, verbose_name='Middle name')),
                ('last_name', models.CharField(max_length=15, verbose_name='Last name')),
                ('user_seq_no', models.CharField(max_length=40, verbose_name='Employee Seq No')),
                ('email', models.EmailField(max_length=30, verbose_name='Email')),
                ('password', models.CharField(max_length=20, verbose_name='Password')),
                ('phone', models.CharField(max_length=10, verbose_name='Phone Number')),
                ('gender', models.CharField(max_length=10, verbose_name='Gender')),
                ('is_active', models.CharField(default='Y', max_length=1, verbose_name='Is Active')),
                ('is_deleted', models.CharField(default='N', max_length=1, verbose_name='Is Deleted')),
                ('created_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Created Date Time')),
                ('created_by', models.IntegerField(default=0, verbose_name='Created By')),
                ('updated_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Updated Date Time')),
                ('updated_by', models.IntegerField(default=0, verbose_name='Updated By')),
                ('sub_application_id', models.CharField(max_length=20, verbose_name='Sub-Application ID')),
                ('application_id', models.CharField(max_length=20, verbose_name='Application ID')),
                ('company_ref_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_company_mst', verbose_name='Company Ref Id')),
                ('role_ref_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_role_mst', verbose_name='Role Ref Id')),
            ],
        ),
        migrations.AddConstraint(
            model_name='tbl_term_mst',
            constraint=models.UniqueConstraint(condition=models.Q(is_deleted='N'), fields=('term_code',), name='unique in term not deleted'),
        ),
        migrations.AddField(
            model_name='tbl_employee_mst',
            name='city_ref_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_city_mst', verbose_name='City ID'),
        ),
        migrations.AddField(
            model_name='tbl_employee_mst',
            name='company_ref_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_company_mst', verbose_name='Company Ref Id'),
        ),
        migrations.AddField(
            model_name='tbl_employee_mst',
            name='country_ref_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_country_mst', verbose_name='Country ID'),
        ),
        migrations.AddField(
            model_name='tbl_employee_mst',
            name='role_ref_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_role_mst', verbose_name='Role Ref Id'),
        ),
        migrations.AddField(
            model_name='tbl_employee_mst',
            name='state_ref_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_state_mst', verbose_name='State ID'),
        ),
        migrations.AddField(
            model_name='tbl_calendar_details',
            name='header_ref_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='initialItemRow', to='portal.tbl_calendar_mst', verbose_name='Header Ref ID'),
        ),
    ]
