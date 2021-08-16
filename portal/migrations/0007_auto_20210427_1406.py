# Generated by Django 3.1.2 on 2021-04-27 08:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portal', '0006_tbl_ticket_status_mst'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_company_mst',
            name='belongs_to_company_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='belongs_to', to='portal.tbl_company_mst'),
        ),
        migrations.AlterField(
            model_name='tbl_company_mst',
            name='currency_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_currency_mst'),
        ),
        migrations.AlterField(
            model_name='tbl_company_mst',
            name='management_belongs_to_company_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='managed_by', to='portal.tbl_company_mst'),
        ),
        migrations.AlterField(
            model_name='tbl_currency_mst',
            name='country_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='currency', to='portal.tbl_country_mst'),
        ),
        migrations.AlterField(
            model_name='tbl_login_mst',
            name='role_ref_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_role_mst', verbose_name='Role ID'),
        ),
        migrations.AlterField(
            model_name='tbl_login_mst',
            name='user',
            field=models.OneToOneField(default=0, max_length=140, on_delete=django.db.models.deletion.PROTECT, related_name='userRow', to=settings.AUTH_USER_MODEL),
        ),
    ]
