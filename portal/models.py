from django.db import models
from django.contrib.auth.models import User
from django.http.request import QueryDict
from django.utils import timezone
from django.core.validators import RegexValidator

# Create your models here.

class tbl_login_mst(models.Model):
    '''
    Columns taken from default User model: is_active, username & password
    '''
    user = models.OneToOneField(User,max_length=140, default=0,on_delete = models.PROTECT,related_name='userRow')
    company_id = models.ForeignKey("tbl_company_mst", default=0, verbose_name="Company Ref Id", on_delete=models.PROTECT)
    role_ref_id = models.ForeignKey('tbl_role_mst', default=0,verbose_name="Role ID",on_delete=models.PROTECT)
    user_type_ref_id = models.ForeignKey("tbl_master", default=1,verbose_name="User Type Ref ID",on_delete=models.PROTECT)
    end_user_ref_id = models.IntegerField(default=0,verbose_name="End User Ref ID")
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")

    class Meta:
        verbose_name_plural = "tbl_login_mst"

class tbl_role_mst(models.Model):
    role_name = models.CharField(max_length=30,verbose_name='Role Name')
    company_ref_id = models.ForeignKey("tbl_company_mst", default=0, verbose_name="Company Ref Id", on_delete=models.PROTECT)
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")  

    class Meta:
        verbose_name_plural = "tbl_role_mst"

class tbl_country_mst(models.Model):
    share_id = models.IntegerField(default=0,verbose_name='Share ID')
    name = models.CharField(max_length=20,verbose_name='Name')
    short_name = models.CharField(max_length=20,verbose_name='Short Name')
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")

    class Meta:
        verbose_name_plural = "tbl_country_mst"

class tbl_state_mst(models.Model):
    share_id =  models.IntegerField(default=0,verbose_name='Share ID')
    country_id = models.ForeignKey("tbl_country_mst", on_delete=models.PROTECT, verbose_name='Country ID', related_name='states')
    state = models.CharField(max_length=20, verbose_name='State')
    gst_state_code = models.IntegerField(default=0)
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")

    def __str__(self):
        return self.state
    
    class Meta:
        verbose_name_plural = "tbl_state_mst"

class tbl_city_mst(models.Model):
    share_id =  models.IntegerField(default=0,verbose_name='Share ID')
    state_id = models.ForeignKey("tbl_state_mst", on_delete=models.PROTECT, verbose_name='State ID', related_name='cities')
    city_name = models.CharField(max_length=20,verbose_name='City Name')
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")

    class Meta:
        verbose_name_plural = "tbl_city_mst"

class tbl_location_mst(models.Model):
    share_id = models.IntegerField(default=0,verbose_name='Share ID')
    city_id = models.ForeignKey("tbl_city_mst", on_delete=models.PROTECT, verbose_name='City ID', related_name='locations')
    state_id = models.ForeignKey("tbl_state_mst", on_delete=models.PROTECT, verbose_name='State ID')
    country_id = models.ForeignKey("tbl_country_mst", on_delete=models.PROTECT, verbose_name='Country ID')
    location_name = models.CharField(max_length=20,verbose_name='Location Name')
    address1 = models.TextField(verbose_name='Address Line 1')
    address2 = models.TextField(verbose_name='Address Line 2')
    address3 = models.TextField(verbose_name='Address Line 3')
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")

    class Meta:
        verbose_name_plural = "tbl_location_mst"
        constraints = [
           models.UniqueConstraint(fields = ['location_name'], condition=models.Q(is_deleted = 'N'), name='unique if not deleted')
       ]

    def delete(self):
        self.is_deleted = 'Y'
        self.save()

class tbl_currency_mst(models.Model):
    share_id = models.IntegerField(default=0,verbose_name='Share ID')
    currency_code = models.CharField(max_length=10,verbose_name='Currency Code',null=False)
    currency_name = models.CharField(max_length=30, verbose_name='Currency Name')
    symbol = models.CharField(max_length=20,verbose_name='Symbol')
    country_id = models.ForeignKey('tbl_country_mst',on_delete=models.PROTECT,related_name='currency')
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")

    class Meta:
        verbose_name_plural = "tbl_currency_mst"
        constraints = [
            models.UniqueConstraint(fields=['country_id'],condition=models.Q(is_deleted='N'),name='unique_if_not_deleted'),
            models.UniqueConstraint(fields=['currency_code'],condition=models.Q(is_deleted='N'),name='unique_if_not'),
        ]     

class tbl_reason_mst(models.Model):
    share_id = models.IntegerField(default=0,verbose_name='Share ID')
    rej_reason_code = models.CharField(max_length=20,verbose_name='Rejection Reason Code')
    rej_reason = models.TextField(verbose_name='Rejection Reason')
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")    

    class Meta:
        verbose_name_plural = "tbl_reason_mst"

class tbl_company_mst(models.Model):
    company_id = models.IntegerField(default=0,verbose_name='Company ID',unique=True)
    share_id  = models.IntegerField(default=0,verbose_name='Share ID')
    entity_share_id = models.TextField(default=0,verbose_name='Entity Share ID')
    company_name = models.CharField(max_length=30,verbose_name='Company Name')
    company_shortname = models.CharField( default=0,max_length=30,verbose_name='Company Short Name')
    address1 = models.CharField(default=0,max_length=30,verbose_name='Address Line 1')
    address2 = models.CharField(default=0,max_length=30,verbose_name='Address Line 2')
    address3 = models.CharField(default=0,max_length=30,verbose_name='Address Line 3')
    country_ref_id =  models.ForeignKey("tbl_country_mst",verbose_name="Country Ref ID",on_delete=models.PROTECT,blank=True, null=True)
    state_ref_id =  models.ForeignKey("tbl_state_mst", default=0,verbose_name="State Ref ID",on_delete=models.PROTECT,blank=True, null=True)
    city_ref_id =  models.ForeignKey("tbl_city_mst", default=0,verbose_name="City Ref ID",on_delete=models.PROTECT,blank=True, null=True)
    location_ref_id = models.ForeignKey("tbl_location_mst", default=0,verbose_name="Location Ref ID",on_delete=models.PROTECT)
    company_type_ref_id = models.ForeignKey("tbl_master", default=1,verbose_name="Company Type Ref ID",on_delete=models.PROTECT,related_name="company_type")
    ownership_status_ref_id =  models.ForeignKey("tbl_master", default=0,verbose_name="Ownership Status Ref ID",on_delete=models.PROTECT)
    cin = models.CharField(default=0,max_length=21,verbose_name='CIN',blank=True, null=True)
    pan = models.CharField(default=0,max_length=15,verbose_name='PAN')
    tan = models.CharField(default=0,max_length=15,verbose_name='TAN')
    gst = models.CharField(default=0,max_length=15,verbose_name='GST No.')
    email = models.EmailField(blank=True,verbose_name='Email') 
    contact_person_name = models.CharField(default=0,max_length=30,verbose_name='Contact Person Name')
    currency_id = models.ForeignKey(tbl_currency_mst, on_delete=models.PROTECT, blank=True, null=True,verbose_name='Currency Ref Id')
    is_holding_company = models.BooleanField(default=False,blank=True, null=True,verbose_name='Is Holding Company')
    belongs_to_company_id = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True, related_name='belongs_to')
    is_this_under_same_management = models.BooleanField(default=False,blank=True, null=True,verbose_name='Is This Under Same Management?')
    management_belongs_to_company_id = models.ForeignKey('self', on_delete=models.PROTECT,blank=True, null=True, related_name='managed_by')
    percentage_holding = models.FloatField(default=0.0000,verbose_name='Percentage Holding')
    is_group_company = models.BooleanField(default=False,blank=True, null=True,verbose_name='Is Group Company')
    contact_person_mobile_number = models.CharField(null=True,max_length=30,verbose_name='Contact Person Mobile No.')
    is_this_branch = models.BooleanField(default=False,blank=True, null=True,verbose_name='Is This Branch?')
    pincode = models.CharField(default=0,max_length=8,verbose_name='Pincode')
    revision_status = models.CharField(default='None',max_length=20,verbose_name="Revision Status")
    attach_document= models.CharField(max_length=500,blank=True, null=True,verbose_name='Attach Document')
    bank_name = models.CharField(max_length=30,blank=True, null=True,verbose_name='Bank Name')
    bank_account = models.CharField(max_length=35, validators=[RegexValidator(r'^\d{9,26}$')],blank=True, null=True,verbose_name='Bank Account')
    ifsc_code = models.CharField(max_length=30,blank=True, null=True,verbose_name='IFSC Code')
    comments = models.CharField(max_length=30,blank=True, null=True,verbose_name='Comments')
    kyc_document_ref_id = models.CharField(default='N',max_length=200,verbose_name="Key Document Ref Id")
    is_company = models.CharField(default='N',max_length=1,verbose_name='Is Company')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")

    class Meta:
        verbose_name_plural = "tbl_company_mst"
        constraints = [
            models.UniqueConstraint(fields = ['company_name'], condition=models.Q(is_deleted = 'N'), name='unique in company name not deleted'),
            models.UniqueConstraint(fields = ['pan'], condition=models.Q(is_deleted = 'N'), name='unique in company pan not deleted')
       ]
        
class tbl_company_contact_details(models.Model):
    header_ref_id = models.ForeignKey("tbl_company_mst", default=0,verbose_name="Header Ref ID",on_delete=models.PROTECT,related_name='initialItemRow')
    contact_person_name = models.CharField(max_length=30,verbose_name='Contact Person Name')
    designation = models.CharField(max_length=30,null=True,blank=True,verbose_name='Contact Person Des')
    contact_person_mobile_number = models.CharField(max_length=30,verbose_name='Contact Person Number')
    email = models.EmailField(max_length=30,verbose_name='Email')
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")

    class Meta:
        verbose_name_plural = "tbl_company_contact_details"

class tbl_master(models.Model):
    share_id = models.IntegerField(default=0,verbose_name='Share ID')
    master_type = models.CharField(max_length=50,verbose_name='Master Type')
    master_value = models.CharField(max_length=20,verbose_name='Master Value')
    master_key = models.CharField(max_length=20,verbose_name='Master Key')
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")

    class Meta:
        verbose_name_plural = "tbl_master"

class tbl_calendar_mst(models.Model):
    share_id =  models.IntegerField(default=0,verbose_name='Share ID')
    calendar_type_id = models.IntegerField(default=0,verbose_name='Calendar Type ID')
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")

    class Meta:
        verbose_name_plural = "tbl_calendar_mst"

class tbl_calendar_details(models.Model):
    header_ref_id = models.ForeignKey("tbl_calendar_mst", default=0,verbose_name="Header Ref ID",on_delete=models.PROTECT,related_name='initialItemRow')
    year = models.CharField(max_length=4,verbose_name='Year')
    period = models.CharField(max_length=2,verbose_name='Period')
    start_date = models.DateField(verbose_name='Start Date')
    end_date = models.DateField(verbose_name='End Date')
    month = models.CharField(max_length=10,verbose_name='Month')
    status = models.TextField(verbose_name='Status')
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")

    class Meta:
        verbose_name_plural = "tbl_calendar_details"

class tbl_term_mst(models.Model):
    share_id = models.IntegerField(default=0,verbose_name='Share ID')
    term_code = models.CharField(max_length=10,verbose_name='Term Code')
    term_description = models.TextField(verbose_name='Term Description')
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")

    class Meta:
        verbose_name_plural = "tbl_term_mst"
        constraints = [
            models.UniqueConstraint(fields = ['term_code'], condition=models.Q(is_deleted = 'N'), name='unique in term not deleted')
       ]
        
class tbl_employee_mst(models.Model):
    first_name = models.CharField(max_length=15,verbose_name='First name')
    middle_name = models.CharField(max_length=15, blank=True, null=True, verbose_name='Middle name')
    last_name = models.CharField(max_length=15,verbose_name='Last name')
    company_ref_id = models.ForeignKey("tbl_company_mst", default=0, verbose_name="Company Ref Id", on_delete=models.PROTECT)
    company_type_ref_id = models.ForeignKey("tbl_master", default=1,verbose_name="Company Type Ref ID",on_delete=models.PROTECT,related_name="employee_company_type")
    employee_seq_no = models.CharField(max_length=40,verbose_name='Employee Seq No')
    role_ref_id = models.ForeignKey("tbl_role_mst", default=0, verbose_name="Role Ref Id", on_delete=models.PROTECT)
    email = models.EmailField(max_length=30,verbose_name='Email')
    password = models.CharField(max_length=20,verbose_name='Password')
    phone = models.CharField(max_length=10,verbose_name='Phone Number')
    pincode = models.CharField(max_length=6,verbose_name='Pincode')
    address1 = models.CharField(max_length=200,verbose_name='Address 1')
    address2 = models.CharField(max_length=200,verbose_name='Address 2')
    address3 = models.CharField(max_length=200,verbose_name='Address 3')
    city_ref_id = models.ForeignKey("tbl_city_mst", on_delete=models.PROTECT, verbose_name='City ID')
    state_ref_id = models.ForeignKey("tbl_state_mst", on_delete=models.PROTECT, verbose_name='State ID')
    country_ref_id = models.ForeignKey("tbl_country_mst", on_delete=models.PROTECT, verbose_name='Country ID')
    gender = models.CharField(max_length=10,verbose_name='Gender')
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")

    class Meta:
        verbose_name_plural = "tbl_employee_mst"

class tbl_user_mst(models.Model):
    first_name = models.CharField(max_length=15,verbose_name='First name')
    middle_name = models.CharField(max_length=15, blank=True, null=True, verbose_name='Middle name')
    last_name = models.CharField(max_length=15,verbose_name='Last name')
    user_seq_no = models.CharField(max_length=40,verbose_name='User Seq No')
    role_ref_id = models.ForeignKey("tbl_role_mst", default=0, verbose_name="Role Ref Id", on_delete=models.PROTECT)
    company_ref_id = models.ForeignKey("tbl_company_mst", default=0, verbose_name="Company Ref Id", on_delete=models.PROTECT)
    email = models.EmailField(max_length=30,verbose_name='Email')
    password = models.CharField(max_length=20,verbose_name='Password')
    phone = models.CharField(max_length=10,verbose_name='Phone Number')
    gender = models.CharField(max_length=10,verbose_name='Gender')
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")

    class Meta:
        verbose_name_plural = "tbl_user_mst"

class tbl_channel_mst(models.Model):
    share_id = models.IntegerField(default=0,verbose_name='Share ID')
    channel_name = models.CharField(default=0,max_length=100,verbose_name='Channel name')
    channel_description = models.CharField(default=0,max_length=100,verbose_name='Channel Description')
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")

    class Meta:
        verbose_name_plural = "tbl_channel_mst"
        constraints = [
           models.UniqueConstraint(fields = ['channel_name'], condition=models.Q(is_deleted = 'N'), name='unique if channel name not deleted')
       ]
        
class tbl_service_asset_mst(models.Model): # tbl_application_mst is renamed to tbl_service_asset_mst
    share_id = models.IntegerField(default=0,verbose_name='Share ID')
    name = models.CharField(default=0,max_length=100,verbose_name='name') # application_name is renamed to name
    description = models.CharField(default=0,max_length=100,verbose_name='Description') # application_description is renamed to description
    priority_ref_id = models.ForeignKey("tbl_master", default=1,verbose_name="Priority Ref ID",on_delete=models.PROTECT)
    asset_ref_id = models.ForeignKey("tbl_asset_mst", null = True , blank =  True,verbose_name="Asset Ref ID",on_delete=models.PROTECT)
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")

    class Meta:
        verbose_name_plural = "tbl_service_asset_mst"
        constraints = [
           models.UniqueConstraint(fields = ['name'], condition=models.Q(is_deleted = 'N'), name='unique if application name not deleted')
       ] 

class tbl_ticket_type_mst(models.Model):
    share_id = models.IntegerField(default=0,verbose_name='Share ID')
    ticket_name = models.CharField(default=0,max_length=50,verbose_name='Ticket name')
    ticket_description = models.CharField(default=0,max_length=100,verbose_name='Ticket Description')
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")

    class Meta:
        verbose_name_plural = "tbl_ticket_type_mst"
        constraints = [
           models.UniqueConstraint(fields = ['ticket_name'], condition=models.Q(is_deleted = 'N'), name='unique if ticket name not deleted')
       ]

class tbl_message_mst(models.Model):
    share_id = models.IntegerField(default=0,verbose_name='Share ID')
    name = models.CharField(max_length=200,verbose_name='API Name')
    description = models.CharField(default=0,max_length=200,verbose_name='Description')
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")   

    class Meta:
        verbose_name_plural = "tbl_message_mst"
        constraints = [
           models.UniqueConstraint(fields = ['name'], condition=models.Q(is_deleted = 'N'), name='tbl_message_mst unique if not deleted')
       ]

class tbl_company_application_link_mst(models.Model):
    share_id = models.IntegerField(default=0,verbose_name='Share ID')
    name = models.CharField(max_length=200,verbose_name='API Name')
    description = models.CharField(default=0,max_length=200,verbose_name='Description')
    company_ref_id = models.ForeignKey("tbl_company_mst",verbose_name="Company Ref Id", on_delete=models.PROTECT)
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")   

    class Meta:
        verbose_name_plural = "tbl_company_application_link_mst"
        constraints = [
           models.UniqueConstraint(fields = ['name'], condition=models.Q(is_deleted = 'N'), name='tbl_company_application_link_mst unique if not deleted')
       ]

class tbl_company_application_link_details(models.Model):
    header_ref_id = models.ForeignKey("tbl_company_application_link_mst", default=0,verbose_name="Header Ref ID",on_delete=models.PROTECT,related_name='initialItemRow')
    application_ref_id = models.ForeignKey("tbl_service_asset_mst", verbose_name="Application Ref Id", on_delete=models.PROTECT)
    channel_ref_id = models.ForeignKey("tbl_channel_mst", verbose_name="Channel Ref Id", on_delete=models.PROTECT)
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID") 

    class Meta:
        verbose_name_plural = "tbl_company_application_link_details"

class tbl_ticket_status_mst(models.Model):
    share_id = models.IntegerField(default=0,verbose_name='Share ID')
    name = models.CharField(default=0,max_length=50,verbose_name='Name')
    description = models.CharField(default=0,max_length=100,verbose_name='Description')
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")

    class Meta:
        verbose_name_plural = "tbl_ticket_status_mst"

class tbl_sla_mst(models.Model):
    share_id = models.IntegerField(default=0,verbose_name='Share ID')
    name = models.CharField(max_length=200,verbose_name='API Name')
    description = models.CharField(default=0,max_length=200,verbose_name='Description')
    company_ref_id = models.ForeignKey("tbl_company_mst",verbose_name="Company Ref Id", on_delete=models.PROTECT)
    from_date = models.DateField(verbose_name="From Date",auto_now_add=False)
    to_date = models.DateField(verbose_name="To Date",auto_now_add=False)
    revision_status = models.CharField(max_length=20,verbose_name="Revision Status")
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")   

    class Meta:
        verbose_name_plural = "tbl_sla_mst"
        constraints = [
           models.UniqueConstraint(fields = ['name'], condition=models.Q(is_deleted = 'N'), name='tbl_sla_mst unique if not deleted')
       ]

class tbl_sla_details(models.Model):
    header_ref_id = models.ForeignKey("tbl_sla_mst", default=0,verbose_name="Header Ref ID",on_delete=models.PROTECT,related_name='initialItemRow')
    application_ref_id = models.ForeignKey("tbl_service_asset_mst", verbose_name="Application Ref Id", on_delete=models.PROTECT)
    ticket_type_ref_id = models.ForeignKey("tbl_ticket_type_mst", verbose_name="Ticket Type Ref Id", on_delete=models.PROTECT)
    priority_ref_id = models.ForeignKey("tbl_master", default=65,verbose_name="Priority Ref ID",on_delete=models.PROTECT)
    response_time =  models.DecimalField(default=0,max_digits=15,decimal_places=2,verbose_name="Response Time")
    resolution_time =  models.DecimalField(default=0,max_digits=15,decimal_places=2,verbose_name="Resolution Time")
    escalation_time =  models.DecimalField(default=0,max_digits=15,decimal_places=2,verbose_name="Escalation Time")
    availability_percentage = models.IntegerField(default=0,verbose_name="availability_percentage")
    down_time =  models.DecimalField(default=0,max_digits=15,decimal_places=2,verbose_name="Down Time")
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID") 

    class Meta:
        verbose_name_plural = "tbl_sla_details"

class tbl_company_priority_link_mst(models.Model):
    share_id = models.IntegerField(default=0,verbose_name='Share ID')
    company_ref_id = models.ForeignKey("tbl_company_mst",verbose_name="Company Ref Id", on_delete=models.PROTECT)
    from_date = models.DateField(verbose_name="From Date",auto_now_add=False)
    to_date = models.DateField(verbose_name="To Date",auto_now_add=False)
    revision_status = models.CharField(max_length=20,verbose_name="Revision Status")
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")   

    class Meta:
            verbose_name_plural = "tbl_company_priority_link_mst"

class tbl_company_priority_link_details(models.Model):
    header_ref_id = models.ForeignKey("tbl_company_priority_link_mst", default=0,verbose_name="Header Ref ID",on_delete=models.PROTECT,related_name='initialItemRow')
    priority_ref_id = models.ForeignKey("tbl_master", default=1,verbose_name="Priority Ref ID",on_delete=models.PROTECT)
    response_time =  models.DecimalField(default=0,max_digits=15,decimal_places=2,verbose_name="Response Time")
    resolution_time =  models.DecimalField(default=0,max_digits=15,decimal_places=2,verbose_name="Resolution Time")
    escalation_time =  models.DecimalField(default=0,max_digits=15,decimal_places=2,verbose_name="Escalation Time")
    availability_percentage = models.IntegerField(default=0,verbose_name="availability_percentage")
    down_time =  models.DecimalField(default=0,max_digits=15,decimal_places=2,verbose_name="Down Time")
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")   

    class Meta:
            verbose_name_plural = "tbl_company_priority_link_details"

class tbl_role_application_mst(models.Model):
    share_id = models.IntegerField(default=0,verbose_name='Share ID')
    company_ref_id = models.ForeignKey("tbl_company_mst",verbose_name="Company Ref Id", on_delete=models.PROTECT)
    role_ref_id = models.ForeignKey("Tbl_Role_Mst",verbose_name="Role Ref Id", on_delete=models.PROTECT)
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")   

    class Meta:
        verbose_name_plural = "tbl_role_application_mst"

class tbl_role_application_details(models.Model):
    header_ref_id = models.ForeignKey("tbl_role_application_mst",default=0,verbose_name="Header Ref ID",on_delete=models.PROTECT,related_name='initialItemRow')
    application_ref_id = models.ForeignKey("tbl_service_asset_mst", verbose_name="Application Ref Id", on_delete=models.PROTECT)
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID") 

    class Meta:
        verbose_name_plural = "tbl_role_application_details"

class tbl_workflow_activity_mst(models.Model):
    activity_name = models.CharField(max_length=200,verbose_name='Activity name')
    activity_description = models.CharField(max_length=200,verbose_name='Activity Description')
    workflow_type_ref_id = models.ForeignKey("tbl_master", null = True , blank= True , verbose_name="Workflow Type Ref Id", on_delete=models.PROTECT)
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")

    class Meta:
        verbose_name_plural = "tbl_workflow_activity_mst"

class tbl_workflow_action_mst(models.Model):
    action_name = models.CharField(max_length=15,verbose_name='Action name')
    action_description = models.CharField(max_length=15,verbose_name='Action Description')
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")  

    class Meta:
        verbose_name_plural = "tbl_workflow_action_mst"

class tbl_workflow_routing_mst(models.Model):
    workflow_routing_name = models.CharField(default='N',max_length=15,verbose_name='Workflow Routing Name')
    workflow_routing_desc = models.CharField(default='N',max_length=100,verbose_name='Workflow Routing Desc')
    version_number = models.IntegerField(default=0,verbose_name='Version Number')
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID") 

    class Meta:
        verbose_name_plural = "tbl_workflow_routing_mst"

class tbl_workflow_routing_details(models.Model):
    header_ref_id = models.ForeignKey("tbl_workflow_routing_mst", default=0,verbose_name="Workflow Routing Ref ID",on_delete=models.CASCADE,related_name='initialItemRow')
    sequence_number = models.IntegerField(default=0,verbose_name='Sequence Number')
    next_sequence_number = models.IntegerField(default=0,verbose_name='Next Sequence Number')
    workflow_ref_id = models.ForeignKey("tbl_workflow_mst", verbose_name="Workflow Ref ID",on_delete=models.CASCADE)
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted") 
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")

    class Meta:
        verbose_name_plural = "tbl_workflow_routing_details"

class tbl_workflow_level_data_mst(models.Model):
    share_id = models.IntegerField(default=0,verbose_name='Share ID')
    workflow_type_ref_id = models.ForeignKey("tbl_master", default=0, verbose_name="Workflow Type Ref Id", on_delete=models.PROTECT)
    level = models.IntegerField(default=0,verbose_name='Level')
    level_name = models.CharField(max_length=50,default=0,verbose_name='Level Name')
    activity_sequence = models.CharField(max_length=50,default=0,verbose_name='Activity Sequence')
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")    

    class Meta:
        verbose_name_plural = "tbl_workflow_level_data_mst"
        constraints = [
            models.UniqueConstraint(fields=['activity_sequence'],condition=models.Q(is_deleted='N'),name='unique_if_not_deleted_level')
        ]

class tbl_workflow_level_data_details(models.Model):
    header_ref_id = models.ForeignKey("tbl_workflow_level_data_mst", default=0,verbose_name="Header Ref ID",on_delete=models.CASCADE,related_name='initialItemRow')
    activity_ref_id = models.ForeignKey("tbl_workflow_activity_mst", default=0, verbose_name="Activity Ref Id", on_delete=models.PROTECT)
    sequence_number = models.IntegerField(default=0,verbose_name="Sequence Number")
    action_ref_id =  models.ForeignKey("tbl_workflow_action_mst", default=0, verbose_name="Action Ref Id", on_delete=models.PROTECT)
    next_sequence_number = models.IntegerField(default=0,verbose_name="Next Sequence Number")
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")    

    class Meta:
        verbose_name_plural = "tbl_workflow_level_data_details"

class tbl_workflow_mst(models.Model):
    share_id = models.IntegerField(default=0,verbose_name='Share ID')
    company_ref_id = models.ForeignKey("tbl_company_mst", default=0, verbose_name="Company Ref Id", on_delete=models.PROTECT)
    service_asset_ref_id = models.ForeignKey("tbl_service_asset_mst", default=2, verbose_name="Service Asset Ref Id", on_delete=models.PROTECT)
    resolution_time =  models.DecimalField(default=0,max_digits=15,decimal_places=2,verbose_name="Resolution Time", blank=True,null = True)
    workflow_type_ref_id = models.ForeignKey("tbl_master", default=0, verbose_name="Workflow Type Ref Id", on_delete=models.PROTECT)
    level_ref_id = models.ForeignKey("tbl_workflow_level_data_mst", default=0, verbose_name="Level Ref Id", on_delete=models.PROTECT)
    level_name = models.CharField(max_length=50,null=True , blank= True,verbose_name='Level Name') #Used when Workflow Type is 'Task'.
    workflow_name = models.CharField(max_length=50,verbose_name='Workflow name')
    workflow_description = models.CharField(max_length=100,verbose_name='Workflow Description')
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")

    class Meta:
        verbose_name_plural = "tbl_workflow_mst"

class tbl_workflow_details(models.Model):
    header_ref_id = models.ForeignKey("tbl_workflow_mst", default=0,verbose_name="Header Ref ID",on_delete=models.CASCADE,related_name='initialItemRow')
    level_details_ref_id = models.ForeignKey("tbl_workflow_level_data_mst",null=True , blank= True,verbose_name="Level Details Ref Id", on_delete=models.PROTECT)
    level_details_name = models.CharField(max_length=50,null=True , blank= True,verbose_name='Level Name') #Used when Workflow Type is 'Process'.
    left_panel_ref_id = models.ForeignKey("tbl_left_panel", null=True , blank= True,verbose_name="Screen", on_delete=models.PROTECT)
    field_name = models.CharField(max_length=100,null=True , blank= True,verbose_name='Database Field name')
    approval_field_value = models.DecimalField(default=0,max_digits=15,decimal_places=4,null=True ,blank= True,verbose_name="Approval Field Value")
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")

    class Meta:
        verbose_name_plural = "tbl_workflow_details"

class tbl_workflow_sub_details(models.Model):
    header_ref_id = models.ForeignKey("tbl_workflow_mst", default=0,verbose_name="Header Ref ID",on_delete=models.CASCADE,related_name='initialItemRow2')
    details_ref_id = models.ForeignKey("tbl_workflow_details", default=0,verbose_name="Details Ref ID",on_delete=models.PROTECT,related_name='initialItemRow3')
    company_ref_id = models.ForeignKey("tbl_company_mst", default=0, verbose_name="Company Ref Id", on_delete=models.PROTECT,null=True , blank= True)
    level_sub_details_ref_id = models.ForeignKey("tbl_workflow_level_data_mst", default=0, verbose_name="Sub Details Ref Id", on_delete=models.PROTECT)
    role_ref_id = models.ForeignKey("Tbl_Role_Mst",verbose_name="Role Ref Id", on_delete=models.PROTECT,null=True , blank= True)
    employee_ref_id = models.ForeignKey("tbl_employee_mst", verbose_name="Employee Ref Id", on_delete=models.PROTECT,null=True , blank= True)
    activity_ref_id = models.ForeignKey("tbl_workflow_activity_mst", default=0, verbose_name="Activity Ref Id", on_delete=models.PROTECT)
    sequence_number = models.IntegerField(default=0,verbose_name="Sequence Number")
    action_ref_id =  models.ForeignKey("tbl_workflow_action_mst", default=0, verbose_name="Action Ref Id", on_delete=models.PROTECT)
    next_sequence_number = models.IntegerField(default=0,verbose_name="Next Sequence Number")
    is_email_required = models.BooleanField(blank=True,null = True)
    is_whatsapp_required = models.BooleanField(blank=True,null = True)
    is_sms_required = models.BooleanField(blank=True,null = True)
    is_reminder_required = models.BooleanField(blank=True,null = True)
    is_worklist_required = models.BooleanField(blank=True,null = True)
    #sla_days = models.IntegerField(default=0, verbose_name="Escalation Days")
    sla_response_time =  models.DecimalField(default=0,max_digits=15,decimal_places=2,verbose_name="Response Time",blank=True,null = True)
    reminder_days = models.IntegerField(default=0, verbose_name="Reminder Days Ref Id")
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")

    class Meta:
        verbose_name_plural = "tbl_workflow_sub_details"

class tbl_workflow_activity(models.Model):
    share_id = models.IntegerField(default=0,verbose_name='Share ID')
    workflow_ref_id = models.ForeignKey("tbl_workflow_mst",verbose_name='Step Ref Id',on_delete=models.PROTECT)
    screen_name = models.CharField(default='SCREEN NAME',max_length=30,verbose_name='Screen Name')
    form_ref_id = models.IntegerField(default=0,verbose_name='Form Ref Id')
    level = models.CharField(max_length=30,verbose_name='Level')
    is_assigned_role_person = models.CharField(default='Y',max_length=1,verbose_name='Is Assigned Role Person')
    assigned_role = models.CharField(max_length=30,verbose_name='Assigned Role', blank=True,null = True)
    assigned_person = models.CharField(max_length=30,verbose_name='Assigned Person')
    activity_ref_id = models.ForeignKey("tbl_workflow_activity_mst",verbose_name="Activity Ref ID",on_delete=models.PROTECT)
    action_ref_id = models.ForeignKey("tbl_workflow_action_mst",verbose_name="Action Ref ID",on_delete=models.PROTECT)
    sequence_number  = models.IntegerField(default=0,verbose_name='Sequence Number')
    next_sequence_number  = models.IntegerField(default=0,verbose_name='Next Sequence Number')
    user_action_ref_id  = models.ForeignKey("tbl_workflow_action_mst", blank=True,null = True, verbose_name="User Action Ref ID",on_delete=models.PROTECT,related_name='user_action_ref_id')
    status = models.CharField(max_length=20,verbose_name='Status')
    sla = models.IntegerField(default=0, verbose_name="SLA")
    actual_response_time = models.DecimalField(default=0,max_digits=15,decimal_places=2,verbose_name="Actual Response Time")
    actual_resolution_time = models.DecimalField(default=0,max_digits=15,decimal_places=2,verbose_name="Actual Resolution Time")
    start_date_time = models.DateTimeField(null=True,verbose_name="Start Date Time")
    end_date_time = models.DateTimeField(null=True,verbose_name="End Date Time")
    escalation_date_time = models.DateTimeField(null=True,verbose_name="Escalation Date Time")
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")                   

    class Meta:
        verbose_name_plural = "tbl_workflow_activity"

class tbl_workflow_activity_notification_details(models.Model):    
    header_ref_id = models.ForeignKey("tbl_workflow_activity", default=0,verbose_name="Header Ref ID",on_delete=models.CASCADE,related_name='workflowactivity_not')
    is_notification_applicable = models.CharField(default='N',max_length=1,verbose_name='Is Notification Applicable')
    is_email = models.CharField(default='N',max_length=1,verbose_name='Is Email')
    is_text_message = models.CharField(default='N',max_length=1,verbose_name='Is Text Message')
    is_whatsapp = models.CharField(default='N',max_length=1,verbose_name='Is Wahtsapp')
    is_additional_email = models.CharField(default='N',max_length=1,verbose_name='Is Add Email')
    is_additional_text_message = models.CharField(default='N',max_length=1,verbose_name='Is Add Message')
    is_additional_watsapp = models.CharField(default='N',max_length=1,verbose_name='Is Add Wahtsapp')
    is_additional_notification_to_senior_management = models.CharField(default='N',max_length=1,verbose_name='Is Add to Senior')
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")   

    class Meta:
        verbose_name_plural = "tbl_workflow_activity_notification_details"

class tbl_workflow_activity_notification_log(models.Model):    
    header_ref_id = models.ForeignKey("tbl_workflow_activity", default=0,verbose_name="Header Ref ID",on_delete=models.CASCADE,related_name='initialItemRow')
    details_ref_id = models.ForeignKey("tbl_workflow_activity_notification_details", default=0,verbose_name="Header Ref ID",on_delete=models.CASCADE,related_name='initialItemRow')
    type_of_notification = models.CharField(max_length=20,default=0,verbose_name='Type of Notification')
    status = models.CharField(max_length=20,verbose_name='Status')
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")      

    class Meta:
        verbose_name_plural = "tbl_workflow_activity_notification_log"

class tbl_workflow_routing_activity(models.Model):
    workflow_routing_ref_id = models.ForeignKey("tbl_workflow_routing_mst",verbose_name="Routing Ref ID",on_delete=models.PROTECT)
    workflow_routing_details_ref_id = models.ForeignKey("tbl_workflow_routing_details",verbose_name="Routing Ref ID",on_delete=models.PROTECT)
    sequence_number  = models.IntegerField(default=0,verbose_name='Sequence Number')
    next_sequence_number  = models.IntegerField(default=0,verbose_name='Next Sequence Number')
    status = models.CharField(max_length=20,verbose_name='Status')
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")  

    class Meta:
        verbose_name_plural = "tbl_workflow_routing_activity"

class File(models.Model):
    issue_mst_ref_id = models.ForeignKey("tbl_issue_mst",verbose_name="Issue Mst Ref Id", on_delete=models.PROTECT,blank=True, null=True)
    issue_details_ref_id = models.ForeignKey("tbl_issue_details",verbose_name="Issue Details Ref Id", on_delete=models.PROTECT,blank=True, null=True)
    file = models.FileField(blank=True, null=True)
    def __str__(self):
        return self.file.name

    class Meta:
        verbose_name_plural = "File"

class tbl_issue_mst(models.Model):
    share_id = models.IntegerField(default=0,verbose_name='Share ID')
    company_ref_id = models.ForeignKey("tbl_company_mst", default=0, verbose_name="Company Ref Id", on_delete=models.PROTECT)
    reported_by = models.ForeignKey("tbl_employee_mst", verbose_name="Reported By", on_delete=models.PROTECT, related_name="reported_by")
    is_it_employee_flag = models.CharField(default='N',max_length=1,verbose_name='Is it Employee Flag')
    assigned_to_ref_id = models.ForeignKey("tbl_employee_mst", default=0, verbose_name="Assigned To Ref Id", on_delete=models.PROTECT,null = True ,blank= True)
    service_asset_ref_id = models.ForeignKey("tbl_service_asset_mst", verbose_name="Service Asset Ref Id", on_delete=models.PROTECT)
    priority_ref_id =models.ForeignKey("tbl_master", default=0, verbose_name="Priority Ref Id", on_delete=models.PROTECT,related_name="issue_priority_ref")
    ticket_type_ref_id = models.ForeignKey("tbl_ticket_type_mst", default=0, verbose_name="Ticket Type Ref Id", on_delete=models.PROTECT)
    impact_ref_id = models.ForeignKey("tbl_master", default=0, verbose_name="Impact Ref Id", on_delete=models.PROTECT)
    impact_on = models.CharField(max_length=100,null=True , blank= True,verbose_name='Impact On')
    status_ref_id = models.ForeignKey("tbl_ticket_status_mst", default=0, verbose_name="Status Ref Id", on_delete=models.PROTECT,related_name="issue_status_ref")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    form = models.CharField(max_length=100,null=True , blank= True,verbose_name='Form')
    closed_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Closed Date Time")
    closed_by = models.IntegerField(default=0,verbose_name="Closed By",null = True ,blank= True)
    is_converted_flag = models.CharField(default='N',max_length=1,verbose_name='Is Converted Flag')
    conversion_ticket_type_ref_id = models.ForeignKey("tbl_ticket_type_mst", verbose_name="C Ticket Type Ref Id", on_delete=models.PROTECT,null = True , blank = True,related_name='converted_ticket')
    converted_issue_ref_id = models.IntegerField(default=0,verbose_name='Converted Issue Ref Id',null = True , blank = True)
    converted_problem_ref_id =  models.ForeignKey("tbl_problem_issue_mst", verbose_name="Problem Ref ID",on_delete=models.CASCADE,blank=True,null = True)
    total_resolution_time = models.DecimalField(default=0,max_digits=15,decimal_places=2,verbose_name="Resolution Time",blank=True,null = True)
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")

    class Meta:
        verbose_name_plural = "tbl_issue_mst"

class tbl_issue_details(models.Model):
    header_ref_id = models.ForeignKey("tbl_issue_mst", default=0,verbose_name="Header Ref ID",on_delete=models.CASCADE,related_name='initialItemRow')
    title = models.CharField(max_length=100,verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    attach_document= models.CharField(max_length=500,blank=True, null=True,verbose_name='Attach Document')
    is_it_original_entry_flag = models.CharField(default='N',max_length=1,verbose_name='Is it Original Entry Flag')
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")

    class Meta:
        verbose_name_plural = "tbl_issue_details"

class tbl_problem_issue_mst(models.Model):
    share_id = models.IntegerField(default=0,verbose_name='Share ID')
    company_ref_id = models.ForeignKey("tbl_company_mst", default=0, verbose_name="Company Ref Id", on_delete=models.PROTECT)
    issue_ref_id = models.ForeignKey("tbl_issue_mst", verbose_name="Issue Ref Id", on_delete=models.PROTECT)
    reported_by = models.ForeignKey("tbl_employee_mst", verbose_name="Reported By", on_delete=models.PROTECT, related_name="problem_reported_by")
    assigned_to_ref_id = models.ForeignKey("tbl_employee_mst", default=0, verbose_name="Assigned To Ref Id", on_delete=models.PROTECT,null = True ,blank= True)
    service_asset_ref_id = models.ForeignKey("tbl_service_asset_mst", verbose_name="Service Asset Ref Id", on_delete=models.PROTECT)
    priority_ref_id =models.ForeignKey("tbl_master", default=0, verbose_name="Priority Ref Id", on_delete=models.PROTECT,related_name="problem_issue_priority_ref")
    ticket_type_ref_id = models.ForeignKey("tbl_ticket_type_mst", default=0, verbose_name="Ticket Type Ref Id", on_delete=models.PROTECT)
    impact_ref_id = models.ForeignKey("tbl_master", default=0, verbose_name="Impact Ref Id", on_delete=models.PROTECT)
    impact_on = models.CharField(max_length=100,null=True , blank= True,verbose_name='Impact On')
    status_ref_id = models.ForeignKey("tbl_ticket_status_mst", default=0, verbose_name="Status Ref Id", on_delete=models.PROTECT,related_name="problem_issue_status_ref")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    form = models.CharField(max_length=100,null=True , blank= True,verbose_name='Form')
    closed_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Closed Date Time")
    closed_by = models.IntegerField(default=0,verbose_name="Closed By",null = True ,blank= True)
    total_resolution_time = models.DecimalField(default=0,max_digits=15,decimal_places=2,verbose_name="Resolution Time",blank=True,null = True)
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")

    class Meta:
        verbose_name_plural = "tbl_problem_issue_mst"

class tbl_problem_issue_details(models.Model):
    header_ref_id = models.ForeignKey("tbl_problem_issue_mst", default=0,verbose_name="Header Ref ID",on_delete=models.CASCADE,related_name='initialItemRow')
    title = models.CharField(max_length=100,verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    attach_document= models.CharField(max_length=500,blank=True, null=True,verbose_name='Attach Document')
    is_it_original_entry_flag = models.CharField(default='N',max_length=1,verbose_name='Is it Original Entry Flag')
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")

    class Meta:
        verbose_name_plural = "tbl_problem_issue_details"


""" class tbl_helpdesk_mst(models.Model):
    share_id = models.IntegerField(default=0,verbose_name='Share ID')
    issue_mst_ref_id = models.ForeignKey("tbl_issue_mst", default=0, verbose_name="Issue Ref Id", on_delete=models.PROTECT)
    company_ref_id = models.ForeignKey("tbl_company_mst", default=0, verbose_name="Company Ref Id", on_delete=models.PROTECT)
    reported_by = models.ForeignKey("tbl_employee_mst", verbose_name="Reported By", on_delete=models.PROTECT)
    assigned_to_ref_id = models.ForeignKey("tbl_employee_mst", default=0, verbose_name="Assigned To Ref Id", on_delete=models.PROTECT,null = True ,blank= True)
    service_asset_ref_id = models.ForeignKey("tbl_service_asset_mst", verbose_name="Service Asset Ref Id", on_delete=models.PROTECT)
    priority_ref_id =models.ForeignKey("tbl_master", default=0, verbose_name="Priority Ref Id", on_delete=models.PROTECT)
    ticket_type_ref_id = models.ForeignKey("tbl_ticket_type_mst", default=0, verbose_name="Ticket Type Ref Id", on_delete=models.PROTECT)
    impact_ref_id = models.ForeignKey("tbl_master", default=0, verbose_name="Impact Ref Id", on_delete=models.PROTECT,related_name="helpdesk_impact")
    impact_on = models.CharField(max_length=100,null=True , blank= True,verbose_name='Impact On')
    status_ref_id = models.ForeignKey("tbl_ticket_status_mst", default=0, verbose_name="Status Ref Id", on_delete=models.PROTECT)
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    form = models.CharField(max_length=100,null=True , blank= True,verbose_name='Form')
    closed_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Closed Date Time")
    closed_by = models.IntegerField(default=0,verbose_name="Closed By",null = True ,blank= True)
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")

    class Meta:
        verbose_name_plural = "tbl_helpdesk_mst"

class tbl_helpdesk_details(models.Model):
    header_ref_id = models.ForeignKey("tbl_helpdesk_mst", default=0,verbose_name="Header Ref ID",on_delete=models.CASCADE,related_name='initialItemRow')
    title = models.CharField(max_length=100,verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    attach_document = models.CharField(max_length=500,blank=True, null=True,verbose_name='Attach Document')
    helpdesk_comments = models.CharField(max_length=500,blank=True, null=True,verbose_name='Help Desk Comments')
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")

    class Meta:
        verbose_name_plural = "tbl_helpdesk_details"

class tbl_assignees_action_mst(models.Model):
    share_id = models.IntegerField(default=0,verbose_name='Share ID')
    issue_mst_ref_id = models.ForeignKey("tbl_issue_mst", default=0, verbose_name="Issue Ref Id", on_delete=models.PROTECT)
    helpdesk_mst_ref_id = models.ForeignKey("tbl_helpdesk_mst", default=0, verbose_name="Help Desk Ref Id", on_delete=models.PROTECT)
    company_ref_id = models.ForeignKey("tbl_company_mst", default=0, verbose_name="Company Ref Id", on_delete=models.PROTECT)
    reported_by = models.ForeignKey("tbl_employee_mst", verbose_name="Reported By", on_delete=models.PROTECT)
    assigned_to_ref_id = models.ForeignKey("tbl_employee_mst", default=0, verbose_name="Assigned To Ref Id", on_delete=models.PROTECT,null = True ,blank= True)
    service_asset_ref_id = models.ForeignKey("tbl_service_asset_mst", verbose_name="Service Asset Ref Id", on_delete=models.PROTECT)
    priority_ref_id =models.ForeignKey("tbl_master", default=0, verbose_name="Priority Ref Id", on_delete=models.PROTECT)
    ticket_type_ref_id = models.ForeignKey("tbl_ticket_type_mst", default=0, verbose_name="Ticket Type Ref Id", on_delete=models.PROTECT)
    impact_ref_id = models.ForeignKey("tbl_master", default=0, verbose_name="Impact Ref Id", on_delete=models.PROTECT, related_name="assignees_impact")
    impact_on = models.CharField(max_length=100,null=True , blank= True,verbose_name='Impact On')
    status_ref_id = models.ForeignKey("tbl_ticket_status_mst", default=0, verbose_name="Status Ref Id", on_delete=models.PROTECT)
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    form = models.CharField(max_length=100,null=True , blank= True,verbose_name='Form')
    closed_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Closed Date Time")
    closed_by = models.IntegerField(default=0,verbose_name="Closed By",null = True ,blank= True)
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")

    class Meta:
        verbose_name_plural = "tbl_assignees_action_mst"

class tbl_assignees_action_details(models.Model):
    header_ref_id = models.ForeignKey("tbl_assignees_action_mst", default=0,verbose_name="Header Ref ID",on_delete=models.CASCADE,related_name='initialItemRow')
    title = models.CharField(max_length=100,verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    attach_document = models.CharField(max_length=500,blank=True, null=True,verbose_name='Attach Document')
    helpdesk_comments = models.CharField(max_length=500,blank=True, null=True,verbose_name='Help Desk Comments')
    assignees_action_comments = models.CharField(max_length=500,blank=True, null=True,verbose_name='Assignees Action Comments')
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")

    class Meta:
        verbose_name_plural = "tbl_assignees_action_details" """

class tbl_left_panel(models.Model):
    share_id = models.IntegerField(default=0,verbose_name='Share ID')
    form_name = models.CharField(max_length=30,verbose_name='Form Name')
    form_link = models.CharField(max_length=200,blank=True,null=True,verbose_name='Form Link')
    backend_model_name = models.CharField(max_length=500,blank=True,null=True,verbose_name='Back End Model')
    module_path = models.CharField(max_length=500,default=0,verbose_name='Module Path')
    is_parent = models.CharField(default='N',max_length=1,verbose_name='Is Parent')
    is_child = models.CharField(default='N',max_length=1,verbose_name='Is Child')
    is_sub_child = models.CharField(default='N',max_length=1,verbose_name='Is Sub Child')
    parent_code = models.CharField(max_length=50,verbose_name='Parent Code')
    child_code = models.CharField(max_length=50,blank=True,null=True,verbose_name='Child Code')
    sub_child_code = models.CharField(max_length=50,blank=True,null=True,verbose_name='Sub Child Code')
    icon_class = models.CharField(max_length=50,verbose_name='Icon Class')
    sequence_id = models.IntegerField(default=0,verbose_name="Sequence ID")
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")

    class Meta:
        verbose_name_plural = "tbl_left_panel"

class tbl_assign_screen_to_role_mst(models.Model):
    share_id = models.IntegerField(default=0,verbose_name='Share ID')
    company_ref_id = models.ForeignKey("tbl_company_mst", default=0, verbose_name="Company Ref Id", on_delete=models.PROTECT)
    assigned_to_role = models.ForeignKey("tbl_role_mst", default=0,verbose_name="Role", on_delete=models.PROTECT)
    form_ref_id = models.ForeignKey("tbl_left_panel", null=True, blank=True, verbose_name="Form Ref Id", on_delete=models.PROTECT)
    parent_code = models.CharField(max_length=50,verbose_name='Parent Code', null=True, blank=True)
    child_code = models.CharField(max_length=50,verbose_name='Child Code', null=True, blank=True)
    sub_child_code = models.CharField(max_length=50,verbose_name='Sub Child Code', null=True, blank=True)
    read_access = models.CharField(default='N',max_length=1,verbose_name='Read Access') #Visible on UI
    write_access = models.CharField(default='N',max_length=1,verbose_name='Write Access') #Visible on UI
    delete_access = models.CharField(default='N',max_length=1,verbose_name='Delete Access') #Visible on UI
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")

    class Meta:
        verbose_name_plural = "tbl_assign_screen_to_role_mst"

class tbl_assign_roles_to_enduser_mst(models.Model): #Enduser means either User or Employee
    share_id = models.IntegerField(default=0,verbose_name='Share ID')
    company_ref_id = models.ForeignKey("tbl_company_mst", default=0, verbose_name="Company Ref Id", on_delete=models.PROTECT)
    assigned_to_user = models.ForeignKey("tbl_employee_mst", null = True, blank=True, verbose_name="Assigned To User", on_delete=models.PROTECT, related_name="assigned_to_user")
    assigned_to_employee = models.ForeignKey("tbl_employee_mst", null = True, blank=True, verbose_name="Assigned To Employee", on_delete=models.PROTECT, related_name="assigned_to_employee")
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")

    class Meta:
        verbose_name_plural = "tbl_assign_roles_to_enduser_mst"

class tbl_assign_roles_to_enduser_details(models.Model): #Enduser means either User or Employee
    header_ref_id = models.ForeignKey("tbl_assign_roles_to_enduser_mst", default=0,verbose_name="Header Ref ID",on_delete=models.CASCADE,related_name='initialItemRow')
    assigned_to_role_ref_id = models.ForeignKey("Tbl_Role_Mst", default=0, verbose_name="Assigned to Role Ref Id", on_delete=models.PROTECT)
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")

    class Meta:
        verbose_name_plural = "tbl_assign_roles_to_enduser_details"

class tbl_asset_mst(models.Model):
    share_id = models.IntegerField(default=0,verbose_name='Share ID')
    asset_type = models.CharField(max_length=200,verbose_name='Asset Type')
    asset_description = models.CharField(default=0,max_length=200,verbose_name='Asset Description')
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")   

    class Meta:
        verbose_name_plural = "tbl_asset_mst"
        constraints = [
           models.UniqueConstraint(fields = ['asset_type'], condition=models.Q(is_deleted = 'N'), name='asset type unique if not deleted')
       ]

class tbl_asset_details(models.Model):
    header_ref_id = models.ForeignKey("tbl_asset_mst", default=0,verbose_name="Header Ref ID",on_delete=models.PROTECT,related_name='initialItemRow')
    asset_no = models.CharField(max_length=20,verbose_name="Asset No")
    asset_owner = models.ForeignKey("tbl_company_mst",verbose_name="Asset Owner", on_delete=models.PROTECT)
    asset_custodian = models.ForeignKey("tbl_employee_mst", verbose_name="Asset Custodian", on_delete=models.PROTECT, related_name="custodian")
    location_ref_id = models.ForeignKey("tbl_location_mst", default=0,verbose_name="Location Ref ID",on_delete=models.PROTECT)
    asset_tag = models.CharField(max_length=20,verbose_name="Asset Tag")
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID") 

    class Meta:
        verbose_name_plural = "tbl_asset_details"

class tbl_entity_relationship_mst(models.Model):
    share_id = models.IntegerField(default=0,verbose_name='Share ID')
    company_ref_id = models.ForeignKey("tbl_company_mst", default=0, verbose_name="Company Ref Id", on_delete=models.PROTECT)
    entity_ref_id = models.TextField(default=0,verbose_name='Entity Ref ID')
    is_active = models.CharField(default='Y',max_length=1,verbose_name='Is Active')
    is_deleted = models.CharField(max_length=1, default='N',verbose_name="Is Deleted")
    created_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Created Date Time")
    created_by = models.IntegerField(default=0,verbose_name="Created By")
    updated_date_time = models.DateTimeField(default=timezone.localtime,verbose_name="Updated Date Time")
    updated_by = models.IntegerField(default=0,verbose_name="Updated By")
    sub_application_id = models.CharField(max_length=20,verbose_name="Sub-Application ID")
    application_id = models.CharField(max_length=20,verbose_name="Application ID")

