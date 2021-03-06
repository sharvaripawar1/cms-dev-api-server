# Generated by Django 3.0.8 on 2021-05-24 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0027_auto_20210521_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_assignees_action_mst',
            name='assigned_to_ref_id',
        ),
        migrations.RemoveField(
            model_name='tbl_assignees_action_mst',
            name='company_ref_id',
        ),
        migrations.RemoveField(
            model_name='tbl_assignees_action_mst',
            name='helpdesk_mst_ref_id',
        ),
        migrations.RemoveField(
            model_name='tbl_assignees_action_mst',
            name='impact_ref_id',
        ),
        migrations.RemoveField(
            model_name='tbl_assignees_action_mst',
            name='issue_mst_ref_id',
        ),
        migrations.RemoveField(
            model_name='tbl_assignees_action_mst',
            name='priority_ref_id',
        ),
        migrations.RemoveField(
            model_name='tbl_assignees_action_mst',
            name='reported_by',
        ),
        migrations.RemoveField(
            model_name='tbl_assignees_action_mst',
            name='service_asset_ref_id',
        ),
        migrations.RemoveField(
            model_name='tbl_assignees_action_mst',
            name='status_ref_id',
        ),
        migrations.RemoveField(
            model_name='tbl_assignees_action_mst',
            name='ticket_type_ref_id',
        ),
        migrations.RemoveField(
            model_name='tbl_helpdesk_details',
            name='header_ref_id',
        ),
        migrations.RemoveField(
            model_name='tbl_helpdesk_mst',
            name='assigned_to_ref_id',
        ),
        migrations.RemoveField(
            model_name='tbl_helpdesk_mst',
            name='company_ref_id',
        ),
        migrations.RemoveField(
            model_name='tbl_helpdesk_mst',
            name='impact_ref_id',
        ),
        migrations.RemoveField(
            model_name='tbl_helpdesk_mst',
            name='issue_mst_ref_id',
        ),
        migrations.RemoveField(
            model_name='tbl_helpdesk_mst',
            name='priority_ref_id',
        ),
        migrations.RemoveField(
            model_name='tbl_helpdesk_mst',
            name='reported_by',
        ),
        migrations.RemoveField(
            model_name='tbl_helpdesk_mst',
            name='service_asset_ref_id',
        ),
        migrations.RemoveField(
            model_name='tbl_helpdesk_mst',
            name='status_ref_id',
        ),
        migrations.RemoveField(
            model_name='tbl_helpdesk_mst',
            name='ticket_type_ref_id',
        ),
        migrations.AlterModelOptions(
            name='tbl_workflow_routing_details',
            options={'verbose_name_plural': 'tbl_left_panel'},
        ),
        migrations.AddField(
            model_name='tbl_issue_details',
            name='is_it_employee_flag',
            field=models.CharField(default='N', max_length=1, verbose_name='Is it Employee Flag'),
        ),
        migrations.AddField(
            model_name='tbl_issue_mst',
            name='is_it_employee_flag',
            field=models.CharField(default='N', max_length=1, verbose_name='Is it Employee Flag'),
        ),
        migrations.DeleteModel(
            name='tbl_assignees_action_details',
        ),
        migrations.DeleteModel(
            name='tbl_assignees_action_mst',
        ),
        migrations.DeleteModel(
            name='tbl_helpdesk_details',
        ),
        migrations.DeleteModel(
            name='tbl_helpdesk_mst',
        ),
    ]
