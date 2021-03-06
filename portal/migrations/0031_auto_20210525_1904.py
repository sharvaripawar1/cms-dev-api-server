# Generated by Django 3.0.8 on 2021-05-25 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0030_auto_20210525_1725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_issue_details',
            name='is_it_employee_flag',
        ),
        migrations.AlterField(
            model_name='tbl_assign_roles_to_enduser_mst',
            name='assigned_to_employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='assigned_to_employee', to='portal.tbl_employee_mst', verbose_name='Assigned To Employee'),
        ),
        migrations.AlterField(
            model_name='tbl_assign_roles_to_enduser_mst',
            name='assigned_to_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='assigned_to_user', to='portal.tbl_employee_mst', verbose_name='Assigned To User'),
        ),
        migrations.AlterField(
            model_name='tbl_issue_mst',
            name='reported_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reported_by', to='portal.tbl_employee_mst', verbose_name='Reported By'),
        ),
    ]
