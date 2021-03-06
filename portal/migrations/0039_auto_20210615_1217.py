# Generated by Django 3.0.8 on 2021-06-15 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0038_tbl_workflow_mst_service_asset_ref_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_workflow_sub_details',
            name='sla_days',
        ),
        migrations.AddField(
            model_name='tbl_workflow_activity',
            name='actual_response_time',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Actual Response Time'),
        ),
        migrations.AddField(
            model_name='tbl_workflow_activity',
            name='sla',
            field=models.IntegerField(default=0, verbose_name='SLA'),
        ),
        migrations.AddField(
            model_name='tbl_workflow_mst',
            name='resolution_time',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Resolution Time'),
        ),
        migrations.AddField(
            model_name='tbl_workflow_sub_details',
            name='sla_response_time',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Response Time'),
        ),
    ]
