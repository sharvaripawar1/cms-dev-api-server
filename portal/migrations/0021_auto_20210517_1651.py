# Generated by Django 3.0.8 on 2021-05-17 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0020_auto_20210517_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_left_panel',
            name='child_code',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Child Code'),
        ),
        migrations.AlterField(
            model_name='tbl_left_panel',
            name='icon_class',
            field=models.CharField(max_length=50, verbose_name='Icon Class'),
        ),
        migrations.AlterField(
            model_name='tbl_left_panel',
            name='parent_code',
            field=models.CharField(max_length=50, verbose_name='Parent Code'),
        ),
        migrations.AlterField(
            model_name='tbl_left_panel',
            name='sub_child_code',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Sub Child Code'),
        ),
    ]
