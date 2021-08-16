# Generated by Django 3.0.8 on 2021-05-18 12:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0022_tbl_left_panel_backend_model_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_assign_screen_to_role_mst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share_id', models.IntegerField(default=0, verbose_name='Share ID')),
                ('assigned_to_role', models.IntegerField(default=0, verbose_name='Role')),
                ('parent_code', models.CharField(max_length=30, verbose_name='Parent Code')),
                ('child_code', models.CharField(max_length=30, verbose_name='Child Code')),
                ('sub_child_code', models.CharField(max_length=30, verbose_name='Sub Child Code')),
                ('read_access', models.CharField(default='N', max_length=1, verbose_name='Read Access')),
                ('write_access', models.CharField(default='N', max_length=1, verbose_name='Write Access')),
                ('delete_access', models.CharField(default='N', max_length=1, verbose_name='Delete Access')),
                ('is_active', models.CharField(default='Y', max_length=1, verbose_name='Is Active')),
                ('is_deleted', models.CharField(default='N', max_length=1, verbose_name='Is Deleted')),
                ('created_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Created Date Time')),
                ('created_by', models.IntegerField(default=0, verbose_name='Created By')),
                ('updated_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Updated Date Time')),
                ('updated_by', models.IntegerField(default=0, verbose_name='Updated By')),
                ('sub_application_id', models.CharField(max_length=20, verbose_name='Sub-Application ID')),
                ('application_id', models.CharField(max_length=20, verbose_name='Application ID')),
                ('company_ref_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_company_mst', verbose_name='Company Ref Id')),
                ('form_ref_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_left_panel', verbose_name='Form Ref Id')),
            ],
        ),
    ]