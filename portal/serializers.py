from .models import *
from rest_framework import serializers
from re import T
from django.contrib.auth.models import User
from rest_framework import fields
from pyexpat import model
from django.db.models import fields
from rest_framework.fields import SerializerMethodField
from .automation import initiate_activity_tbl, routing_activity_for_Assignees_Action, update_activity_for_NOT_INITIATED, update_activity_tbl
class tbl_login_mst_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = tbl_login_mst
        fields  = ('__all__')

    def get(user):
        return tbl_login_mst.objects.get(user = user)

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required = False)   #may be required

    class Meta:
        model = User
        fields = ('__all__')
        
    def get(username):
        return User.objects.get(username = username)

class tbl_entity_relationship_mst_serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = tbl_entity_relationship_mst
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer): # Previously tbl_role_mst_serializer
    class Meta:
        model = tbl_role_mst
        fields = ('__all__')

    def get(role):
        return tbl_role_mst.objects.get(id = role.id)

class tbl_role_master_serializer(serializers.ModelSerializer):
    class Meta:
        model = tbl_role_mst
        fields = ('__all__')      

    def get(self, request):
        return tbl_role_mst.objects.filter(is_deleted='N').filter(share_id=request.GET['share_id']).filter(application_id=request.GET['application_id'])  

class MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = tbl_master
        fields = ('__all__')

    def get(type):
        return tbl_master.objects.get(id = type)

class tbl_company_mst_serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    company_type = serializers.CharField(source='company_type_ref_id.master_key', read_only=True)
    ownership_status = serializers.CharField(source='ownership_status_ref_id.master_key', read_only=True)
    location = serializers.CharField(source='location_ref_id.location_name', read_only=True)
    country = serializers.CharField(source='country_ref_id.name', read_only=True)
    state = serializers.CharField(source='state_ref_id.state', read_only=True)
    city = serializers.CharField(source='city_ref_id.city_name', read_only=True)

    class Meta:
        model = tbl_company_mst 
        fields = ('__all__') 

    def get(company):
        print (company)
        return tbl_company_mst.objects.get(id = company.company_id)

    
class tbl_location_mst_serializer(serializers.ModelSerializer):
    name = serializers.CharField(source='country_id.name', read_only=True)
    state = serializers.CharField(source='state_id.state', read_only=True)
    city_name = serializers.CharField(source='city_id.city_name', read_only=True)

    class Meta:
        model = tbl_location_mst
        fields = ('__all__') 
        
    def get(self, request):
        return tbl_location_mst.objects.filter(is_deleted='N').filter(share_id=request.GET['share_id']).filter(application_id=request.GET['application_id'])

class tbl_city_mst_serializer(serializers.ModelSerializer):
    locations = tbl_location_mst_serializer(many=True, read_only=True)
    class Meta:
        model = tbl_city_mst
        fields = ('__all__')

class tbl_state_mst_serializer(serializers.ModelSerializer):
    cities = tbl_city_mst_serializer(many=True, read_only=True)
    class Meta:
        model = tbl_state_mst
        fields = ('__all__')

class tbl_country_mst_serializer(serializers.ModelSerializer):
    states = tbl_state_mst_serializer(many=True, read_only=True)
    class Meta:
        model = tbl_country_mst
        fields = ('__all__')

class tbl_currency_mst_serializer(serializers.ModelSerializer):
    country_name = serializers.CharField(source='country_id.name',read_only=True)
    class Meta:
        model = tbl_currency_mst
        fields = ('__all__')

class tbl_reason_mst_serializer(serializers.ModelSerializer):
    class Meta:
        model = tbl_reason_mst
        fields = ('__all__')

# Employee Registation
class tbl_employee_mst_serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    company = serializers.CharField(source='company_ref_id.company_name', read_only=True)
    role = serializers.CharField(source='role_ref_id.role_name', read_only=True)
    city = serializers.CharField(source='city_ref_id.city_name', read_only=True)
    state = serializers.CharField(source='state_ref_id.state', read_only=True)
    country = serializers.CharField(source='country_ref_id.name', read_only=True)

    class Meta:
        model = tbl_employee_mst
        fields = '__all__'

    def get(self, request):
        return tbl_employee_mst.objects.filter(is_deleted='N').filter(company_type_ref_id=request.GET['company_type_ref_id'])

# User Registration
class tbl_user_mst_serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    company = serializers.CharField(source='company_ref_id.company_name', read_only=True)
    role = serializers.CharField(source='role_ref_id.role_name', read_only=True)

    class Meta:
        model = tbl_user_mst
        fields = '__all__'
       
class tbl_service_asset_mst_serializer(serializers.ModelSerializer):
    priority_name = serializers.CharField(source='priority_ref_id.master_key', read_only=True)

    class Meta:
        model = tbl_service_asset_mst 
        fields = '__all__'   

class tbl_ticket_type_mst_serializer(serializers.ModelSerializer):
    class Meta:
        model = tbl_ticket_type_mst
        fields = '__all__'  
    def get(self, request):
        return tbl_ticket_type_mst.objects.filter(is_deleted='N').filter(share_id=request.GET['share_id']).filter(application_id=request.GET['application_id'])

class tbl_company_application_link_details_serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    
    class Meta:
        model = tbl_company_application_link_details
        fields = '__all__'

    def get(self, request):
        return tbl_company_application_link_details.objects.filter(is_deleted='N').filter(share_id=request.GET['share_id']).filter(application_id=request.GET['application_id'])
        
class tbl_company_application_link_mst_serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    company_name = serializers.CharField(source='company_ref_id.company_name', read_only=True)
    initialItemRow = tbl_company_application_link_details_serializer(many=True)

    class Meta:
        model = tbl_company_application_link_mst
        fields = '__all__'

    def get(self, request):
        return tbl_company_application_link_mst.objects.filter(is_deleted='N').filter(share_id=request.GET['share_id']).filter(application_id=request.GET['application_id'])

    def create(self, validated_data):
        initialItemRow = validated_data.pop('initialItemRow')
       
        CompanyAppLinkMaster = tbl_company_application_link_mst.objects.create(**validated_data)
        for item in initialItemRow:
            tbl_company_application_link_details.objects.create(**item, header_ref_id=CompanyAppLinkMaster)
        return CompanyAppLinkMaster

    def update(self, instance, validated_data):
       
        object = tbl_company_application_link_mst.objects.get(id = validated_data['id'])
        initialItemRow = validated_data.pop('initialItemRow')
        instance.name = validated_data.get('name',instance.name)
        instance.description = validated_data.get('description',instance.description)
        instance.company_ref_id = validated_data.get('company_ref_id',instance.company_ref_id)
        instance.sub_application_id = validated_data.get('sub_application_id', instance.sub_application_id)
        instance.application_id = validated_data.get('application_id', instance.application_id)
        instance.is_deleted = validated_data.get('is_deleted', instance.is_deleted)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.created_date_time = validated_data.get('created_date_time', instance.created_date_time)
        instance.created_by = validated_data.get('created_by', instance.created_by)
        instance.updated_date_time = validated_data.get('updated_date_time', instance.updated_date_time)
        instance.updated_by = validated_data.get('updated_by', instance.updated_by)

        instance.save()
        keep_details = []

        for init in initialItemRow:
            if "id" in init.keys():
                if tbl_company_application_link_details.objects.filter(id=init['id']).exists():
                    det = tbl_company_application_link_details.objects.get(id=init['id'])
                    det.header_ref_id = init.get('header_ref_id',det.header_ref_id)
                    det.application_ref_id = init.get('application_ref_id',det.application_ref_id)
                    det.channel_ref_id = init.get('channel_ref_id',det.channel_ref_id)
                    det.created_date_time = init.get('created_date_time',det.created_date_time)
                    det.updated_date_time = init.get('updated_date_time',det.updated_date_time)
                    det.application_id = init.get('application_id',det.application_id)
                    det.sub_application_id = init.get('sub_application_id',det.sub_application_id)
                    instance.is_deleted = validated_data.get('is_deleted', instance.is_deleted)
                    instance.is_active = validated_data.get('is_active', instance.is_active)
                    det.updated_by = init.get('updated_by',det.updated_by)
                    det.created_by = init.get('created_by',det.created_by)

                    det.save()
                    keep_details.append(det.id)
                else:
                    continue
            else:
                det = tbl_company_application_link_details.objects.create(**init,header_ref_id=instance)
                keep_details.append(det.id)
        
        det = tbl_company_application_link_details.objects.filter(header_ref_id=object.id)
        det_id = [d.id for d in det]

        for d in det_id:
            if d in keep_details:
                continue
            else:
                det_record = tbl_company_application_link_details.objects.get(id=d)
                det_record.is_deleted = 'Y'
                det_record.save()

        return instance

class tbl_channel_mst_serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    
    class Meta:
        model = tbl_channel_mst
        fields = '__all__'
        
    def get(self, request):
        return tbl_channel_mst.objects.filter(is_deleted='N').filter(share_id=request.GET['share_id']).filter(application_id=request.GET['application_id'])

# SLA
class tbl_sla_details_mst_serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = tbl_sla_details
        fields = '__all__'

class tbl_sla_mst_serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    company_name = serializers.CharField(source='company_ref_id.company_name', read_only=True)
    
    initialItemRow = tbl_sla_details_mst_serializer(many=True)

    class Meta:
        model = tbl_sla_mst 
        fields = '__all__'   

    def create(self, validated_data):
        initialItemRow = validated_data.pop('initialItemRow')
       
        slaMaster = tbl_sla_mst.objects.create(**validated_data)
        for item in initialItemRow:
            tbl_sla_details.objects.create(**item, header_ref_id=slaMaster)
        return slaMaster
        
    def update(self, instance, validated_data):
        object = tbl_sla_mst.objects.get(id=validated_data['id'])
        initialItemRow = validated_data.pop('initialItemRow')

        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.company_ref_id = validated_data.get('company_ref_id', instance.company_ref_id)
        instance.from_date = validated_data.get('from_date', instance.from_date)
        instance.to_date = validated_data.get('to_date', instance.to_date)
        instance.revision_status = validated_data.get('revision_status', instance.revision_status)
        instance.sub_application_id = validated_data.get('sub_application_id', instance.sub_application_id)
        instance.application_id = validated_data.get('application_id', instance.application_id)
        instance.is_deleted = validated_data.get('is_deleted', instance.is_deleted)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        
        instance.created_by = validated_data.get('created_by', instance.created_by)


        instance.save()
        keep_details = []

        for init in initialItemRow:
            if "id" in init.keys():
                if tbl_sla_details.objects.filter(id=init['id']).exists():
                    det = tbl_sla_details.objects.get(id=init['id'])
                    det.header_ref_id = init.get('header_ref_id',det.header_ref_id)
                    det.application_ref_id = init.get('application_ref_id',det.application_ref_id)
                    det.ticket_type_ref_id = init.get('ticket_type_ref_id',det.ticket_type_ref_id)
                    det.priority_ref_id = init.get('priority_ref_id',det.priority_ref_id)
                    det.response_time= init.get('response_time',det.response_time)
                    det.resolution_time = init.get('resolution_time',det.resolution_time)
                    det.escalation_time = init.get('escalation_time',det.escalation_time)
                    det.availability_percentage=init.get('availability_percentage',det.availability_percentage)
                    det.down_time=init.get('down_time',det.down_time)
                    det.application_id = init.get('application_id',det.application_id)
                    det.sub_application_id = init.get('sub_application_id',det.sub_application_id)
                    instance.is_deleted = validated_data.get('is_deleted', instance.is_deleted)
                    instance.is_active = validated_data.get('is_active', instance.is_active)
                    det.created_by = init.get('created_by',det.created_by)

                    det.save()
                    keep_details.append(det.id)
                else:
                    continue
            else:
                det = tbl_sla_details.objects.create(**init,header_ref_id=instance)
                keep_details.append(det.id)
        
        det = tbl_sla_details.objects.filter(header_ref_id=object.id)
        det_id = [d.id for d in det]

        for d in det_id:
            if d in keep_details:
                continue
            else:
                det_record = tbl_sla_details.objects.get(id=d)
                det_record.is_deleted = 'Y'
                det_record.save()

        return instance

class tbl_message_mst_serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    
    class Meta:
        model = tbl_message_mst
        fields = '__all__'
    def get(self, request):
        return tbl_message_mst.objects.filter(is_deleted='N').filter(share_id=request.GET['share_id']).filter(application_id=request.GET['application_id'])  

# Workflow Module
class tbl_workflow_mst_serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = tbl_workflow_mst
        fields = '__all__'      

    def get(self, request):
        return tbl_workflow_mst.objects.filter(is_deleted='N').filter(share_id=request.GET['share_id']).filter(application_id=request.GET['application_id'])  

class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    workflow_type = serializers.CharField(source='workflow_type_ref_id.master_key', read_only=True)

    class Meta:
        model = tbl_workflow_activity_mst
        fields = ('__all__')  

    def get(self, request):
        return tbl_workflow_activity_mst.objects.filter(is_deleted='N').filter(share_id=request.GET['share_id']).filter(application_id=request.GET['application_id'])  

class LevelDetailsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = tbl_workflow_level_data_details
        fields = ('__all__')

    def get(self, request):
        return tbl_workflow_level_data_details.objects.filter(is_deleted='N').filter(share_id=request.GET['share_id']).filter(application_id=request.GET['application_id'])  

class LevelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    workflow_type = serializers.CharField(source='workflow_type_ref_id.master_key', read_only=True)

    initialItemRow = LevelDetailsSerializer(many=True)
    class Meta:
        model = tbl_workflow_level_data_mst
        fields = ('__all__')
    
    def get(self, request):
        return tbl_workflow_level_data_mst.objects.filter(is_deleted='N').filter(share_id=request.GET['share_id']).filter(application_id=request.GET['application_id'])  

    def create(self, validated_data):
        initialItemRow = validated_data.pop('initialItemRow')
        level = tbl_workflow_level_data_mst.objects.create(**validated_data)

        for item in initialItemRow:
            tbl_workflow_level_data_details.objects.create(**item, header_ref_id=level)
        return level

    def update(self, instance, validated_data):
        object = tbl_workflow_level_data_mst.objects.get(id=validated_data['id'])
        initialItemRow = validated_data.pop('initialItemRow')

        instance.workflow_type_ref_id = validated_data.get('workflow_type_ref_id', instance.workflow_type_ref_id)
        instance.level = validated_data.get('level', instance.level)
        instance.level_name = validated_data.get('level_name', instance.level_name)
        instance.activity_sequence = validated_data.get('activity_sequence', instance.activity_sequence)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_deleted = validated_data.get('is_deleted', instance.is_deleted)
        instance.created_date_time = validated_data.get('created_date_time', instance.created_date_time)
        instance.created_by = validated_data.get('created_by', instance.created_by)
        instance.updated_date_time = validated_data.get('updated_date_time', instance.updated_date_time)
        instance.updated_by = validated_data.get('updated_by', instance.updated_by)
        instance.sub_application_id = validated_data.get('sub_application_id', instance.sub_application_id)
        instance.application_id = validated_data.get('application_id', instance.application_id)
        instance.save()

        updated_data = []

        for init in initialItemRow:
            if "id" in init.keys():
                if tbl_workflow_level_data_details.objects.filter(id=init['id']).exists():
                    det = tbl_workflow_level_data_details.objects.get(id=init['id'])
                    activity_ref_id = init.get('activity_ref_id',det.activity_ref_id)
                    sequence_number = init.get('sequence_number',det.sequence_number)
                    action_ref_id = init.get('action_ref_id',det.action_ref_id)
                    next_sequence_number = init.get('next_sequence_number',det.next_sequence_number)
                    det.is_active = init.get('is_active', det.is_active)
                    det.is_deleted = init.get('is_deleted', det.is_deleted)
                    det.created_date_time = init.get('created_date_time', det.created_date_time)
                    det.created_by = init.get('created_by', det.created_by)
                    det.updated_date_time = init.get('updated_date_time', det.updated_date_time)
                    det.updated_by = init.get('updated_by', det.updated_by)
                    det.application_id = init.get('application_id', det.application_id)
                    det.sub_application_id = init.get('sub_application_id', det.sub_application_id)
                    det.save()
                    updated_data.append(det.id)
                else:
                    continue
            else:
                det = tbl_workflow_level_data_details.objects.create(**init, header_ref_id=instance)
                updated_data.append(det.id)

        det = tbl_workflow_level_data_details.objects.filter(header_ref_id=object.id)
        det_id = [d.id for d in det]

        for d in det_id:
            if d in updated_data:
                continue
            else:
                det_record = tbl_workflow_level_data_details.objects.get(id=d)
                det_record.is_deleted = 'Y'
                det_record.save()
        return instance

class ActionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = tbl_workflow_action_mst
        fields = ('__all__')

    def get(self, request):
        return tbl_workflow_action_mst.objects.filter(is_deleted='N').filter(share_id=request.GET['share_id']).filter(application_id=request.GET['application_id'])  

class GeneralSerializer(serializers.ModelSerializer):
    labels = serializers.SerializerMethodField()

    def _init_(self, *args, **kwargs):
        super(GeneralSerializer, self)._init_(*args, **kwargs)

        if 'labels' in self.fields:
            raise RuntimeError(
                'You cant have labels field defined '
                'while using GeneralSerializer'
            )

        self.fields['labels'] = SerializerMethodField()

    def get_labels(self, *args):
        labels = {}

        for field in self.Meta.model._meta.get_fields():
            if field.name in self.fields:
                labels[field.name] = field.verbose_name

        return labels

    class Meta:
        model = None
        exclude = ('is_active','is_deleted','created_date_time','created_by','updated_date_time','updated_by', 'sub_application_id','application_id' )        

class WorkflowSubDetailsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = tbl_workflow_sub_details
        fields = ('__all__')

    def get(self, request):
        return tbl_workflow_sub_details.objects.filter(is_deleted='N').filter(share_id=request.GET['share_id']).filter(application_id=request.GET['application_id'])  

class WorkflowDetailsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    # initialItemRow2 = WorkflowSubDetailsSerializer(many=True)
    class Meta:
        model = tbl_workflow_details
        fields = ('__all__')

    def get(self, request):
        return tbl_workflow_details.objects.filter(is_deleted='N').filter(share_id=request.GET['share_id']).filter(application_id=request.GET['application_id'])  

class WorkflowSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    workflow_type = serializers.CharField(source='workflow_type_ref_id.master_key', read_only=True)
    level = serializers.CharField(source='level_ref_id.level', read_only=True)
    company = serializers.CharField(source='company_ref_id.company_name', read_only=True)

    initialItemRow = WorkflowDetailsSerializer(many=True)
    initialItemRow2 = WorkflowSubDetailsSerializer(many=True)

    class Meta:
        model = tbl_workflow_mst
        fields = ('__all__') 
    
    def get(self, request):
        return tbl_workflow_mst.objects.filter(is_deleted='N').filter(share_id=request.GET['share_id']).filter(application_id=request.GET['application_id'])  

    def create(self, validated_data):
        print(validated_data)
        initialItemRow = validated_data.pop('initialItemRow')
        print(initialItemRow)
        initialItemRow2 = validated_data.pop('initialItemRow2')
        workflow = tbl_workflow_mst.objects.create(**validated_data)

        for item in initialItemRow:
            workflow_details = tbl_workflow_details.objects.create(**item, header_ref_id=workflow)
        
        for item2 in initialItemRow2:
            tbl_workflow_sub_details.objects.create(**item2, header_ref_id=workflow,details_ref_id=workflow_details)

        return workflow

    def update(self, instance, validated_data):
        object = tbl_workflow_mst.objects.get(id=validated_data['id'])
        initialItemRow = validated_data.pop('initialItemRow')
        initialItemRow2 = validated_data.pop('initialItemRow2')

        instance.company_ref_id  = validated_data.get('company_ref_id', instance.company_ref_id)
        instance.service_asset_ref_id  = validated_data.get('service_asset_ref_id', instance.service_asset_ref_id)
        #instance.resolution_time = validated_data.get('resolution_time', instance.resolution_time)
        instance.workflow_type_ref_id = validated_data.get('workflow_type_ref_id', instance.workflow_type_ref_id)
        instance.level_ref_id = validated_data.get('level_ref_id', instance.level_ref_id)
        instance.level_name = validated_data.get('level_name', instance.level_name)
        instance.workflow_name = validated_data.get('workflow_name', instance.workflow_name)
        instance.workflow_description = validated_data.get('workflow_description', instance.workflow_description)
        instance.sub_application_id = validated_data.get('sub_application_id', instance.sub_application_id)
        instance.application_id = validated_data.get('application_id', instance.application_id)
        instance.is_deleted = validated_data.get('is_deleted', instance.is_deleted)
        instance.updated_date_time = validated_data.get('updated_date_time', instance.updated_date_time)
        instance.save()

        updated_data = []
        updated_data2 = []

        for init in initialItemRow:
            if "id" in init.keys():
                if tbl_workflow_details.objects.filter(id=init['id']).exists():
                    det = tbl_workflow_details.objects.get(id=init['id'])
                    level_details_ref_id = init.get('level_details_ref_id',det.level_details_ref_id)
                    level_details_name = init.get('level_details_name', det.level_details_name)
                    left_panel_ref_id = init.get('left_panel_ref_id',det.left_panel_ref_id)
                    field_name = init.get('field_name',det.field_name)
                    #currency_id = init.get('currency_id',det.currency_id)
                    approval_field_value = init.get('approval_field_value',det.approval_field_value)
                    is_active = init.get('is_active',det.is_active)
                    is_deleted = init.get('is_deleted',det.is_deleted)
                    created_date_time = init.get('created_date_time',det.created_date_time)
                    created_by = init.get('created_by',det.created_by)
                    updated_date_time = init.get('updated_date_time',det.updated_date_time)
                    updated_by = init.get('updated_by',det.updated_by)
                    sub_application_id = init.get('sub_application_id',det.sub_application_id)
                    application_id = init.get('application_id',det.application_id)
                    det.save()
                    updated_data.append(det.id)
                else:
                    continue
            else:
                det = tbl_workflow_details.objects.create(**init, header_ref_id=instance)
                updated_data.append(det.id)
        
        for init2 in initialItemRow2:
            if "id" in init2.keys():
                if tbl_workflow_sub_details.objects.filter(id=init2['id']).exists():
                    det2 = tbl_workflow_sub_details.objects.get(id=init2['id'])
                    company_ref_id = init2.get('company_ref_id',det2.company_ref_id)
                    level_sub_details_ref_id = init2.get('level_sub_details_ref_id',det2.level_sub_details_ref_id)
                    role_ref_id = init2.get('role_ref_id',det2.role_ref_id)
                    employee_ref_id = init2.get('employee_ref_id',det2.employee_ref_id)
                    activity_ref_id = init2.get('activity_ref_id',det2.activity_ref_id)
                    sequence_number = init2.get('sequence_number',det2.sequence_number)
                    action_ref_id = init2.get('action_ref_id',det2.action_ref_id)
                    next_sequence_number = init2.get('next_sequence_number',det2.next_sequence_number)
                    is_email_required = init2.get('is_email_required',det2.is_email_required)
                    is_whatsapp_required = init2.get('is_whatsapp_required',det2.is_whatsapp_required)
                    is_sms_required = init2.get('is_sms_required',det2.is_sms_required)
                    is_reminder_required = init2.get('is_reminder_required',det2.is_reminder_required)
                    is_worklist_required = init2.get('is_worklist_required',det2.is_worklist_required)
                    #sla_days = init2.get('sla_days',det2.sla_days)
                    #sla_response_time = init2.get('sla_response_time', det2.sla_response_time)
                    reminder_days = init2.get('reminder_days',det2.reminder_days)
                    is_active = init2.get('is_active',det2.is_active)
                    is_deleted = init2.get('is_deleted',det2.is_deleted)
                    created_date_time = init2.get('created_date_time',det2.created_date_time)
                    created_by = init2.get('created_by',det2.created_by)
                    updated_date_time = init2.get('updated_date_time',det2.updated_date_time)
                    updated_by = init2.get('updated_by',det2.updated_by)
                    sub_application_id = init2.get('sub_application_id',det2.sub_application_id)
                    application_id = init2.get('application_id',det2.application_id)
                    det2.save()
                    updated_data2.append(det2.id)
                else:
                    continue
            else:
                det2 = tbl_workflow_sub_details.objects.create(**init2, header_ref_id=instance)
                updated_data2.append(det2.id)

        det = tbl_workflow_details.objects.filter(header_ref_id=object.id)
        det_id = [d.id for d in det]

        for d in det_id:
            if d in updated_data:
                continue
            else:
                det_record = tbl_workflow_details.objects.get(id=d)
                print(det_record)
                det_record.is_deleted = 'Y'
                det_record.save()
        
        det2 = tbl_workflow_sub_details.objects.filter(header_ref_id=object.id)
        det2_id = [d.id for d in det2]

        for d in det2_id:
            if d in updated_data2:
                continue
            else:
                det_record2 = tbl_workflow_sub_details.objects.get(id=d)
                print(det_record2)
                det_record2.is_deleted = 'Y'
                det_record2.save()
        
        return instance    

class WorkflowRoutingDetailsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = tbl_workflow_routing_details
        fields = ('__all__')
    
    def get(self, request):
        return tbl_workflow_routing_details.objects.filter(is_deleted='N').filter(share_id=request.GET['share_id']).filter(application_id=request.GET['application_id'])  

class WorkflowRoutingSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    initialItemRow = WorkflowRoutingDetailsSerializer(many=True)

    class Meta:
        model = tbl_workflow_routing_mst
        fields = ('__all__')

    def get(self, request):
        return tbl_workflow_routing_mst.objects.filter(is_deleted='N').filter(share_id=request.GET['share_id']).filter(application_id=request.GET['application_id'])  

    def create(self, validated_data):
        initialItemRow = validated_data.pop('initialItemRow')
        level = tbl_workflow_routing_mst.objects.create(**validated_data)

        for item in initialItemRow:
            tbl_workflow_routing_details.objects.create(**item, header_ref_id=level)
        return level

    def update(self, instance, validated_data):
        object = tbl_workflow_routing_mst.objects.get(id=validated_data['id'])
        initialItemRow = validated_data.pop('initialItemRow')

        instance.workflow_routing_name = validated_data.get('workflow_routing_name', instance.workflow_routing_name)
        instance.workflow_routing_desc = validated_data.get('workflow_routing_desc', instance.workflow_routing_desc)
        instance.version_number = validated_data.get('version_number', instance.version_number)
        instance.sub_application_id = validated_data.get('sub_application_id', instance.sub_application_id)
        instance.application_id = validated_data.get('application_id', instance.application_id)
        instance.is_deleted = validated_data.get('is_deleted', instance.is_deleted)
        instance.updated_date_time = validated_data.get('updated_date_time', instance.updated_date_time)
        instance.save()

        updated_data = []

        for init in initialItemRow:
            if "id" in init.keys():
                if tbl_workflow_routing_details.objects.filter(id=init['id']).exists():
                    det = tbl_workflow_routing_details.objects.get(id=init['id'])
                    sequence_number = init.get('sequence_number',det.sequence_number)
                    next_sequence_number = init.get('next_sequence_number',det.next_sequence_number)
                    workflow_ref_id = init.get('workflow_ref_id',det.workflow_ref_id)
                    next_workflow_ref_id = init.get('next_workflow_ref_id',det.next_workflow_ref_id)
                    role_ref_id = init.get('role_ref_id',det.role_ref_id)
                    employee_ref_id = init.get('employee_ref_id',det.employee_ref_id)
                    det.created_date_time = init.get('created_date_time', det.created_date_time)
                    det.is_deleted = init.get('is_deleted', det.is_deleted)
                    det.updated_date_time = init.get('updated_date_time', det.updated_date_time)
                    det.application_id = init.get('application_id', det.application_id)
                    det.sub_application_id = init.get('sub_application_id', det.sub_application_id)
                    det.save()
                    updated_data.append(det.id)
                else:
                    continue
            else:
                det = tbl_workflow_routing_details.objects.create(**init, header_ref_id=instance)
                updated_data.append(det.id)

        det = tbl_workflow_routing_details.objects.filter(header_ref_id=object.id)
        det_id = [d.id for d in det]

        for d in det_id:
            if d in updated_data:
                continue
            else:
                det_record = tbl_workflow_routing_details.objects.get(id=d)
                print(det_record)
                det_record.is_deleted = 'Y'
                print(det_record.is_deleted,'nnnnnnnnnnnnnn')
                det_record.save()
        return instance

class EmployeeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = tbl_employee_mst
        fields = ('__all__')

    def get(self, request):
        return tbl_employee_mst.objects.filter(is_deleted='N').filter(share_id=request.GET['share_id']).filter(application_id=request.GET['application_id'])  

class CurrencySerializer(serializers.ModelSerializer):
    country_name = serializers.CharField(source='country_id.name',read_only=True)
    class Meta:
        model = tbl_currency_mst
        fields = ('__all__')

    def get(self, request):
        return tbl_currency_mst.objects.filter(is_deleted='N').filter(share_id=request.GET['share_id']).filter(application_id=request.GET['application_id'])  

# Role Application Link
class tbl_role_application_details_serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    
    class Meta:
        model = tbl_role_application_details
        fields = '__all__'
        
class tbl_role_application_mst_serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    initialItemRow = tbl_role_application_details_serializer(many=True)
    company_name = serializers.CharField(source='company_ref_id.company_name', read_only=True) 
    role_name = serializers.CharField(source='role_ref_id.role_name', read_only=True) 
    class Meta:
        model = tbl_role_application_mst
        fields = '__all__'

    def create(self, validated_data):
        initialItemRow = validated_data.pop('initialItemRow')
        RoleAppLinkMaster = tbl_role_application_mst.objects.create(**validated_data)
        
        for item in initialItemRow:
            tbl_role_application_details.objects.create(**item, header_ref_id=RoleAppLinkMaster)
        return RoleAppLinkMaster

    def update(self, instance, validated_data):
        
        object = tbl_role_application_mst.objects.get(id = validated_data['id'])
        initialItemRow = validated_data.pop('initialItemRow')
        instance.company_ref_id = validated_data.get('company_ref_id',instance.company_ref_id)
        instance.role_ref_id = validated_data.get('role_ref_id',instance.role_ref_id)
        instance.updated_date_time = validated_data.get('updated_date_time', instance.updated_date_time)
        instance.updated_by = validated_data.get('updated_by', instance.updated_by)
        instance.is_deleted = validated_data.get('is_deleted',instance.is_deleted)
        instance.save()
        keep_details = []

        for init in initialItemRow:
            if "id" in init.keys():
                if tbl_role_application_details.objects.filter(id=init['id']).exists():
                    det = tbl_role_application_details.objects.get(id=init['id'])
                    det.header_ref_id = init.get('header_ref_id',det.header_ref_id)
                    det.application_ref_id = init.get('application_ref_id',det.application_ref_id)
                    det.updated_date_time = init.get('updated_date_time',det.updated_date_time)
                    det.updated_by = init.get('updated_by',det.updated_by)
                    det.is_deleted = init.get('is_deleted',det.is_deleted)
                    det.save()
                    keep_details.append(det.id)
                else:
                    continue
            else:
                det = tbl_role_application_details.objects.create(**init,header_ref_id=instance)
                keep_details.append(det.id)
        
        det = tbl_role_application_details.objects.filter(header_ref_id=object.id)
        det_id = [d.id for d in det]

        for d in det_id:
            if d in keep_details:
                continue
            else:
                det_record = tbl_role_application_details.objects.get(id=d)
                det_record.is_deleted = 'Y'
                det_record.save()

        return instance

class file_serializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ("__all__")   
   
class tbl_ticket_status_mst_serializer(serializers.ModelSerializer):
    class Meta:
        model = tbl_ticket_status_mst
        fields = ('__all__')   

# Issue  
class tbl_issue_details_serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = tbl_issue_details
        fields = ('__all__')
              
class tbl_issue_mst_serializer(serializers.ModelSerializer):
    
    id = serializers.IntegerField(required=False)
    
    company_name = serializers.CharField(source='company_ref_id.company_name', read_only=True) 
    impact = serializers.CharField(source='impact_ref_id.master_key', read_only=True) 
    reported_by_name = serializers.CharField(source='reported_by.first_name', read_only=True) 
    priority_name = serializers.CharField(source='priority_ref_id.master_key', read_only=True)
    ticket_type = serializers.CharField(source='ticket_type_ref_id.ticket_name', read_only=True)
    status = serializers.CharField(source='status_ref_id.name', read_only=True)
    assigned_to = serializers.CharField(source='assigned_to_ref_id.first_name', read_only=True)
   
    initialItemRow = tbl_issue_details_serializer(many=True)
    class Meta:
        model = tbl_issue_mst
        fields = ('__all__')
    
    def create(self, validated_data):
       
        initialItemRow = validated_data.pop('initialItemRow')
        IssueMaster = tbl_issue_mst.objects.create(**validated_data)

        left_panel_id_for_Issue = tbl_left_panel.objects.filter(form_name="Issue", is_deleted='N').first().id
        print('Serializer : Left Panel Issue')
        left_panel_id_for_HelpDesk = tbl_left_panel.objects.filter(form_name="Help Desk Incident", is_deleted='N').first().id
        print('Serializer : Left Panel Help Desk')
        left_panel_id_for_Assignees_Action = tbl_left_panel.objects.filter(form_name="Assignees Action Incident", is_deleted='N').first().id
        print('Serializer : Assignees Action')

        form_ref_id = IssueMaster.id 
        form_company_ref_id = IssueMaster.company_ref_id.id
        form_service_asset_ref_id = IssueMaster.service_asset_ref_id.id
        form_ticket_type_ref_id = IssueMaster.ticket_type_ref_id.id
        form_priority_ref_id = IssueMaster.priority_ref_id.id
        
        for item in initialItemRow:
            tbl_issue_details.objects.create(**item, header_ref_id=IssueMaster)
        
        initiate_activity_tbl(left_panel_id_for_Issue, form_ref_id, form_company_ref_id, form_service_asset_ref_id, form_ticket_type_ref_id, form_priority_ref_id)
        initiate_activity_tbl(left_panel_id_for_HelpDesk, form_ref_id, form_company_ref_id, form_service_asset_ref_id, form_ticket_type_ref_id, form_priority_ref_id)
        routing_activity_for_Assignees_Action(left_panel_id_for_Assignees_Action, form_ref_id, form_company_ref_id, form_service_asset_ref_id)
                
        return IssueMaster

    def update(self, instance, validated_data):
        
        object = tbl_issue_mst.objects.get(id = validated_data['id'])
        initialItemRow = validated_data.pop('initialItemRow')
        instance.company_ref_id = validated_data.get('company_ref_id',instance.company_ref_id)
        instance.reported_by = validated_data.get('reported_by',instance.reported_by)
        instance.assigned_to_ref_id = validated_data.get('assigned_to_ref_id',instance.assigned_to_ref_id)
        instance.service_asset_ref_id = validated_data.get('service_asset_ref_id',instance.service_asset_ref_id)
        instance.priority_ref_id = validated_data.get('priority_ref_id',instance.priority_ref_id)
        instance.ticket_type_ref_id = validated_data.get('ticket_type_ref_id',instance.ticket_type_ref_id)
        instance.impact_ref_id = validated_data.get('impact_ref_id',instance.impact_ref_id)
        instance.impact_on = validated_data.get('impact_on',instance.impact_on)
        instance.status_ref_id = validated_data.get('status_ref_id',instance.status_ref_id)
        instance.conversion_ticket_type_ref_id = validated_data.get('conversion_ticket_type_ref_id',instance.conversion_ticket_type_ref_id)
        instance.is_converted_flag = validated_data.get('is_converted_flag',instance.is_converted_flag)
        instance.converted_issue_ref_id = validated_data.get('converted_issue_ref_id',instance.converted_issue_ref_id)
        instance.converted_problem_ref_id = validated_data.get('converted_problem_ref_id',instance.converted_problem_ref_id)
        instance.total_resolution_time = validated_data.get('total_resolution_time',instance.total_resolution_time)
        instance.form = validated_data.get('form',instance.form) 
        instance.closed_by = validated_data.get('closed_by', instance.closed_by)
        instance.closed_date_time = validated_data.get('closed_date_time', instance.closed_date_time)
        instance.updated_date_time = validated_data.get('updated_date_time', instance.updated_date_time)
        instance.updated_by = validated_data.get('updated_by', instance.updated_by)
        instance.is_deleted = validated_data.get('is_deleted',instance.is_deleted)
        print(instance)
        instance.save()
        keep_details = []

        for init in initialItemRow:
            if "id" in init.keys():
                if tbl_issue_details.objects.filter(id=init['id']).exists():
                    det = tbl_issue_details.objects.get(id=init['id'])
                    det.header_ref_id = init.get('header_ref_id',det.header_ref_id)
                    det.title = init.get('title',det.title)
                    det.description = init.get('description',det.description)
                    det.attach_document = init.get('attach_document',det.attach_document)
                    det.updated_date_time = init.get('updated_date_time',det.updated_date_time)
                    det.updated_by = init.get('updated_by',det.updated_by)
                    det.is_deleted = init.get('is_deleted',det.is_deleted)
                    det.save()
                    keep_details.append(det.id)
                else:
                    continue
            else:
                det = tbl_issue_details.objects.create(**init,header_ref_id=instance)
                keep_details.append(det.id)
                
        det = tbl_issue_details.objects.filter(header_ref_id=object.id)
        det_id = [d.id for d in det]

        for d in det_id:
            if d in keep_details:
                continue
            else:
                det_record = tbl_issue_details.objects.get(id=d)
                det_record.is_deleted = 'Y'
                det_record.save()

        form_ref_id = object.id
        #left_panel_id_for_HelpDesk = tbl_left_panel.objects.filter(form_name="Help Desk").filter(is_deleted='N')[0].id
        
       # update_issue_activity_from_issue(form_ref_id)
        return instance

#Incident Help Desk
class help_desk_details_serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = tbl_issue_details
        fields = ('__all__')

class help_desk_mst_serializer(serializers.ModelSerializer):
    
    id = serializers.IntegerField(required=False)
    
    company_name = serializers.CharField(source='company_ref_id.company_name', read_only=True) 
    impact = serializers.CharField(source='impact_ref_id.master_key', read_only=True) 
    reported_by_name = serializers.CharField(source='reported_by.first_name', read_only=True) 
    priority_name = serializers.CharField(source='priority_ref_id.master_key', read_only=True)
    ticket_type = serializers.CharField(source='ticket_type_ref_id.ticket_name', read_only=True)
    status = serializers.CharField(source='status_ref_id.name', read_only=True)
    assigned_to = serializers.CharField(source='assigned_to_ref_id.first_name', read_only=True)
   
    initialItemRow = help_desk_details_serializer(many=True)
    class Meta:
        model = tbl_issue_mst
        fields = ('__all__')
    
    def create(self, validated_data):
        initialItemRow = validated_data.pop('initialItemRow')
        IssueMaster = tbl_issue_mst.objects.create(**validated_data)
        
        for item in initialItemRow:
            tbl_issue_details.objects.create(**item, header_ref_id=IssueMaster)
        return IssueMaster

    def update(self, instance, validated_data):
        submitAction = self.context.get('submitAction')
        print(submitAction)
        object = tbl_issue_mst.objects.get(id = validated_data['id'])
        initialItemRow = validated_data.pop('initialItemRow')
        instance.company_ref_id = validated_data.get('company_ref_id',instance.company_ref_id)
        instance.reported_by = validated_data.get('reported_by',instance.reported_by)
        instance.assigned_to_ref_id = validated_data.get('assigned_to_ref_id',instance.assigned_to_ref_id)
        instance.service_asset_ref_id = validated_data.get('service_asset_ref_id',instance.service_asset_ref_id)
        instance.priority_ref_id = validated_data.get('priority_ref_id',instance.priority_ref_id)
        instance.ticket_type_ref_id = validated_data.get('ticket_type_ref_id',instance.ticket_type_ref_id)
        instance.impact_ref_id = validated_data.get('impact_ref_id',instance.impact_ref_id)
        instance.impact_on = validated_data.get('impact_on',instance.impact_on)
        instance.status_ref_id = validated_data.get('status_ref_id',instance.status_ref_id)
        instance.conversion_ticket_type_ref_id = validated_data.get('conversion_ticket_type_ref_id',instance.conversion_ticket_type_ref_id)
        instance.is_converted_flag = validated_data.get('is_converted_flag',instance.is_converted_flag)
        instance.converted_issue_ref_id = validated_data.get('converted_issue_ref_id',instance.converted_issue_ref_id)
        instance.converted_problem_ref_id = validated_data.get('converted_problem_ref_id',instance.converted_problem_ref_id)
        instance.total_resolution_time = validated_data.get('total_resolution_time',instance.total_resolution_time)
        instance.form = validated_data.get('form',instance.form) 
        instance.closed_by = validated_data.get('closed_by', instance.closed_by)
        instance.closed_date_time = validated_data.get('closed_date_time', instance.closed_date_time)
        instance.updated_date_time = validated_data.get('updated_date_time', instance.updated_date_time)
        instance.updated_by = validated_data.get('updated_by', instance.updated_by)
        instance.is_deleted = validated_data.get('is_deleted',instance.is_deleted)
        instance.save()
        keep_details = []

        form_ref_id = object.id
        form_company_ref_id = object.company_ref_id.id
        form_service_asset_ref_id = object.service_asset_ref_id.id
        form_ticket_type_ref_id = object.ticket_type_ref_id.id
        form_priority_ref_id = object.priority_ref_id.id
        left_panel_id_for_HelpDesk = tbl_left_panel.objects.filter(form_name="Help Desk Incident", is_deleted='N').first().id
        print('Help Desk Update - Form Ref ID : ', form_ref_id)
        left_panel_id_for_Assignees_Action = tbl_left_panel.objects.filter(form_name="Assignees Action Incident", is_deleted='N').first().id
        print('Serializer : Left Panel Assignees Action')
        user_action_ref_id = tbl_workflow_action_mst.objects.filter(id=1).first()
        print('Serializer : User Action Ref ID', user_action_ref_id)

        for init in initialItemRow:
            if "id" in init.keys():
                if tbl_issue_details.objects.filter(id=init['id']).exists():
                    det = tbl_issue_details.objects.get(id=init['id'])
                    det.header_ref_id = init.get('header_ref_id',det.header_ref_id)
                    det.title = init.get('title',det.title)
                    det.description = init.get('description',det.description)
                    det.attach_document = init.get('attach_document',det.attach_document)
                    det.updated_date_time = init.get('updated_date_time',det.updated_date_time)
                    det.updated_by = init.get('updated_by',det.updated_by)
                    det.is_deleted = init.get('is_deleted',det.is_deleted)
                    det.save()
                    keep_details.append(det.id)
                else:
                    continue
            else:
                det = tbl_issue_details.objects.create(**init,header_ref_id=instance)
                keep_details.append(det.id)
        
        print('Serializer : Assign - Help Desk')
        update_activity_tbl(left_panel_id_for_HelpDesk, form_ref_id, user_action_ref_id, form_company_ref_id, form_service_asset_ref_id)
        update_activity_for_NOT_INITIATED(left_panel_id_for_HelpDesk, form_ref_id, user_action_ref_id, form_company_ref_id, form_service_asset_ref_id)
        initiate_activity_tbl(left_panel_id_for_Assignees_Action, form_ref_id, form_company_ref_id, form_service_asset_ref_id, form_ticket_type_ref_id, form_priority_ref_id)
               
        det = tbl_issue_details.objects.filter(header_ref_id=object.id)
        det_id = [d.id for d in det]

        for d in det_id:
            if d in keep_details:
                continue
            else:
                det_record = tbl_issue_details.objects.get(id=d)
                det_record.is_deleted = 'Y'
                det_record.save()

    #    #Update values in activity table
    #     print("validated data",validated_data)
        form_ref_id = object.id
        #update_issue_activity_from_help_desk(form_ref_id)
        #initiate_activity_tbl(21, 5)
        return instance

#Incident Assignees Action
class assignees_action_details_serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = tbl_issue_details
        fields = ('__all__')

class assignees_action_mst_serializer(serializers.ModelSerializer):
    
    id = serializers.IntegerField(required=False)
    
    company_name = serializers.CharField(source='company_ref_id.company_name', read_only=True) 
    impact = serializers.CharField(source='impact_ref_id.master_key', read_only=True) 
    reported_by_name = serializers.CharField(source='reported_by.first_name', read_only=True) 
    priority_name = serializers.CharField(source='priority_ref_id.master_key', read_only=True)
    ticket_type = serializers.CharField(source='ticket_type_ref_id.ticket_name', read_only=True)
    status = serializers.CharField(source='status_ref_id.name', read_only=True)
    assigned_to = serializers.CharField(source='assigned_to_ref_id.first_name', read_only=True)
   
    initialItemRow = assignees_action_details_serializer(many=True)
    class Meta:
        model = tbl_issue_mst
        fields = ('__all__')
    
    def create(self, validated_data):
        initialItemRow = validated_data.pop('initialItemRow')
        IssueMaster = tbl_issue_mst.objects.create(**validated_data)
        
        for item in initialItemRow:
            tbl_issue_details.objects.create(**item, header_ref_id=IssueMaster)
        return IssueMaster

    def update(self, instance, validated_data):
     
        print('validated_data',validated_data)
        object = tbl_issue_mst.objects.get(id = validated_data['id'])
        initialItemRow = validated_data.pop('initialItemRow')
     
        instance.company_ref_id = validated_data.get('company_ref_id',instance.company_ref_id)
        instance.reported_by = validated_data.get('reported_by',instance.reported_by)
        instance.assigned_to_ref_id = validated_data.get('assigned_to_ref_id',instance.assigned_to_ref_id)
        instance.service_asset_ref_id = validated_data.get('service_asset_ref_id',instance.service_asset_ref_id)
        instance.priority_ref_id = validated_data.get('priority_ref_id',instance.priority_ref_id)
        instance.ticket_type_ref_id = validated_data.get('ticket_type_ref_id',instance.ticket_type_ref_id)
        instance.impact_ref_id = validated_data.get('impact_ref_id',instance.impact_ref_id)
        instance.impact_on = validated_data.get('impact_on',instance.impact_on)
        instance.status_ref_id = validated_data.get('status_ref_id',instance.status_ref_id)
        instance.conversion_ticket_type_ref_id = validated_data.get('conversion_ticket_type_ref_id',instance.conversion_ticket_type_ref_id)
        instance.is_converted_flag = validated_data.get('is_converted_flag',instance.is_converted_flag)
        instance.converted_issue_ref_id = validated_data.get('converted_issue_ref_id',instance.converted_issue_ref_id)
        instance.converted_problem_ref_id = validated_data.get('converted_problem_ref_id',instance.converted_problem_ref_id)
        instance.total_resolution_time = validated_data.get('total_resolution_time',instance.total_resolution_time)
        instance.form = validated_data.get('form',instance.form) 
        instance.closed_by = validated_data.get('closed_by', instance.closed_by)
        instance.closed_date_time = validated_data.get('closed_date_time', instance.closed_date_time)
        instance.updated_date_time = validated_data.get('updated_date_time', instance.updated_date_time)
        instance.updated_by = validated_data.get('updated_by', instance.updated_by)
        instance.is_deleted = validated_data.get('is_deleted',instance.is_deleted)
        instance.save()
        keep_details = []

        form_ref_id = object.id 
        form_company_ref_id = object.company_ref_id.id
        form_service_asset_ref_id = object.service_asset_ref_id.id
        left_panel_id_for_Assignees_Action = tbl_left_panel.objects.filter(form_name="Assignees Action Incident", is_deleted='N').first().id
        print('Serializer : Left Panel Assignees Action')
        user_action_ref_id = tbl_workflow_action_mst.objects.filter(id=3).first()
        print('Serializer : User Action Ref ID', user_action_ref_id)

        for init in initialItemRow:
            if "id" in init.keys():
                if tbl_issue_details.objects.filter(id=init['id']).exists():
                    det = tbl_issue_details.objects.get(id=init['id'])
                    det.header_ref_id = init.get('header_ref_id',det.header_ref_id)
                    det.title = init.get('title',det.title)
                    det.description = init.get('description',det.description)
                    det.attach_document = init.get('attach_document',det.attach_document)
                    det.updated_date_time = init.get('updated_date_time',det.updated_date_time)
                    det.updated_by = init.get('updated_by',det.updated_by)
                    det.is_deleted = init.get('is_deleted',det.is_deleted)
                    det.save()
                    keep_details.append(det.id)
                else:
                    continue
            else:
                det = tbl_issue_details.objects.create(**init,header_ref_id=instance)
                keep_details.append(det.id)

        print('Serializer : Close - Assignees Action')
        update_activity_tbl(left_panel_id_for_Assignees_Action, form_ref_id, user_action_ref_id, form_company_ref_id, form_service_asset_ref_id)
        update_activity_for_NOT_INITIATED(left_panel_id_for_Assignees_Action, form_ref_id, user_action_ref_id, form_company_ref_id, form_service_asset_ref_id)
        
        det = tbl_issue_details.objects.filter(header_ref_id=object.id)
        det_id = [d.id for d in det]

        for d in det_id:
            if d in keep_details:
                continue
            else:
                det_record = tbl_issue_details.objects.get(id=d)
                det_record.is_deleted = 'Y'
                det_record.save()

        return instance

class LeftPanelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = tbl_left_panel
        fields = ('__all__')

    def get(self, request):
        return tbl_left_panel.objects.filter(is_deleted='N').filter(share_id=request.GET['share_id']).filter(application_id=request.GET['application_id']) 

# Assign Screen To Role 
class tbl_assign_screen_to_role_mst_Serializer(serializers.ModelSerializer):

    id = serializers.IntegerField(required=False)
    company_name = serializers.CharField(source='company_ref_id.company_name', read_only=True)
    form_name = serializers.CharField(source='form_ref_id.form_name',read_only=True)
    role_name = serializers.CharField(source='assigned_to_role.role_name',read_only=True)

    class Meta:
        model = tbl_assign_screen_to_role_mst
        fields = ('__all__')

    def get(self, request):
        return tbl_assign_screen_to_role_mst.objects.filter(is_deleted='N').filter(share_id=request.GET['share_id']).filter(application_id=request.GET['application_id'])

# Assign Roles To Enduser       
class RolesToEnduserDetailsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = tbl_assign_roles_to_enduser_details
        fields = ('__all__')

class AssignRolesToEnduserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    assigned_to_user_f_name=serializers.CharField(source='assigned_to_user.first_name',read_only=True)
    assigned_to_user_l_name=serializers.CharField(source='assigned_to_user.last_name',read_only=True)
    assigned_to_employee_f_name=serializers.CharField(source='assigned_to_employee.first_name',read_only=True)
    assigned_to_employee_l_name=serializers.CharField(source='assigned_to_employee.last_name',read_only=True)
    initialItemRow = RolesToEnduserDetailsSerializer(many=True)
    
    class Meta:
        model = tbl_assign_roles_to_enduser_mst
        fields = ('__all__')

    def create(self, validated_data):
        initialItemRow = validated_data.pop('initialItemRow')
        role = tbl_assign_roles_to_enduser_mst.objects.create(**validated_data)
        for item in initialItemRow:
            tbl_assign_roles_to_enduser_details.objects.create(**item, header_ref_id=role)
        return role

    def update(self, instance, validated_data):
        object = tbl_assign_roles_to_enduser_mst.objects.get(id=validated_data['id'])
        initialItemRow = validated_data.pop('initialItemRow')

        instance.company_ref_id = validated_data.get('company_ref_id', instance.company_ref_id)
        instance.assigned_to_user = validated_data.get('assigned_to_user', instance.assigned_to_user)
        instance.assigned_to_employee = validated_data.get('assigned_to_employee', instance.assigned_to_employee)
        instance.sub_application_id = validated_data.get('sub_application_id', instance.sub_application_id)
        instance.application_id = validated_data.get('application_id', instance.application_id)
        instance.is_deleted = validated_data.get('is_deleted', instance.is_deleted)
        instance.updated_date_time = validated_data.get('updated_date_time', instance.updated_date_time)
        instance.save()

        updated_data = []

        for init in initialItemRow:
            if "id" in init.keys():
                if tbl_assign_roles_to_enduser_details.objects.filter(id=init['id']).exists():
                    det = tbl_assign_roles_to_enduser_details.objects.get(id=init['id'])
                    det.assigned_to_role_ref_id = init.get('assigned_to_role_ref_id',det.assigned_to_role_ref_id)
                    det.created_date_time = init.get('created_date_time', det.created_date_time)
                    det.is_deleted = init.get('is_deleted', det.is_deleted)
                    det.updated_date_time = init.get('updated_date_time', det.updated_date_time)
                    det.application_id = init.get('application_id', det.application_id)
                    det.sub_application_id = init.get('sub_application_id', det.sub_application_id)
                    det.save()
                    updated_data.append(det.id)
                else:
                    continue
            else:
                det = tbl_assign_roles_to_enduser_details.objects.create(**init, header_ref_id=instance)
                updated_data.append(det.id)

        det = tbl_assign_roles_to_enduser_details.objects.filter(header_ref_id=object.id)
        det_id = [d.id for d in det]

        for d in det_id:
            if d in updated_data:
                continue
            else:
                det_record = tbl_assign_roles_to_enduser_details.objects.get(id=d)
                det_record.is_deleted = 'Y'
                det_record.save()
        return instance

# workflowData = tbl_workflow_activity.objects.filter(form_ref_id=form_ref_id,).filter(is_deleted='N')
#         activityData = tbl_workflow_activity_mst.objects.filter(activity_name='Assign').filter(is_deleted = 'N')
#         activityId = activityData[0].id
#         workflow_ref_id  = workflowData[0].workflow_ref_id.id
        # left_panel = tbl_left_panel.objects.filter(form_name="Help Desk").filter(is_deleted='N')
        # left_panel_id = left_panel[0].id
        # print("Left Panel = ",left_panel[0].id)
        # initiate_activity_tbl(left_panel_id, form_ref_id)
        #print("form ref id= ",form_ref_id)
        #print("workflow ref id = ",workflow_ref_id)
        #print("activity Id",activityId)
        # for workflow_activity_entry in workflowData:
        #     print(workflow_activity_entry)
        #     if workflow_activity_entry:
        #         if workflow_activity_entry.status == "Initiated" and workflow_activity_entry.sequence_number == 1:
        #             workflow_activity_entry.status = "Closed"
        #         if workflow_activity_entry.activity_ref_id.activity_name=="Assign" and workflow_activity_entry.sequence_number == 2:
        #             workflow_activity_entry.status = "Initiated"
        #         if workflow_activity_entry.activity_ref_id.activity_name=="Resubmit" and workflow_activity_entry.sequence_number == 2:
        #             workflow_activity_entry.status = "Initiated"              
        #     workflow_activity_entry.save()    
                 
        #initiate_activity_tbl(left_panel_id, form_ref_id)
        
# Company Priority Link
class tbl_company_priority_link_details_mst_serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = tbl_company_priority_link_details
        fields = '__all__'

class tbl_company_priority_link_mst_serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    company_name = serializers.CharField(source='company_ref_id.company_name', read_only=True)
    
    initialItemRow = tbl_company_priority_link_details_mst_serializer(many=True)

    class Meta:
        model = tbl_company_priority_link_mst 
        fields = '__all__'   

    def create(self, validated_data):
        initialItemRow = validated_data.pop('initialItemRow')
       
        companyprioritylinkMaster = tbl_company_priority_link_mst.objects.create(**validated_data)
        for item in initialItemRow:
            tbl_company_priority_link_details.objects.create(**item, header_ref_id=companyprioritylinkMaster)
        return companyprioritylinkMaster
        
    def update(self, instance, validated_data):
        object = tbl_company_priority_link_mst.objects.get(id=validated_data['id'])
        initialItemRow = validated_data.pop('initialItemRow')
        instance.company_ref_id = validated_data.get('company_ref_id', instance.company_ref_id)
        instance.from_date = validated_data.get('from_date', instance.from_date)
        instance.to_date = validated_data.get('to_date', instance.to_date)
        instance.revision_status = validated_data.get('revision_status', instance.revision_status)
        instance.sub_application_id = validated_data.get('sub_application_id', instance.sub_application_id)
        instance.application_id = validated_data.get('application_id', instance.application_id)
        instance.is_deleted = validated_data.get('is_deleted', instance.is_deleted)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        
        instance.created_by = validated_data.get('created_by', instance.created_by)


        instance.save()
        keep_details = []

        for init in initialItemRow:
            if "id" in init.keys():
                if tbl_company_priority_link_details.objects.filter(id=init['id']).exists():
                    det = tbl_company_priority_link_details.objects.get(id=init['id'])
                    det.header_ref_id = init.get('header_ref_id',det.header_ref_id)
                    det.priority_ref_id = init.get('priority_ref_id',det.priority_ref_id)
                    det.response_time= init.get('response_time',det.response_time)
                    det.resolution_time = init.get('resolution_time',det.resolution_time)
                    det.escalation_time = init.get('escalation_time',det.escalation_time)
                    det.availability_percentage=init.get('availability_percentage',det.availability_percentage)
                    det.down_time=init.get('down_time',det.down_time)
                    det.application_id = init.get('application_id',det.application_id)
                    det.sub_application_id = init.get('sub_application_id',det.sub_application_id)
                    instance.is_deleted = validated_data.get('is_deleted', instance.is_deleted)
                    instance.is_active = validated_data.get('is_active', instance.is_active)
                    det.created_by = init.get('created_by',det.created_by)

                    det.save()
                    keep_details.append(det.id)
                else:
                    continue
            else:
                det = tbl_company_priority_link_details.objects.create(**init,header_ref_id=instance)
                keep_details.append(det.id)
        
        det = tbl_company_priority_link_details.objects.filter(header_ref_id=object.id)
        det_id = [d.id for d in det]

        for d in det_id:
            if d in keep_details:
                continue
            else:
                det_record = tbl_company_priority_link_details.objects.get(id=d)
                det_record.is_deleted = 'Y'
                det_record.save()

        return instance
    def get(self, request):
        return tbl_company_priority_link_mst.objects.filter(is_deleted='N').filter(share_id=request.GET['share_id']).filter(application_id=request.GET['application_id'])

class tbl_problem_issue_details_serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = tbl_problem_issue_details
        fields = ('__all__')

class tbl_problem_issue_mst_serializer(serializers.ModelSerializer):
    
    id = serializers.IntegerField(required=False)
    
    company_name = serializers.CharField(source='company_ref_id.company_name', read_only=True) 
    impact = serializers.CharField(source='impact_ref_id.master_key', read_only=True) 
    reported_by_name = serializers.CharField(source='reported_by.first_name', read_only=True) 
    priority_name = serializers.CharField(source='priority_ref_id.master_key', read_only=True)
    ticket_type = serializers.CharField(source='ticket_type_ref_id.ticket_name', read_only=True)
    status = serializers.CharField(source='status_ref_id.name', read_only=True)
    assigned_to = serializers.CharField(source='assigned_to_ref_id.first_name', read_only=True)
   
    initialItemRow = tbl_problem_issue_details_serializer(many=True)
    class Meta:
        model =  tbl_problem_issue_mst
        fields = ('__all__')
    
    def create(self, validated_data):
       
        initialItemRow = validated_data.pop('initialItemRow')
        ProblemIssueMaster =  tbl_problem_issue_mst.objects.create(**validated_data)

        left_panel_id_for_Problem_Issue = tbl_left_panel.objects.filter(form_name="Help Desk Incident", is_deleted='N').first().id
        print('Serializer : Left Panel Problem Issue')
        left_panel_id_for_HelpDesk_Problem = tbl_left_panel.objects.filter(form_name="Help Desk Problem", is_deleted='N').first().id
        print('Serializer : Left Panel Help Desk', left_panel_id_for_HelpDesk_Problem)
        left_panel_id_for_Assignees_Action = tbl_left_panel.objects.filter(form_name="Assignees Action Problem", is_deleted='N').first().id
        print('Serializer : Left Panel Assignees Action Problem')

        form_ref_id = ProblemIssueMaster.id 
        form_company_ref_id = ProblemIssueMaster.company_ref_id.id
        form_service_asset_ref_id = ProblemIssueMaster.service_asset_ref_id.id
        form_ticket_type_ref_id = ProblemIssueMaster.ticket_type_ref_id.id
        form_priority_ref_id = ProblemIssueMaster.priority_ref_id.id
        
        for item in initialItemRow:
            tbl_problem_issue_details.objects.create(**item, header_ref_id=ProblemIssueMaster)
        
        initiate_activity_tbl(left_panel_id_for_Problem_Issue, form_ref_id, form_company_ref_id, form_service_asset_ref_id, form_ticket_type_ref_id, form_priority_ref_id)
        initiate_activity_tbl(left_panel_id_for_HelpDesk_Problem, form_ref_id, form_company_ref_id, form_service_asset_ref_id, form_ticket_type_ref_id, form_priority_ref_id)
        routing_activity_for_Assignees_Action(left_panel_id_for_Assignees_Action, form_ref_id, form_company_ref_id, form_service_asset_ref_id)
                
        return ProblemIssueMaster

    def update(self, instance, validated_data):
        
        object = tbl_problem_issue_mst.objects.get(id = validated_data['id'])
        initialItemRow = validated_data.pop('initialItemRow')
        instance.company_ref_id = validated_data.get('company_ref_id',instance.company_ref_id)
        instance.reported_by = validated_data.get('reported_by',instance.reported_by)
        instance.assigned_to_ref_id = validated_data.get('assigned_to_ref_id',instance.assigned_to_ref_id)
        instance.service_asset_ref_id = validated_data.get('service_asset_ref_id',instance.service_asset_ref_id)
        instance.priority_ref_id = validated_data.get('priority_ref_id',instance.priority_ref_id)
        instance.ticket_type_ref_id = validated_data.get('ticket_type_ref_id',instance.ticket_type_ref_id)
        instance.impact_ref_id = validated_data.get('impact_ref_id',instance.impact_ref_id)
        instance.impact_on = validated_data.get('impact_on',instance.impact_on)
        instance.status_ref_id = validated_data.get('status_ref_id',instance.status_ref_id)
        instance.form = validated_data.get('form',instance.form) 
        instance.closed_by = validated_data.get('closed_by', instance.closed_by)
        instance.closed_date_time = validated_data.get('closed_date_time', instance.closed_date_time)
        instance.updated_date_time = validated_data.get('updated_date_time', instance.updated_date_time)
        instance.updated_by = validated_data.get('updated_by', instance.updated_by)
        instance.is_deleted = validated_data.get('is_deleted',instance.is_deleted)
        instance.total_resolution_time = validated_data.get('total_resolution_time',instance.total_resolution_time)
        instance.save()
        keep_details = []

        for init in initialItemRow:
            if "id" in init.keys():
                if tbl_problem_issue_details.objects.filter(id=init['id']).exists():
                    det = tbl_problem_issue_details.objects.get(id=init['id'])
                    det.header_ref_id = init.get('header_ref_id',det.header_ref_id)
                    det.title = init.get('title',det.title)
                    det.description = init.get('description',det.description)
                    det.attach_document = init.get('attach_document',det.attach_document)
                    det.updated_date_time = init.get('updated_date_time',det.updated_date_time)
                    det.updated_by = init.get('updated_by',det.updated_by)
                    det.is_deleted = init.get('is_deleted',det.is_deleted)
                    det.save()
                    keep_details.append(det.id)
                else:
                    continue
            else:
                det = tbl_problem_issue_details.objects.create(**init,header_ref_id=instance)
                keep_details.append(det.id)
                
        det = tbl_problem_issue_details.objects.filter(header_ref_id=object.id)
        det_id = [d.id for d in det]

        for d in det_id:
            if d in keep_details:
                continue
            else:
                det_record = tbl_problem_issue_details.objects.get(id=d)
                det_record.is_deleted = 'Y'
                det_record.save()

        form_ref_id = object.id
        left_panel_id_for_HelpDesk_Problem = tbl_left_panel.objects.filter(form_name="Help Desk Problem").filter(is_deleted='N')[0].id
        
       # update_issue_activity_from_issue(form_ref_id)
        return instance

#Problem Help Desk
class problem_help_desk_details_serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = tbl_problem_issue_details
        fields = ('__all__')
              
class problem_help_desk_mst_serializer(serializers.ModelSerializer):
    
    id = serializers.IntegerField(required=False)
    
    company_name = serializers.CharField(source='company_ref_id.company_name', read_only=True) 
    impact = serializers.CharField(source='impact_ref_id.master_key', read_only=True) 
    reported_by_name = serializers.CharField(source='reported_by.first_name', read_only=True) 
    priority_name = serializers.CharField(source='priority_ref_id.master_key', read_only=True)
    ticket_type = serializers.CharField(source='ticket_type_ref_id.ticket_name', read_only=True)
    status = serializers.CharField(source='status_ref_id.name', read_only=True)
    assigned_to = serializers.CharField(source='assigned_to_ref_id.first_name', read_only=True)
   
    initialItemRow = problem_help_desk_details_serializer(many=True)
    class Meta:
        model = tbl_problem_issue_mst
        fields = ('__all__')
    
    def create(self, validated_data):
        initialItemRow = validated_data.pop('initialItemRow')
        IssueMaster = tbl_problem_issue_mst.objects.create(**validated_data)
        
        for item in initialItemRow:
            tbl_problem_issue_details.objects.create(**item, header_ref_id=IssueMaster)
        return IssueMaster

    def update(self, instance, validated_data):
        # print("Submit Action=",validated_data.get('submitAction'))
        # print("Validate data 1=",validated_data)
        # print(" ")
        # print("Self Data Resubmit =",self.data.get("submitAction"))
        # print(" ")
        # print("SubmitAction = ",self.context.get("submitAction"))
        # request= self.context.get("request")
        # submitAction = request.submitAction
        # print("Submit Action 2=",submitAction)

        object = tbl_problem_issue_mst.objects.get(id = validated_data['id'])
        
        initialItemRow = validated_data.pop('initialItemRow')
        instance.company_ref_id = validated_data.get('company_ref_id',instance.company_ref_id)
        instance.reported_by = validated_data.get('reported_by',instance.reported_by)
        instance.assigned_to_ref_id = validated_data.get('assigned_to_ref_id',instance.assigned_to_ref_id)
        instance.service_asset_ref_id = validated_data.get('service_asset_ref_id',instance.service_asset_ref_id)
        instance.priority_ref_id = validated_data.get('priority_ref_id',instance.priority_ref_id)
        instance.ticket_type_ref_id = validated_data.get('ticket_type_ref_id',instance.ticket_type_ref_id)
        instance.impact_ref_id = validated_data.get('impact_ref_id',instance.impact_ref_id)
        instance.impact_on = validated_data.get('impact_on',instance.impact_on)
        instance.status_ref_id = validated_data.get('status_ref_id',instance.status_ref_id)
        instance.form = validated_data.get('form',instance.form) 
        instance.closed_by = validated_data.get('closed_by', instance.closed_by)
        instance.closed_date_time = validated_data.get('closed_date_time', instance.closed_date_time)
        instance.updated_date_time = validated_data.get('updated_date_time', instance.updated_date_time)
        instance.updated_by = validated_data.get('updated_by', instance.updated_by)
        instance.is_deleted = validated_data.get('is_deleted',instance.is_deleted)
        instance.total_resolution_time = validated_data.get('total_resolution_time',instance.total_resolution_time)
        instance.save()
        keep_details = []

        form_ref_id = object.id 
        form_company_ref_id = object.company_ref_id.id
        form_service_asset_ref_id = object.service_asset_ref_id.id
        form_ticket_type_ref_id = object.ticket_type_ref_id.id
        form_priority_ref_id = object.priority_ref_id.id
        left_panel_id_for_HelpDesk = tbl_left_panel.objects.filter(form_name="Help Desk Problem", is_deleted='N').first().id
        print('Help Desk Update - Form Ref ID : ', form_ref_id)
        left_panel_id_for_Assignees_Action = tbl_left_panel.objects.filter(form_name="Assignees Action Problem", is_deleted='N').first().id
        print('Serializer : Left Panel Assignees Action')
        user_action_ref_id = tbl_workflow_action_mst.objects.filter(id=1).first()
        print('Serializer : User Action Ref ID', user_action_ref_id)

        for init in initialItemRow:
            if "id" in init.keys():
                if tbl_problem_issue_details.objects.filter(id=init['id']).exists():
                    det = tbl_problem_issue_details.objects.get(id=init['id'])
                    det.header_ref_id = init.get('header_ref_id',det.header_ref_id)
                    det.title = init.get('title',det.title)
                    det.description = init.get('description',det.description)
                    det.attach_document = init.get('attach_document',det.attach_document)
                    det.updated_date_time = init.get('updated_date_time',det.updated_date_time)
                    det.updated_by = init.get('updated_by',det.updated_by)
                    det.is_deleted = init.get('is_deleted',det.is_deleted)
                    det.save()
                    keep_details.append(det.id)
                else:
                    continue
            else:
                det = tbl_problem_issue_details.objects.create(**init,header_ref_id=instance)
                keep_details.append(det.id)
        
        print('Serializer : Assign - Help Desk')
        update_activity_tbl(left_panel_id_for_HelpDesk, form_ref_id, user_action_ref_id, form_company_ref_id, form_service_asset_ref_id)
        update_activity_for_NOT_INITIATED(left_panel_id_for_HelpDesk, form_ref_id, user_action_ref_id, form_company_ref_id, form_service_asset_ref_id)
        initiate_activity_tbl(left_panel_id_for_Assignees_Action, form_ref_id, form_company_ref_id, form_service_asset_ref_id, form_ticket_type_ref_id, form_priority_ref_id)
               
        det = tbl_problem_issue_details.objects.filter(header_ref_id=object.id)
        det_id = [d.id for d in det]

        for d in det_id:
            if d in keep_details:
                continue
            else:
                det_record = tbl_problem_issue_details.objects.get(id=d)
                det_record.is_deleted = 'Y'
                det_record.save()

    #    #Update values in activity table
    #     print("validated data",validated_data)
        form_ref_id = object.id
        #update_issue_activity_from_help_desk(form_ref_id)
        #initiate_activity_tbl(21, 5)
        return instance

#Incident Assignees Action
class problem_assignees_action_details_serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = tbl_problem_issue_details
        fields = ('__all__')

class problem_assignees_action_mst_serializer(serializers.ModelSerializer):
    
    id = serializers.IntegerField(required=False)
    
    company_name = serializers.CharField(source='company_ref_id.company_name', read_only=True) 
    impact = serializers.CharField(source='impact_ref_id.master_key', read_only=True) 
    reported_by_name = serializers.CharField(source='reported_by.first_name', read_only=True) 
    priority_name = serializers.CharField(source='priority_ref_id.master_key', read_only=True)
    ticket_type = serializers.CharField(source='ticket_type_ref_id.ticket_name', read_only=True)
    status = serializers.CharField(source='status_ref_id.name', read_only=True)
    assigned_to = serializers.CharField(source='assigned_to_ref_id.first_name', read_only=True)
   
    initialItemRow = problem_assignees_action_details_serializer(many=True)
    class Meta:
        model = tbl_problem_issue_mst
        fields = ('__all__')
    
    def create(self, validated_data):
        initialItemRow = validated_data.pop('initialItemRow')
        IssueMaster = tbl_problem_issue_mst.objects.create(**validated_data)
        
        for item in initialItemRow:
            tbl_problem_issue_details.objects.create(**item, header_ref_id=IssueMaster)
        return IssueMaster

    def update(self, instance, validated_data):
     
        object = tbl_problem_issue_mst.objects.get(id = validated_data['id'])
        initialItemRow = validated_data.pop('initialItemRow')
     
        instance.company_ref_id = validated_data.get('company_ref_id',instance.company_ref_id)
        instance.reported_by = validated_data.get('reported_by',instance.reported_by)
        instance.assigned_to_ref_id = validated_data.get('assigned_to_ref_id',instance.assigned_to_ref_id)
        instance.service_asset_ref_id = validated_data.get('service_asset_ref_id',instance.service_asset_ref_id)
        instance.priority_ref_id = validated_data.get('priority_ref_id',instance.priority_ref_id)
        instance.ticket_type_ref_id = validated_data.get('ticket_type_ref_id',instance.ticket_type_ref_id)
        instance.impact_ref_id = validated_data.get('impact_ref_id',instance.impact_ref_id)
        instance.impact_on = validated_data.get('impact_on',instance.impact_on)
        instance.status_ref_id = validated_data.get('status_ref_id',instance.status_ref_id)
        instance.form = validated_data.get('form',instance.form) 
        instance.closed_by = validated_data.get('closed_by', instance.closed_by)
        instance.closed_date_time = validated_data.get('closed_date_time', instance.closed_date_time)
        instance.updated_date_time = validated_data.get('updated_date_time', instance.updated_date_time)
        instance.updated_by = validated_data.get('updated_by', instance.updated_by)
        instance.is_deleted = validated_data.get('is_deleted',instance.is_deleted)
        instance.total_resolution_time = validated_data.get('total_resolution_time',instance.total_resolution_time)
        instance.save()
        keep_details = []

        form_ref_id = object.id 
        form_company_ref_id = object.company_ref_id.id
        form_service_asset_ref_id = object.service_asset_ref_id.id
        left_panel_id_for_Assignees_Action = tbl_left_panel.objects.filter(form_name="Assignees Action Problem", is_deleted='N').first().id
        print('Serializer : Left Panel Assignees Action')
        user_action_ref_id = tbl_workflow_action_mst.objects.filter(id=3).first()
        print('Serializer : User Action Ref ID', user_action_ref_id)

        for init in initialItemRow:
            if "id" in init.keys():
                if tbl_problem_issue_details.objects.filter(id=init['id']).exists():
                    det = tbl_problem_issue_details.objects.get(id=init['id'])
                    det.header_ref_id = init.get('header_ref_id',det.header_ref_id)
                    det.title = init.get('title',det.title)
                    det.description = init.get('description',det.description)
                    det.attach_document = init.get('attach_document',det.attach_document)
                    det.updated_date_time = init.get('updated_date_time',det.updated_date_time)
                    det.updated_by = init.get('updated_by',det.updated_by)
                    det.is_deleted = init.get('is_deleted',det.is_deleted)
                    det.save()
                    keep_details.append(det.id)
                else:
                    continue
            else:
                det = tbl_problem_issue_details.objects.create(**init,header_ref_id=instance)
                keep_details.append(det.id)

        print('Serializer : Close - Assignees Action')
        update_activity_tbl(left_panel_id_for_Assignees_Action, form_ref_id, user_action_ref_id, form_company_ref_id, form_service_asset_ref_id)
        update_activity_for_NOT_INITIATED(left_panel_id_for_Assignees_Action, form_ref_id, user_action_ref_id, form_company_ref_id, form_service_asset_ref_id)
        
        det = tbl_problem_issue_details.objects.filter(header_ref_id=object.id)
        det_id = [d.id for d in det]

        for d in det_id:
            if d in keep_details:
                continue
            else:
                det_record = tbl_problem_issue_details.objects.get(id=d)
                det_record.is_deleted = 'Y'
                det_record.save()

        return instance

class tbl_asset_details_serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    
    class Meta:
        model = tbl_asset_details
        fields = '__all__'

    def get(self, request):
        return tbl_asset_details.objects.filter(is_deleted='N').filter(share_id=request.GET['share_id']).filter(application_id=request.GET['application_id'])

class tbl_asset_mst_serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    company_name = serializers.CharField(source='company_ref_id.company_name', read_only=True)
    initialItemRow = tbl_asset_details_serializer(many=True)

    class Meta:
        model = tbl_asset_mst
        fields = '__all__'

    def get(self, request):
        return tbl_asset_mst.objects.filter(is_deleted='N').filter(share_id=request.GET['share_id']).filter(application_id=request.GET['application_id'])

    def create(self, validated_data):
        initialItemRow = validated_data.pop('initialItemRow')
       
        AssetMaster = tbl_asset_mst.objects.create(**validated_data)
        for item in initialItemRow:
            tbl_asset_details.objects.create(**item, header_ref_id=AssetMaster)
        return AssetMaster

    def update(self, instance, validated_data):
       
        object = tbl_asset_mst.objects.get(id = validated_data['id'])
        initialItemRow = validated_data.pop('initialItemRow')
        instance.asset_type = validated_data.get('asset_type',instance.asset_type)
        instance.asset_description = validated_data.get('asset_description',instance.asset_description)
        instance.sub_application_id = validated_data.get('sub_application_id', instance.sub_application_id)
        instance.application_id = validated_data.get('application_id', instance.application_id)
        instance.is_deleted = validated_data.get('is_deleted', instance.is_deleted)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.created_date_time = validated_data.get('created_date_time', instance.created_date_time)
        instance.created_by = validated_data.get('created_by', instance.created_by)
        instance.updated_date_time = validated_data.get('updated_date_time', instance.updated_date_time)
        instance.updated_by = validated_data.get('updated_by', instance.updated_by)

        instance.save()
        keep_details = []

        for init in initialItemRow:
            if "id" in init.keys():
                if tbl_asset_details.objects.filter(id=init['id']).exists():
                    det = tbl_asset_details.objects.get(id=init['id'])
                    det.header_ref_id = init.get('header_ref_id',det.header_ref_id)
                    det.asset_no = init.get('asset_no',det.asset_no)
                    det.asset_owner = init.get('asset_owner',det.asset_owner)
                    det.asset_custodian = init.get('asset_custodian',det.asset_custodian)
                    det.location_ref_id = init.get('location_ref_id',det.location_ref_id)
                    det.asset_tag = init.get('asset_tag',det.asset_tag)
                    det.created_date_time = init.get('created_date_time',det.created_date_time)
                    det.updated_date_time = init.get('updated_date_time',det.updated_date_time)
                    det.application_id = init.get('application_id',det.application_id)
                    det.sub_application_id = init.get('sub_application_id',det.sub_application_id)
                    instance.is_deleted = validated_data.get('is_deleted', instance.is_deleted)
                    instance.is_active = validated_data.get('is_active', instance.is_active)
                    det.updated_by = init.get('updated_by',det.updated_by)
                    det.created_by = init.get('created_by',det.created_by)

                    det.save()
                    keep_details.append(det.id)
                else:
                    continue
            else:
                det = tbl_asset_details.objects.create(**init,header_ref_id=instance)
                keep_details.append(det.id)
        
        det = tbl_asset_details.objects.filter(header_ref_id=object.id)
        det_id = [d.id for d in det]

        for d in det_id:
            if d in keep_details:
                continue
            else:
                det_record = tbl_asset_details.objects.get(id=d)
                det_record.is_deleted = 'Y'
                det_record.save()

        return instance
