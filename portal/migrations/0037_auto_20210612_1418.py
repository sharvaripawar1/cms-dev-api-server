# Generated by Django 3.0.8 on 2021-06-12 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0036_auto_20210601_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_workflow_activity',
            name='user_action_ref_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_action_ref_id', to='portal.tbl_workflow_action_mst', verbose_name='User Action Ref ID'),
        ),
    ]