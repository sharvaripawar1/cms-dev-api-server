# Generated by Django 3.0.8 on 2021-05-27 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0032_auto_20210527_0234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_assign_screen_to_role_mst',
            name='assigned_to_role',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_role_mst', verbose_name='Role'),
        ),
    ]
