# Generated by Django 3.1.2 on 2021-05-10 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0015_auto_20210510_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_service_asset_mst',
            name='description',
            field=models.CharField(default=0, max_length=100, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='tbl_service_asset_mst',
            name='name',
            field=models.CharField(default=0, max_length=100, verbose_name='name'),
        ),
        migrations.AddConstraint(
            model_name='tbl_service_asset_mst',
            constraint=models.UniqueConstraint(condition=models.Q(is_deleted='N'), fields=('name',), name='unique if application name not deleted'),
        ),
    ]
