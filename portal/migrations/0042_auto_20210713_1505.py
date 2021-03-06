# Generated by Django 3.1.2 on 2021-07-13 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0041_tbl_problem_issue_details_tbl_problem_issue_mst'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_problem_issue_mst',
            name='assigned_to_ref_id',
        ),
        migrations.RemoveField(
            model_name='tbl_problem_issue_mst',
            name='company_ref_id',
        ),
        migrations.RemoveField(
            model_name='tbl_problem_issue_mst',
            name='impact_ref_id',
        ),
        migrations.RemoveField(
            model_name='tbl_problem_issue_mst',
            name='issue_ref_id',
        ),
        migrations.RemoveField(
            model_name='tbl_problem_issue_mst',
            name='priority_ref_id',
        ),
        migrations.RemoveField(
            model_name='tbl_problem_issue_mst',
            name='reported_by',
        ),
        migrations.RemoveField(
            model_name='tbl_problem_issue_mst',
            name='service_asset_ref_id',
        ),
        migrations.RemoveField(
            model_name='tbl_problem_issue_mst',
            name='status_ref_id',
        ),
        migrations.RemoveField(
            model_name='tbl_problem_issue_mst',
            name='ticket_type_ref_id',
        ),
        migrations.DeleteModel(
            name='tbl_problem_issue_details',
        ),
        migrations.DeleteModel(
            name='tbl_problem_issue_mst',
        ),
    ]
