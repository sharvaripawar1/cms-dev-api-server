# Generated by Django 3.1.2 on 2021-04-20 09:35

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_city_mst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share_id', models.IntegerField(default=0, verbose_name='Share ID')),
                ('city_name', models.CharField(max_length=20, verbose_name='City Name')),
                ('is_active', models.CharField(default='Y', max_length=1, verbose_name='Is Active')),
                ('is_deleted', models.CharField(default='N', max_length=1, verbose_name='Is Deleted')),
                ('created_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Created Date Time')),
                ('created_by', models.IntegerField(default=0, verbose_name='Created By')),
                ('updated_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Updated Date Time')),
                ('updated_by', models.IntegerField(default=0, verbose_name='Updated By')),
                ('sub_application_id', models.CharField(max_length=20, verbose_name='Sub-Application ID')),
                ('application_id', models.CharField(max_length=20, verbose_name='Application ID')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_company_mst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.IntegerField(default=0, unique=True, verbose_name='Company ID')),
                ('share_id', models.IntegerField(default=0, verbose_name='Share ID')),
                ('entity_share_id', models.TextField(default=0, verbose_name='Entity Share ID')),
                ('company_name', models.CharField(max_length=30)),
                ('company_shortname', models.CharField(default=0, max_length=30)),
                ('address1', models.CharField(default=0, max_length=30)),
                ('address2', models.CharField(default=0, max_length=30)),
                ('address3', models.CharField(default=0, max_length=30)),
                ('cin', models.CharField(default=0, max_length=21)),
                ('pan', models.CharField(default=0, max_length=15)),
                ('tan', models.CharField(default=0, max_length=15)),
                ('gst', models.CharField(default=0, max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('contact_person_name', models.CharField(default=0, max_length=30)),
                ('is_holding_company', models.BooleanField(blank=True, default=False, null=True)),
                ('is_this_under_same_management', models.BooleanField(blank=True, default=False, null=True)),
                ('percentage_holding', models.FloatField(default=0.0)),
                ('is_group_company', models.BooleanField(blank=True, default=False, null=True)),
                ('contact_person_mobile_number', models.CharField(max_length=30, null=True)),
                ('is_this_branch', models.BooleanField(blank=True, default=False, null=True)),
                ('pincode', models.CharField(default=0, max_length=8)),
                ('revision_status', models.CharField(default='None', max_length=20, verbose_name='Revision Status')),
                ('attach_document', models.CharField(blank=True, max_length=500, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=30, null=True)),
                ('bank_account', models.CharField(blank=True, max_length=35, null=True, validators=[django.core.validators.RegexValidator('^\\d{9,26}$')])),
                ('ifsc_code', models.CharField(blank=True, max_length=30, null=True)),
                ('comments', models.CharField(blank=True, max_length=30, null=True)),
                ('kyc_document_ref_id', models.CharField(default='N', max_length=200, verbose_name='Key Document Ref Id')),
                ('is_deleted', models.CharField(default='N', max_length=1, verbose_name='Is Deleted')),
                ('is_active', models.CharField(default='Y', max_length=1, verbose_name='Is Active')),
                ('created_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Created Date Time')),
                ('created_by', models.IntegerField(default=0, verbose_name='Created By')),
                ('updated_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Updated Date Time')),
                ('updated_by', models.IntegerField(default=0, verbose_name='Updated By')),
                ('sub_application_id', models.CharField(max_length=20, verbose_name='Sub-Application ID')),
                ('application_id', models.CharField(max_length=20, verbose_name='Application ID')),
                ('belongs_to_company_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='belongs_to', to='portal.tbl_company_mst')),
                ('city_ref_id', models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_city_mst', verbose_name='City Ref ID')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_country_mst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share_id', models.IntegerField(default=0, verbose_name='Share ID')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('short_name', models.CharField(max_length=20, verbose_name='Short Name')),
                ('is_active', models.CharField(default='Y', max_length=1, verbose_name='Is Active')),
                ('is_deleted', models.CharField(default='N', max_length=1, verbose_name='Is Deleted')),
                ('created_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Created Date Time')),
                ('created_by', models.IntegerField(default=0, verbose_name='Created By')),
                ('updated_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Updated Date Time')),
                ('updated_by', models.IntegerField(default=0, verbose_name='Updated By')),
                ('sub_application_id', models.CharField(max_length=20, verbose_name='Sub-Application ID')),
                ('application_id', models.CharField(max_length=20, verbose_name='Application ID')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share_id', models.IntegerField(default=0, verbose_name='Share ID')),
                ('master_type', models.CharField(max_length=50, verbose_name='Master Type')),
                ('master_value', models.CharField(max_length=20, verbose_name='Master Value')),
                ('master_key', models.CharField(max_length=20, verbose_name='Master Key')),
                ('is_active', models.CharField(default='Y', max_length=1, verbose_name='Is Active')),
                ('is_deleted', models.CharField(default='N', max_length=1, verbose_name='Is Deleted')),
                ('created_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Created Date Time')),
                ('created_by', models.IntegerField(default=0, verbose_name='Created By')),
                ('updated_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Updated Date Time')),
                ('updated_by', models.IntegerField(default=0, verbose_name='Updated By')),
                ('sub_application_id', models.CharField(max_length=20, verbose_name='Sub-Application ID')),
                ('application_id', models.CharField(max_length=20, verbose_name='Application ID')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_state_mst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share_id', models.IntegerField(default=0, verbose_name='Share ID')),
                ('state', models.CharField(max_length=20, verbose_name='State')),
                ('gst_state_code', models.IntegerField(default=0)),
                ('is_active', models.CharField(default='Y', max_length=1, verbose_name='Is Active')),
                ('is_deleted', models.CharField(default='N', max_length=1, verbose_name='Is Deleted')),
                ('created_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Created Date Time')),
                ('created_by', models.IntegerField(default=0, verbose_name='Created By')),
                ('updated_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Updated Date Time')),
                ('updated_by', models.IntegerField(default=0, verbose_name='Updated By')),
                ('sub_application_id', models.CharField(max_length=20, verbose_name='Sub-Application ID')),
                ('application_id', models.CharField(max_length=20, verbose_name='Application ID')),
                ('country_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='states', to='portal.tbl_country_mst', verbose_name='Country ID')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_role_mst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=30, verbose_name='Role Name')),
                ('is_active', models.CharField(default='Y', max_length=1, verbose_name='Is Active')),
                ('is_deleted', models.CharField(default='N', max_length=1, verbose_name='Is Deleted')),
                ('created_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Created Date Time')),
                ('created_by', models.IntegerField(default=0, verbose_name='Created By')),
                ('updated_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Updated Date Time')),
                ('updated_by', models.IntegerField(default=0, verbose_name='Updated By')),
                ('sub_application_id', models.CharField(max_length=20, verbose_name='Sub-Application ID')),
                ('application_id', models.CharField(max_length=20, verbose_name='Application ID')),
                ('company_ref_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_company_mst', verbose_name='Company Ref Id')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_login_mst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_user_ref_id', models.IntegerField(default=0, verbose_name='End User Ref ID')),
                ('is_deleted', models.CharField(default='N', max_length=1, verbose_name='Is Deleted')),
                ('created_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Created Date Time')),
                ('created_by', models.IntegerField(default=0, verbose_name='Created By')),
                ('updated_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Updated Date Time')),
                ('updated_by', models.IntegerField(default=0, verbose_name='Updated By')),
                ('sub_application_id', models.CharField(max_length=20, verbose_name='Sub-Application ID')),
                ('application_id', models.CharField(max_length=20, verbose_name='Application ID')),
                ('company_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_company_mst', verbose_name='Company Ref Id')),
                ('role_ref_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='portal.tbl_role_mst', verbose_name='Role ID')),
                ('user', models.OneToOneField(default=0, max_length=140, on_delete=django.db.models.deletion.CASCADE, related_name='userRow', to=settings.AUTH_USER_MODEL)),
                ('user_type_ref_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_master', verbose_name='User Type Ref ID')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_location_mst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share_id', models.IntegerField(default=0, verbose_name='Share ID')),
                ('location_name', models.CharField(max_length=20, verbose_name='Location Name')),
                ('address1', models.TextField(verbose_name='Address Line 1')),
                ('address2', models.TextField(verbose_name='Address Line 2')),
                ('address3', models.TextField(verbose_name='Address Line 3')),
                ('is_active', models.CharField(default='Y', max_length=1, verbose_name='Is Active')),
                ('is_deleted', models.CharField(default='N', max_length=1, verbose_name='Is Deleted')),
                ('created_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Created Date Time')),
                ('created_by', models.IntegerField(default=0, verbose_name='Created By')),
                ('updated_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Updated Date Time')),
                ('updated_by', models.IntegerField(default=0, verbose_name='Updated By')),
                ('sub_application_id', models.CharField(max_length=20, verbose_name='Sub-Application ID')),
                ('application_id', models.CharField(max_length=20, verbose_name='Application ID')),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations', to='portal.tbl_city_mst', verbose_name='City ID')),
                ('country_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_country_mst', verbose_name='Country ID')),
                ('state_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_state_mst', verbose_name='State ID')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_currency_mst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share_id', models.IntegerField(default=0, verbose_name='Share ID')),
                ('currency_code', models.CharField(max_length=10, verbose_name='Currency Code')),
                ('currency_name', models.CharField(max_length=30, verbose_name='Currency Name')),
                ('symbol', models.CharField(max_length=20, verbose_name='Symbol')),
                ('is_active', models.CharField(default='Y', max_length=1, verbose_name='Is Active')),
                ('is_deleted', models.CharField(default='N', max_length=1, verbose_name='Is Deleted')),
                ('created_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Created Date Time')),
                ('created_by', models.IntegerField(default=0, verbose_name='Created By')),
                ('updated_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Updated Date Time')),
                ('updated_by', models.IntegerField(default=0, verbose_name='Updated By')),
                ('sub_application_id', models.CharField(max_length=20, verbose_name='Sub-Application ID')),
                ('application_id', models.CharField(max_length=20, verbose_name='Application ID')),
                ('country_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currency', to='portal.tbl_country_mst')),
            ],
        ),
        migrations.AddField(
            model_name='tbl_company_mst',
            name='company_type_ref_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='company_type', to='portal.tbl_master', verbose_name='Company Type Ref ID'),
        ),
        migrations.AddField(
            model_name='tbl_company_mst',
            name='country_ref_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_country_mst', verbose_name='Country Ref ID'),
        ),
        migrations.AddField(
            model_name='tbl_company_mst',
            name='currency_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.tbl_currency_mst'),
        ),
        migrations.AddField(
            model_name='tbl_company_mst',
            name='location_ref_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_location_mst', verbose_name='Location Ref ID'),
        ),
        migrations.AddField(
            model_name='tbl_company_mst',
            name='management_belongs_to_company_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='managed_by', to='portal.tbl_company_mst'),
        ),
        migrations.AddField(
            model_name='tbl_company_mst',
            name='ownership_status_ref_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_master', verbose_name='Ownership Status Ref ID'),
        ),
        migrations.AddField(
            model_name='tbl_company_mst',
            name='state_ref_id',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.PROTECT, to='portal.tbl_state_mst', verbose_name='State Ref ID'),
        ),
        migrations.CreateModel(
            name='tbl_company_contact_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_person_name', models.CharField(max_length=30, verbose_name='Contact Person Name')),
                ('designation', models.CharField(blank=True, max_length=30, null=True, verbose_name='Contact Person Des')),
                ('contact_person_mobile_number', models.CharField(max_length=30, verbose_name='Contact Person Number')),
                ('email', models.EmailField(max_length=30, verbose_name='Email')),
                ('is_active', models.CharField(default='Y', max_length=1, verbose_name='Is Active')),
                ('is_deleted', models.CharField(default='N', max_length=1, verbose_name='Is Deleted')),
                ('created_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Created Date Time')),
                ('created_by', models.IntegerField(default=0, verbose_name='Created By')),
                ('updated_date_time', models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='Updated Date Time')),
                ('updated_by', models.IntegerField(default=0, verbose_name='Updated By')),
                ('sub_application_id', models.CharField(max_length=20, verbose_name='Sub-Application ID')),
                ('application_id', models.CharField(max_length=20, verbose_name='Application ID')),
                ('header_ref_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='initialItemRow', to='portal.tbl_company_mst', verbose_name='Header Ref ID')),
            ],
        ),
        migrations.AddField(
            model_name='tbl_city_mst',
            name='state_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cities', to='portal.tbl_state_mst', verbose_name='State ID'),
        ),
        migrations.AddConstraint(
            model_name='tbl_location_mst',
            constraint=models.UniqueConstraint(condition=models.Q(is_deleted='N'), fields=('location_name',), name='unique if not deleted'),
        ),
        migrations.AddConstraint(
            model_name='tbl_currency_mst',
            constraint=models.UniqueConstraint(condition=models.Q(is_deleted='N'), fields=('country_id',), name='unique_if_not_deleted'),
        ),
        migrations.AddConstraint(
            model_name='tbl_currency_mst',
            constraint=models.UniqueConstraint(condition=models.Q(is_deleted='N'), fields=('currency_code',), name='unique_if_not'),
        ),
        migrations.AddConstraint(
            model_name='tbl_company_mst',
            constraint=models.UniqueConstraint(condition=models.Q(is_deleted='N'), fields=('company_name',), name='unique in company name not deleted'),
        ),
        migrations.AddConstraint(
            model_name='tbl_company_mst',
            constraint=models.UniqueConstraint(condition=models.Q(is_deleted='N'), fields=('pan',), name='unique in company pan not deleted'),
        ),
    ]
