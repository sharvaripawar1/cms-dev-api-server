# Generated by Django 3.1.2 on 2021-05-04 12:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0008_auto_20210427_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_left_panel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share_id', models.IntegerField(default=0, verbose_name='Share ID')),
                ('form_name', models.CharField(max_length=30, verbose_name='Form Name')),
                ('form_link', models.CharField(default=0, max_length=200, verbose_name='Form Link')),
                ('backend_model_name', models.CharField(default=0, max_length=500, verbose_name='Back End Model')),
                ('is_parent', models.CharField(default='N', max_length=1, verbose_name='Is Parent')),
                ('is_child', models.CharField(default='N', max_length=1, verbose_name='Is Child')),
                ('is_sub_child', models.CharField(default='N', max_length=1, verbose_name='Is Sub Child')),
                ('parent_code', models.CharField(max_length=30, verbose_name='Parent Code')),
                ('child_code', models.CharField(max_length=30, verbose_name='Child Code')),
                ('sub_child_code', models.CharField(max_length=30, verbose_name='Sub Child Code')),
                ('icon_class', models.CharField(max_length=30, verbose_name='Icon Class')),
                ('sequence_id', models.IntegerField(default=0, verbose_name='Sequence ID')),
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
            name='tbl_workflow_action_mst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_name', models.CharField(max_length=15, verbose_name='Action name')),
                ('action_description', models.CharField(max_length=15, verbose_name='Action Description')),
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
            name='tbl_workflow_activity_mst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.CharField(max_length=200, verbose_name='Activity name')),
                ('activity_description', models.CharField(max_length=200, verbose_name='Activity Description')),
                ('is_active', models.CharField(default='Y', max_length=1, verbose_name='Is Active')),
                ('is_deleted', models.CharField(default='N', max_length=1, verbose_name='Is Deleted')),
                ('created_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Created Date Time')),
                ('created_by', models.IntegerField(default=0, verbose_name='Created By')),
                ('updated_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Updated Date Time')),
                ('updated_by', models.IntegerField(default=0, verbose_name='Updated By')),
                ('sub_application_id', models.CharField(max_length=20, verbose_name='Sub-Application ID')),
                ('application_id', models.CharField(max_length=20, verbose_name='Application ID')),
                ('workflow_type_ref_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_master', verbose_name='Workflow Type Ref Id')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_workflow_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Database Field name')),
                ('approval_field_value', models.DecimalField(blank=True, decimal_places=4, default=0, max_digits=15, null=True, verbose_name='Approval Field Value')),
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
            name='tbl_workflow_level_data_mst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share_id', models.IntegerField(default=0, verbose_name='Share ID')),
                ('level', models.IntegerField(default=0, verbose_name='Level')),
                ('level_name', models.CharField(default=0, max_length=50, verbose_name='Level Name')),
                ('activity_sequence', models.CharField(default=0, max_length=50, verbose_name='Activity Sequence')),
                ('is_active', models.CharField(default='Y', max_length=1, verbose_name='Is Active')),
                ('is_deleted', models.CharField(default='N', max_length=1, verbose_name='Is Deleted')),
                ('created_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Created Date Time')),
                ('created_by', models.IntegerField(default=0, verbose_name='Created By')),
                ('updated_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Updated Date Time')),
                ('updated_by', models.IntegerField(default=0, verbose_name='Updated By')),
                ('sub_application_id', models.CharField(max_length=20, verbose_name='Sub-Application ID')),
                ('application_id', models.CharField(max_length=20, verbose_name='Application ID')),
                ('workflow_type_ref_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_master', verbose_name='Workflow Type Ref Id')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_workflow_mst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share_id', models.IntegerField(default=0, verbose_name='Share ID')),
                ('level_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Level Name')),
                ('workflow_name', models.CharField(max_length=50, verbose_name='Workflow name')),
                ('workflow_description', models.CharField(max_length=100, verbose_name='Workflow Description')),
                ('is_active', models.CharField(default='Y', max_length=1, verbose_name='Is Active')),
                ('is_deleted', models.CharField(default='N', max_length=1, verbose_name='Is Deleted')),
                ('created_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Created Date Time')),
                ('created_by', models.IntegerField(default=0, verbose_name='Created By')),
                ('updated_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Updated Date Time')),
                ('updated_by', models.IntegerField(default=0, verbose_name='Updated By')),
                ('sub_application_id', models.CharField(max_length=20, verbose_name='Sub-Application ID')),
                ('application_id', models.CharField(max_length=20, verbose_name='Application ID')),
                ('company_ref_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_company_mst', verbose_name='Company Ref Id')),
                ('level_ref_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_workflow_level_data_mst', verbose_name='Level Ref Id')),
                ('workflow_type_ref_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_master', verbose_name='Workflow Type Ref Id')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_workflow_routing_mst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workflow_routing_name', models.CharField(default='N', max_length=15, verbose_name='Workflow Routing Name')),
                ('workflow_routing_desc', models.CharField(default='N', max_length=100, verbose_name='Workflow Routing Desc')),
                ('version_number', models.IntegerField(default=0, verbose_name='Version Number')),
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
            name='tbl_workflow_sub_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence_number', models.IntegerField(default=0, verbose_name='Sequence Number')),
                ('next_sequence_number', models.IntegerField(default=0, verbose_name='Next Sequence Number')),
                ('is_email_required', models.BooleanField(blank=True, null=True)),
                ('is_whatsapp_required', models.BooleanField(blank=True, null=True)),
                ('is_sms_required', models.BooleanField(blank=True, null=True)),
                ('is_reminder_required', models.BooleanField(blank=True, null=True)),
                ('is_worklist_required', models.BooleanField(blank=True, null=True)),
                ('sla_days', models.IntegerField(default=0, verbose_name='Escalation Days')),
                ('reminder_days', models.IntegerField(default=0, verbose_name='Reminder Days Ref Id')),
                ('is_active', models.CharField(default='Y', max_length=1, verbose_name='Is Active')),
                ('is_deleted', models.CharField(default='N', max_length=1, verbose_name='Is Deleted')),
                ('created_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Created Date Time')),
                ('created_by', models.IntegerField(default=0, verbose_name='Created By')),
                ('updated_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Updated Date Time')),
                ('updated_by', models.IntegerField(default=0, verbose_name='Updated By')),
                ('sub_application_id', models.CharField(max_length=20, verbose_name='Sub-Application ID')),
                ('application_id', models.CharField(max_length=20, verbose_name='Application ID')),
                ('action_ref_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_workflow_action_mst', verbose_name='Action Ref Id')),
                ('activity_ref_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_workflow_activity_mst', verbose_name='Activity Ref Id')),
                ('company_ref_id', models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_company_mst', verbose_name='Company Ref Id')),
                ('details_ref_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='initialItemRow3', to='portal.tbl_workflow_details', verbose_name='Details Ref ID')),
                ('employee_ref_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_employee_mst', verbose_name='Employee Ref Id')),
                ('header_ref_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='initialItemRow2', to='portal.tbl_workflow_mst', verbose_name='Header Ref ID')),
                ('level_sub_details_ref_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_workflow_level_data_mst', verbose_name='Sub Details Ref Id')),
                ('role_ref_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_role_mst', verbose_name='Role Ref Id')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_workflow_routing_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence_number', models.IntegerField(default=0, verbose_name='Sequence Number')),
                ('next_sequence_number', models.IntegerField(default=0, verbose_name='Next Sequence Number')),
                ('is_active', models.CharField(default='Y', max_length=1, verbose_name='Is Active')),
                ('is_deleted', models.CharField(default='N', max_length=1, verbose_name='Is Deleted')),
                ('created_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Created Date Time')),
                ('created_by', models.IntegerField(default=0, verbose_name='Created By')),
                ('updated_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Updated Date Time')),
                ('updated_by', models.IntegerField(default=0, verbose_name='Updated By')),
                ('sub_application_id', models.CharField(max_length=20, verbose_name='Sub-Application ID')),
                ('application_id', models.CharField(max_length=20, verbose_name='Application ID')),
                ('header_ref_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='initialItemRow', to='portal.tbl_workflow_routing_mst', verbose_name='Workflow Routing Ref ID')),
                ('workflow_ref_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.tbl_workflow_mst', verbose_name='Workflow Ref ID')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_workflow_level_data_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence_number', models.IntegerField(default=0, verbose_name='Sequence Number')),
                ('next_sequence_number', models.IntegerField(default=0, verbose_name='Next Sequence Number')),
                ('is_active', models.CharField(default='Y', max_length=1, verbose_name='Is Active')),
                ('is_deleted', models.CharField(default='N', max_length=1, verbose_name='Is Deleted')),
                ('created_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Created Date Time')),
                ('created_by', models.IntegerField(default=0, verbose_name='Created By')),
                ('updated_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Updated Date Time')),
                ('updated_by', models.IntegerField(default=0, verbose_name='Updated By')),
                ('sub_application_id', models.CharField(max_length=20, verbose_name='Sub-Application ID')),
                ('application_id', models.CharField(max_length=20, verbose_name='Application ID')),
                ('action_ref_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_workflow_action_mst', verbose_name='Action Ref Id')),
                ('activity_ref_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_workflow_activity_mst', verbose_name='Activity Ref Id')),
                ('header_ref_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='initialItemRow', to='portal.tbl_workflow_level_data_mst', verbose_name='Header Ref ID')),
            ],
        ),
        migrations.AddField(
            model_name='tbl_workflow_details',
            name='header_ref_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='initialItemRow', to='portal.tbl_workflow_mst', verbose_name='Header Ref ID'),
        ),
        migrations.AddField(
            model_name='tbl_workflow_details',
            name='left_panel_ref_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_left_panel', verbose_name='Screen'),
        ),
        migrations.AddField(
            model_name='tbl_workflow_details',
            name='level_details_ref_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_workflow_level_data_mst', verbose_name='Level Details Ref Id'),
        ),
        migrations.AddConstraint(
            model_name='tbl_workflow_level_data_mst',
            constraint=models.UniqueConstraint(condition=models.Q(is_deleted='N'), fields=('activity_sequence',), name='unique_if_not_deleted_level'),
        ),
    ]
