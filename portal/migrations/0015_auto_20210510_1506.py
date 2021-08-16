# Generated by Django 3.1.2 on 2021-05-10 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0014_auto_20210510_1503'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='tbl_service_asset_mst',
            name='unique if application name not deleted',
        ),
        migrations.RenameField(
            model_name='tbl_service_asset_mst',
            old_name='application_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='tbl_service_asset_mst',
            old_name='application_name',
            new_name='name',
        ),
    ]