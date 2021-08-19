# Generated by Django 3.1.2 on 2021-07-13 09:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0042_auto_20210713_1505'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_problem_issue_mst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share_id', models.IntegerField(default=0, verbose_name='Share ID')),
                ('impact_on', models.CharField(blank=True, max_length=100, null=True, verbose_name='Impact On')),
                ('created_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Created Date Time')),
                ('form', models.CharField(blank=True, max_length=100, null=True, verbose_name='Form')),
                ('closed_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Closed Date Time')),
                ('closed_by', models.IntegerField(blank=True, default=0, null=True, verbose_name='Closed By')),
                ('is_active', models.CharField(default='Y', max_length=1, verbose_name='Is Active')),
                ('is_deleted', models.CharField(default='N', max_length=1, verbose_name='Is Deleted')),
                ('created_by', models.IntegerField(default=0, verbose_name='Created By')),
                ('updated_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Updated Date Time')),
                ('updated_by', models.IntegerField(default=0, verbose_name='Updated By')),
                ('sub_application_id', models.CharField(max_length=20, verbose_name='Sub-Application ID')),
                ('application_id', models.CharField(max_length=20, verbose_name='Application ID')),
                ('assigned_to_ref_id', models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_employee_mst', verbose_name='Assigned To Ref Id')),
                ('company_ref_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_company_mst', verbose_name='Company Ref Id')),
                ('impact_ref_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_master', verbose_name='Impact Ref Id')),
                ('issue_ref_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_issue_mst', verbose_name='Issue Ref Id')),
                ('priority_ref_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='problem_issue_priority_ref', to='portal.tbl_master', verbose_name='Priority Ref Id')),
                ('reported_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='problem_reported_by', to='portal.tbl_employee_mst', verbose_name='Reported By')),
                ('service_asset_ref_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_service_asset_mst', verbose_name='Service Asset Ref Id')),
                ('status_ref_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='problem_issue_status_ref', to='portal.tbl_ticket_status_mst', verbose_name='Status Ref Id')),
                ('ticket_type_ref_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_ticket_type_mst', verbose_name='Ticket Type Ref Id')),
            ],
            options={
                'verbose_name_plural': 'tbl_problem_issue_mst',
            },
        ),
        migrations.CreateModel(
            name='tbl_problem_issue_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('attach_document', models.CharField(blank=True, max_length=500, null=True, verbose_name='Attach Document')),
                ('is_it_original_entry_flag', models.CharField(default='N', max_length=1, verbose_name='Is it Original Entry Flag')),
                ('is_active', models.CharField(default='Y', max_length=1, verbose_name='Is Active')),
                ('is_deleted', models.CharField(default='N', max_length=1, verbose_name='Is Deleted')),
                ('created_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Created Date Time')),
                ('created_by', models.IntegerField(default=0, verbose_name='Created By')),
                ('updated_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Updated Date Time')),
                ('updated_by', models.IntegerField(default=0, verbose_name='Updated By')),
                ('sub_application_id', models.CharField(max_length=20, verbose_name='Sub-Application ID')),
                ('application_id', models.CharField(max_length=20, verbose_name='Application ID')),
                ('header_ref_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='initialItemRow', to='portal.tbl_problem_issue_mst', verbose_name='Header Ref ID')),
            ],
            options={
                'verbose_name_plural': 'tbl_problem_issue_details',
            },
        ),
    ]
