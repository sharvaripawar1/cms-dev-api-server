# Generated by Django 3.0.8 on 2021-05-25 11:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0029_tbl_issue_details_is_it_original_entry_flag'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_workflow_activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share_id', models.IntegerField(default=0, verbose_name='Share ID')),
                ('form_ref_id', models.IntegerField(default=0, verbose_name='Form Ref Id')),
                ('level', models.CharField(max_length=30, verbose_name='Level')),
                ('is_assigned_role_person', models.CharField(default='Y', max_length=1, verbose_name='Is Assigned Role Person')),
                ('assigned_role', models.CharField(max_length=30, verbose_name='Assigned Role')),
                ('assigned_person', models.CharField(max_length=30, verbose_name='Assigned Person')),
                ('sequence_number', models.IntegerField(default=0, verbose_name='Sequence Number')),
                ('next_sequence_number', models.IntegerField(default=0, verbose_name='Next Sequence Number')),
                ('status', models.CharField(max_length=20, verbose_name='Status')),
                ('is_active', models.CharField(default='Y', max_length=1, verbose_name='Is Active')),
                ('is_deleted', models.CharField(default='N', max_length=1, verbose_name='Is Deleted')),
                ('created_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Created Date Time')),
                ('created_by', models.IntegerField(default=0, verbose_name='Created By')),
                ('updated_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Updated Date Time')),
                ('updated_by', models.IntegerField(default=0, verbose_name='Updated By')),
                ('sub_application_id', models.CharField(max_length=20, verbose_name='Sub-Application ID')),
                ('application_id', models.CharField(max_length=20, verbose_name='Application ID')),
                ('action_ref_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_workflow_action_mst', verbose_name='Action Ref ID')),
                ('activity_ref_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_workflow_activity_mst', verbose_name='Activity Ref ID')),
                ('user_action_ref_id', models.ForeignKey(default=999, on_delete=django.db.models.deletion.PROTECT, related_name='user_action_ref_id', to='portal.tbl_workflow_action_mst', verbose_name='User Action Ref ID')),
                ('workflow_ref_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_workflow_mst', verbose_name='Step Ref Id')),
            ],
            options={
                'verbose_name_plural': 'tbl_workflow_activity',
            },
        ),
        migrations.CreateModel(
            name='tbl_workflow_activity_notification_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_notification_applicable', models.CharField(default='N', max_length=1, verbose_name='Is Notification Applicable')),
                ('is_email', models.CharField(default='N', max_length=1, verbose_name='Is Email')),
                ('is_text_message', models.CharField(default='N', max_length=1, verbose_name='Is Text Message')),
                ('is_whatsapp', models.CharField(default='N', max_length=1, verbose_name='Is Wahtsapp')),
                ('is_additional_email', models.CharField(default='N', max_length=1, verbose_name='Is Add Email')),
                ('is_additional_text_message', models.CharField(default='N', max_length=1, verbose_name='Is Add Message')),
                ('is_additional_watsapp', models.CharField(default='N', max_length=1, verbose_name='Is Add Wahtsapp')),
                ('is_additional_notification_to_senior_management', models.CharField(default='N', max_length=1, verbose_name='Is Add to Senior')),
                ('is_active', models.CharField(default='Y', max_length=1, verbose_name='Is Active')),
                ('is_deleted', models.CharField(default='N', max_length=1, verbose_name='Is Deleted')),
                ('created_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Created Date Time')),
                ('created_by', models.IntegerField(default=0, verbose_name='Created By')),
                ('updated_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Updated Date Time')),
                ('updated_by', models.IntegerField(default=0, verbose_name='Updated By')),
                ('sub_application_id', models.CharField(max_length=20, verbose_name='Sub-Application ID')),
                ('application_id', models.CharField(max_length=20, verbose_name='Application ID')),
                ('header_ref_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='workflowactivity_not', to='portal.tbl_workflow_activity', verbose_name='Header Ref ID')),
            ],
            options={
                'verbose_name_plural': 'tbl_workflow_activity_notification_details',
            },
        ),
        migrations.AddField(
            model_name='tbl_employee_mst',
            name='company_type_ref_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='employee_company_type', to='portal.tbl_master', verbose_name='Company Type Ref ID'),
        ),
        migrations.CreateModel(
            name='tbl_workflow_routing_activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence_number', models.IntegerField(default=0, verbose_name='Sequence Number')),
                ('next_sequence_number', models.IntegerField(default=0, verbose_name='Next Sequence Number')),
                ('status', models.CharField(max_length=20, verbose_name='Status')),
                ('is_active', models.CharField(default='Y', max_length=1, verbose_name='Is Active')),
                ('is_deleted', models.CharField(default='N', max_length=1, verbose_name='Is Deleted')),
                ('created_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Created Date Time')),
                ('created_by', models.IntegerField(default=0, verbose_name='Created By')),
                ('updated_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Updated Date Time')),
                ('updated_by', models.IntegerField(default=0, verbose_name='Updated By')),
                ('sub_application_id', models.CharField(max_length=20, verbose_name='Sub-Application ID')),
                ('application_id', models.CharField(max_length=20, verbose_name='Application ID')),
                ('workflow_routing_details_ref_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_workflow_routing_details', verbose_name='Routing Ref ID')),
                ('workflow_routing_ref_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_workflow_routing_mst', verbose_name='Routing Ref ID')),
            ],
            options={
                'verbose_name_plural': 'tbl_workflow_routing_activity',
            },
        ),
        migrations.CreateModel(
            name='tbl_workflow_activity_notification_log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_notification', models.CharField(default=0, max_length=20, verbose_name='Type of Notification')),
                ('status', models.CharField(max_length=20, verbose_name='Status')),
                ('is_active', models.CharField(default='Y', max_length=1, verbose_name='Is Active')),
                ('is_deleted', models.CharField(default='N', max_length=1, verbose_name='Is Deleted')),
                ('created_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Created Date Time')),
                ('created_by', models.IntegerField(default=0, verbose_name='Created By')),
                ('updated_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Updated Date Time')),
                ('updated_by', models.IntegerField(default=0, verbose_name='Updated By')),
                ('sub_application_id', models.CharField(max_length=20, verbose_name='Sub-Application ID')),
                ('application_id', models.CharField(max_length=20, verbose_name='Application ID')),
                ('details_ref_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='initialItemRow', to='portal.tbl_workflow_activity_notification_details', verbose_name='Header Ref ID')),
                ('header_ref_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='initialItemRow', to='portal.tbl_workflow_activity', verbose_name='Header Ref ID')),
            ],
            options={
                'verbose_name_plural': 'tbl_workflow_activity_notification_log',
            },
        ),
    ]
