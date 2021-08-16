# Generated by Django 3.1.2 on 2021-05-17 07:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0018_auto_20210512_1243'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tbl_calendar_details',
            options={'verbose_name_plural': 'tbl_calendar_details'},
        ),
        migrations.AlterModelOptions(
            name='tbl_calendar_mst',
            options={'verbose_name_plural': 'tbl_calendar_mst'},
        ),
        migrations.AlterModelOptions(
            name='tbl_channel_mst',
            options={'verbose_name_plural': 'tbl_channel_mst'},
        ),
        migrations.AlterModelOptions(
            name='tbl_city_mst',
            options={'verbose_name_plural': 'tbl_city_mst'},
        ),
        migrations.AlterModelOptions(
            name='tbl_company_application_link_details',
            options={'verbose_name_plural': 'tbl_company_application_link_details'},
        ),
        migrations.AlterModelOptions(
            name='tbl_company_application_link_mst',
            options={'verbose_name_plural': 'tbl_company_application_link_mst'},
        ),
        migrations.AlterModelOptions(
            name='tbl_company_contact_details',
            options={'verbose_name_plural': 'tbl_company_contact_details'},
        ),
        migrations.AlterModelOptions(
            name='tbl_company_mst',
            options={'verbose_name_plural': 'tbl_company_mst'},
        ),
        migrations.AlterModelOptions(
            name='tbl_country_mst',
            options={'verbose_name_plural': 'tbl_country_mst'},
        ),
        migrations.AlterModelOptions(
            name='tbl_currency_mst',
            options={'verbose_name_plural': 'tbl_currency_mst'},
        ),
        migrations.AlterModelOptions(
            name='tbl_employee_mst',
            options={'verbose_name_plural': 'tbl_employee_mst'},
        ),
        migrations.AlterModelOptions(
            name='tbl_left_panel',
            options={'verbose_name_plural': 'tbl_left_panel'},
        ),
        migrations.AlterModelOptions(
            name='tbl_location_mst',
            options={'verbose_name_plural': 'tbl_location_mst'},
        ),
        migrations.AlterModelOptions(
            name='tbl_login_mst',
            options={'verbose_name_plural': 'tbl_login_mst'},
        ),
        migrations.AlterModelOptions(
            name='tbl_master',
            options={'verbose_name_plural': 'tbl_master'},
        ),
        migrations.AlterModelOptions(
            name='tbl_message_mst',
            options={'verbose_name_plural': 'tbl_message_mst'},
        ),
        migrations.AlterModelOptions(
            name='tbl_role_application_details',
            options={'verbose_name_plural': 'tbl_role_application_details'},
        ),
        migrations.AlterModelOptions(
            name='tbl_role_application_mst',
            options={'verbose_name_plural': 'tbl_role_application_mst'},
        ),
        migrations.AlterModelOptions(
            name='tbl_role_mst',
            options={'verbose_name_plural': 'tbl_role_mst'},
        ),
        migrations.AlterModelOptions(
            name='tbl_service_asset_mst',
            options={'verbose_name_plural': 'tbl_service_asset_mst'},
        ),
        migrations.AlterModelOptions(
            name='tbl_sla_details',
            options={'verbose_name_plural': 'tbl_sla_details'},
        ),
        migrations.AlterModelOptions(
            name='tbl_sla_mst',
            options={'verbose_name_plural': 'tbl_sla_mst'},
        ),
        migrations.AlterModelOptions(
            name='tbl_state_mst',
            options={'verbose_name_plural': 'tbl_state_mst'},
        ),
        migrations.AlterModelOptions(
            name='tbl_term_mst',
            options={'verbose_name_plural': 'tbl_term_mst'},
        ),
        migrations.AlterModelOptions(
            name='tbl_ticket_status_mst',
            options={'verbose_name_plural': 'tbl_ticket_status_mst'},
        ),
        migrations.AlterModelOptions(
            name='tbl_ticket_type_mst',
            options={'verbose_name_plural': 'tbl_ticket_type_mst'},
        ),
        migrations.AlterModelOptions(
            name='tbl_user_mst',
            options={'verbose_name_plural': 'tbl_user_mst'},
        ),
        migrations.AlterModelOptions(
            name='tbl_workflow_action_mst',
            options={'verbose_name_plural': 'tbl_workflow_action_mst'},
        ),
        migrations.AlterModelOptions(
            name='tbl_workflow_activity_mst',
            options={'verbose_name_plural': 'tbl_workflow_activity_mst'},
        ),
        migrations.AlterModelOptions(
            name='tbl_workflow_details',
            options={'verbose_name_plural': 'tbl_workflow_details'},
        ),
        migrations.AlterModelOptions(
            name='tbl_workflow_level_data_details',
            options={'verbose_name_plural': 'tbl_workflow_level_data_details'},
        ),
        migrations.AlterModelOptions(
            name='tbl_workflow_level_data_mst',
            options={'verbose_name_plural': 'tbl_workflow_level_data_mst'},
        ),
        migrations.AlterModelOptions(
            name='tbl_workflow_mst',
            options={'verbose_name_plural': 'tbl_workflow_mst'},
        ),
        migrations.AlterModelOptions(
            name='tbl_workflow_routing_details',
            options={'verbose_name_plural': 'tbl_workflow_routing_details'},
        ),
        migrations.AlterModelOptions(
            name='tbl_workflow_routing_mst',
            options={'verbose_name_plural': 'tbl_workflow_routing_mst'},
        ),
        migrations.AlterModelOptions(
            name='tbl_workflow_sub_details',
            options={'verbose_name_plural': 'tbl_workflow_sub_details'},
        ),
        migrations.RemoveConstraint(
            model_name='tbl_role_application_mst',
            name='tbl_role_application_mst unique if not deleted',
        ),
        migrations.AddField(
            model_name='tbl_issue_mst',
            name='closed_by',
            field=models.IntegerField(default=0, verbose_name='Closed By'),
        ),
        migrations.AlterField(
            model_name='tbl_employee_mst',
            name='middle_name',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Middle name'),
        ),
        migrations.AlterField(
            model_name='tbl_issue_mst',
            name='closed_date_time',
            field=models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Closed Date Time'),
        ),
        migrations.AlterField(
            model_name='tbl_issue_mst',
            name='impact_ref_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_master', verbose_name='Impact Ref Id'),
        ),
        migrations.AlterField(
            model_name='tbl_user_mst',
            name='middle_name',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Middle name'),
        ),
    ]