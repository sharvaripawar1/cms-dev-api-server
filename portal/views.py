from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets,status,generics,permissions
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.schemas import views
from rest_framework.response import Response
from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
import json
import re
from rest_framework.parsers import JSONParser,FileUploadParser, MultiPartParser, FormParser
from django.db import connection, models
from django.db.models import query
from django.http import HttpResponse, request
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
import django.apps
from django.apps import apps
from django.contrib import admin
from rhythmworks_recon import settings
from django.utils import timezone
from rest_framework.parsers import JSONParser,FileUploadParser, MultiPartParser, FormParser
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from rhythmworks_recon.settings import EMAIL_HOST_USER
from rest_framework.permissions import IsAuthenticated

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

class tbl_company_mst_view(viewsets.ModelViewSet):
    serializer_class = tbl_company_mst_serializer
    queryset = tbl_company_mst.objects.filter(is_deleted='N').order_by('-id')

class add_company_view(APIView):
    
    def post(self, request, *args, **kwargs):
        company_serializer = tbl_company_mst_serializer(data=request.data['company_master_form'])
        plain_text_pass = request.data['userForm']['password']
        request.data['userForm']['password'] = make_password(request.data['userForm']['password'],hasher='default')
        user_serializer = UserSerializer(data=request.data['userForm'])
        print(company_serializer.is_valid(),"company_serializer" )
        print( user_serializer.is_valid() ,"user_serializer")
        print( user_serializer.errors ,"user_serializer")
        try:
            print('In Try')
            if company_serializer.is_valid() and user_serializer.is_valid(): 
                company_serializer.save()
                user_serializer.save()

                request.data['entityRelationMstForm']['company_ref_id'] = company_serializer['id'].value
                request.data['entityRelationMstForm']['entity_ref_id'] = company_serializer['id'].value
                entity_serializer_1 = tbl_entity_relationship_mst_serializer(data=request.data['entityRelationMstForm'])
                print( entity_serializer_1.is_valid() ,"entity_serializer_1")
                if entity_serializer_1.is_valid():
                    entity_serializer_1.save()

                request.data['entityRelationMstForm']['company_ref_id'] = company_serializer['id'].value
                request.data['entityRelationMstForm']['entity_ref_id'] = request.data['COMPANY_ID']
                #request.data['entityRelationMstForm']['entity_ref_id'] = company_serializer['company_id'].value
                entity_serializer_2 = tbl_entity_relationship_mst_serializer(data=request.data['entityRelationMstForm'])
                print( entity_serializer_2.is_valid() ,"entity_serializer_2")
                if entity_serializer_2.is_valid():
                    entity_serializer_2.save()

                request.data['roleMstForm']['company_ref_id'] = company_serializer['id'].value
                role_serializer = RoleSerializer(data=request.data['roleMstForm'])  
                print( role_serializer.is_valid() ,"role_serializer")          
                if role_serializer.is_valid():
                    role_serializer.save()

                #print(login_serializer.is_valid())
                request.data['loginMasterForm']['company_id'] = company_serializer['id'].value
                request.data['loginMasterForm']['role_ref_id'] = role_serializer['id'].value
                request.data['loginMasterForm']['user'] = user_serializer['id'].value
                login_serializer = tbl_login_mst_serializer(data=request.data['loginMasterForm'])
                print( login_serializer.is_valid() ,"login_serializer")          
                if login_serializer.is_valid():
                    login_serializer.save()

                # Send Mail Function
                subject = 'WELCOME'
                message = 'Rhythmflows CMS Welcomes You!' + '\n\n' + 'USERNAME: ' + request.data['userForm']['username'] + '\n' + 'PASSWORD: ' + plain_text_pass
                recepient = request.data['company_master_form']['email']
                send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)

                return Response(company_serializer.data, status=status.HTTP_201_CREATED)

            return Response(company_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print('In Except')
            return JsonResponse({"Exception_Message":str(e)})
            
    def put(self, request, pk):
        saved_company = get_object_or_404(tbl_company_mst.objects.all(),pk=pk)
        company_serializer = tbl_company_mst_serializer(instance=saved_company, data=request.data['company_master_form'])
        if company_serializer.is_valid():
            company_serializer.save()
            return Response(company_serializer.data, status=status.HTTP_201_CREATED)
        return Response(company_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class tbl_login_mst_view(viewsets.ModelViewSet):
    serializer_class = tbl_login_mst_serializer
    queryset = tbl_login_mst.objects.all() 
          
class tbl_state_mst_view(viewsets.ModelViewSet):
    serializer_class = tbl_state_mst_serializer
    queryset = tbl_state_mst.objects.filter(is_deleted='N')

class tbl_city_mst_view(viewsets.ModelViewSet):
    serializer_class = tbl_city_mst_serializer
    queryset = tbl_city_mst.objects.filter(is_deleted='N')

class tbl_ticket_type_mst_view(viewsets.ModelViewSet):
    serializer_class=tbl_ticket_type_mst_serializer
    queryset=tbl_ticket_type_mst.objects.filter(is_deleted='N')
    
class tbl_location_mst_view(viewsets.ModelViewSet):
    
    serializer_class = tbl_location_mst_serializer
    queryset = tbl_location_mst.objects.all().filter(is_deleted='N')

    def delete(self):
        self.queryset = tbl_location_mst.objects.filter(self=self).update(is_deleted='Y')

class MasterViewSet(viewsets.ModelViewSet):
    serializer_class = MasterSerializer
    queryset = tbl_master.objects.filter(is_deleted='N')

    def list(self, request, master_type=None):
        if master_type:
            master = tbl_master.objects.filter(master_type = master_type, is_deleted='N')
            serializer = self.get_serializer(master, many=True)
            return Response(serializer.data)
        else:
            currency = tbl_master.objects.filter(is_deleted='N')
            serializer = self.get_serializer(currency, many=True)
            return Response(serializer.data)

class tbl_currency_mst_view(viewsets.ModelViewSet):
    queryset = tbl_currency_mst.objects.filter(is_deleted='N')
    serializer_class = tbl_currency_mst_serializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['currency_code','is_deleted']

    def list(self, request, country_id=None):
        if country_id:
            currency = tbl_currency_mst.objects.filter(country_id = country_id, is_deleted='N')
            serializer = self.get_serializer(currency, many=True)
            return Response(serializer.data)
        else:
            currency = tbl_currency_mst.objects.filter(is_deleted='N')
            serializer = self.get_serializer(currency, many=True)
            return Response(serializer.data)

class tbl_reason_mst_view(viewsets.ModelViewSet):
    serializer_class = tbl_reason_mst_serializer
    queryset = tbl_reason_mst.objects.all().filter(is_deleted='N')

    def delete(self):
        self.queryset = tbl_reason_mst.objects.filter(self=self).update(is_deleted='Y')

class tbl_country_mst_view(viewsets.ModelViewSet):
    queryset = tbl_country_mst.objects.filter(is_deleted='N')
    serializer_class = tbl_country_mst_serializer        

class company_name_view(APIView):
    def get(self, request):
        serializer_class = User.objects.filter(username=request.GET['user_name'])
        # serializer_result = LoginMasterSerializer(serializer_class, many=True)
        # print(serializer_result)
        breakpoint()
        # return Response(serializer_result, status=status.HTTP_201_CREATED)

# Employee Registation 
class tbl_employee_mst_view(viewsets.ModelViewSet):
    serializer_class = tbl_employee_mst_serializer
    queryset = tbl_employee_mst.objects.filter(is_deleted='N')

class employee_registration_view(APIView):
    
    def post(self, request, *args, **kwargs):
        employee_serializer = tbl_employee_mst_serializer(data=request.data['employeeMstForm'])

        print('Employee Password ===>>>',request.data['userForm']['password'])
        request.data['userForm']['password'] = make_password(request.data['userForm']['password'],hasher='default')
        print('Encrypted Employee Password ===>>>',request.data['userForm']['password'])
        user_serializer = UserSerializer(data=request.data['userForm'])

        # send_mail function
        subject = 'Welcome to Rhythmflows'
        message = 'Rhythmflows CMS Welcomes You' + '\n\n' + 'USERNAME: ' + request.data['userForm']['username'] + '\n' + 'PASSWORD: ' + request.data['employeeMstForm']['password']
        recepient = request.data['employeeMstForm']['email']
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        print(employee_serializer.is_valid(),"employee_serializer")
        print(user_serializer.is_valid(),"user_serializer")
        print(user_serializer.errors,"user_serializer")
        # breakpoint()
        if employee_serializer.is_valid() and user_serializer.is_valid():
            employee_serializer.save()
            user_serializer.save()

            request.data['loginMstForm']['user'] = user_serializer['id'].value
            request.data['loginMstForm']['end_user_ref_id'] = employee_serializer['id'].value
            login_serializer = tbl_login_mst_serializer(data=request.data['loginMstForm'])
            print(login_serializer.is_valid(),"login_serializer")
            if login_serializer.is_valid():
                login_serializer.save()

            return Response(employee_serializer.data, status=status.HTTP_201_CREATED)
        else:
          return Response(employee_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        saved_employee = get_object_or_404(tbl_employee_mst.objects.all(), pk=pk)
        employee_serializer = tbl_employee_mst_serializer(instance=saved_employee, data=request.data['employeeMstForm'])
        if employee_serializer.is_valid():
            employee_serializer.save()
            return Response(employee_serializer.data, status=status.HTTP_201_CREATED)
        return Response(employee_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class get_role_ref_id_view(APIView):
    def get(self, request):
        serializer_class = tbl_role_mst.objects.filter(is_deleted='N').filter(company_ref_id=request.GET['COMPANY_ID'])
        serializer_result = RoleSerializer(serializer_class, many=True)
        return Response(serializer_result.data, status=status.HTTP_200_OK)

# User Registration 
class tbl_user_mst_view(viewsets.ModelViewSet):
    serializer_class = tbl_user_mst_serializer
    queryset = tbl_user_mst.objects.filter(is_deleted='N')

class user_registration_view(APIView):
    
    def post(self, request, *args, **kwargs):
        network_user_serializer = tbl_user_mst_serializer(data=request.data['networkUserMst'])

        print('User Password ===>>>',request.data['userFormData']['password'])
        request.data['userFormData']['password'] = make_password(request.data['userFormData']['password'],hasher='default')
        print('Encrypted User Password ===>>>',request.data['userFormData']['password'])
        user_serializer = UserSerializer(data=request.data['userFormData'])

        # send_mail function
        subject = 'Welcome to Rhythmflows'
        message = 'Rhythmflows CMS Welcomes You' + '\n\n' + 'USERNAME: ' + request.data['userFormData']['username'] + '\n' + 'PASSWORD: ' + request.data['networkUserMst']['password']
        recepient = request.data['networkUserMst']['email']
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        
        if network_user_serializer.is_valid() and user_serializer.is_valid():
            network_user_serializer.save()
            user_serializer.save()

            request.data['loginMstFormData']['user'] = user_serializer['id'].value
            request.data['loginMstFormData']['end_user_ref_id'] = network_user_serializer['id'].value
            login_serializer = tbl_login_mst_serializer(data=request.data['loginMstFormData'])
            if login_serializer.is_valid():
                login_serializer.save()

            return Response(network_user_serializer.data, status=status.HTTP_201_CREATED)
        else:
          return Response(network_user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        saved_employee = get_object_or_404(tbl_user_mst.objects.all(), pk=pk)
        network_user_serializer = tbl_user_mst_serializer(instance=saved_employee, data=request.data['networkUserMst'])
        if network_user_serializer.is_valid():
            network_user_serializer.save()
            return Response(network_user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(network_user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class tbl_service_asset_mst_view(viewsets.ModelViewSet):
    serializer_class = tbl_service_asset_mst_serializer
    queryset = tbl_service_asset_mst.objects.filter(is_deleted='N')

class tbl_company_application_link_details_view(viewsets.ModelViewSet):
    serializer_class = tbl_company_application_link_details_serializer
    queryset = tbl_company_application_link_details.objects.filter(is_deleted='N')

class tbl_company_application_link_mst_view(viewsets.ModelViewSet):
    serializer_class = tbl_company_application_link_mst_serializer
    queryset = tbl_company_application_link_mst.objects.filter(is_deleted='N')

class tbl_channel_mst_view(viewsets.ModelViewSet):
    serializer_class = tbl_channel_mst_serializer
    queryset = tbl_channel_mst.objects.filter(is_deleted='N')

class tbl_sla_mst_view(viewsets.ModelViewSet):
    serializer_class = tbl_sla_mst_serializer
    queryset = tbl_sla_mst.objects.filter(is_deleted='N')

class tbl_sla_details_mst_view(viewsets.ModelViewSet):
    serializer_class = tbl_sla_details_mst_serializer
    queryset = tbl_sla_details.objects.filter(is_deleted='N')
    
class tbl_message_mst_view(viewsets.ModelViewSet):
    serializer_class = tbl_message_mst_serializer
    queryset = tbl_message_mst.objects.filter(is_deleted='N')

class RoleViewset(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = tbl_role_mst.objects.filter(is_deleted='N') 

class tbl_role_master_view(viewsets.ModelViewSet):
    serializer_class = tbl_role_master_serializer
    queryset = tbl_role_mst.objects.filter(is_deleted='N')

class tbl_role_application_mst_view(viewsets.ModelViewSet):
    serializer_class = tbl_role_application_mst_serializer
    queryset = tbl_role_application_mst.objects.filter(is_deleted = 'N')   

# Workflow Module
class tbl_workflow_mst_view(viewsets.ModelViewSet):
    serializer_class = tbl_workflow_mst_serializer
    queryset = tbl_workflow_mst.objects.filter(is_deleted='N')    

class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    queryset = tbl_workflow_activity_mst.objects.filter(is_deleted='N')

class LeftPanelViewSet(viewsets.ModelViewSet):
    serializer_class = LeftPanelSerializer
    queryset = tbl_left_panel.objects.filter(is_deleted='N')

class LevelViewSet(viewsets.ModelViewSet):
    serializer_class = LevelSerializer
    queryset = tbl_workflow_level_data_mst.objects.filter(is_deleted='N')

class LevelDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = LevelDetailsSerializer
    queryset = tbl_workflow_level_data_details.objects.filter(is_deleted='N')

class ActionViewSet(viewsets.ModelViewSet):
    serializer_class = ActionSerializer
    queryset = tbl_workflow_action_mst.objects.filter(is_deleted='N')

class GeneralViewSet(viewsets.ModelViewSet):
    @property
    def model(self):
        return apps.get_model(app_label=str(self.kwargs['app_label']), model_name=str(self.kwargs['model_name']))

    def get_queryset(self):
        model = self.model
        return model.objects.all()[:1]           

    def get_serializer_class(self):
        GeneralSerializer.Meta.model = self.model
        return GeneralSerializer
        
class WorkflowViewSet(viewsets.ModelViewSet):
    serializer_class = WorkflowSerializer
    queryset = tbl_workflow_mst.objects.filter(is_deleted='N')

class WorkflowRoutingViewSet(viewsets.ModelViewSet):
    serializer_class = WorkflowRoutingSerializer
    queryset = tbl_workflow_routing_mst.objects.filter(is_deleted='N')

class WorkflowRoutingDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = WorkflowRoutingDetailsSerializer
    queryset = tbl_workflow_routing_details.objects.filter(is_deleted='N')

class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = tbl_employee_mst.objects.filter(is_deleted='N') 

class tbl_role_mst_view(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = tbl_role_master_serializer
    queryset = tbl_role_mst.objects.filter(is_deleted='N')

class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = tbl_currency_mst.objects.filter(is_deleted='N')
    serializer_class = CurrencySerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['currency_code','is_deleted']

    def list(self, request, country_id=None):
        if country_id:
            currency = tbl_currency_mst.objects.filter(country_id = country_id, is_deleted='N')
            serializer = self.get_serializer(currency, many=True)
            return Response(serializer.data)
        else:
            currency = tbl_currency_mst.objects.filter(is_deleted='N')
            serializer = self.get_serializer(currency, many=True)
            return Response(serializer.data)  

class tbl_ticket_status_view(viewsets.ModelViewSet):
    serializer_class = tbl_ticket_status_mst_serializer
    queryset = tbl_ticket_status_mst.objects.filter(is_deleted = 'N')       

class file_view(viewsets.ModelViewSet):
    serializer_class = file_serializer
    queryset = File.objects.all()

class file_upload_view(APIView):
    parser_class = (FileUploadParser,)
    
    def post(self, request, *args, **kwargs):  
      fileSerializer = file_serializer(data=request.data) 
      if fileSerializer.is_valid():
          fileSerializer.save()
          return Response(fileSerializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(fileSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Issue 
class tbl_issue_mst_view(viewsets.ModelViewSet):
    serializer_class = tbl_issue_mst_serializer
    queryset = tbl_issue_mst.objects.filter(is_deleted='N').order_by('-assigned_to_ref_id','-id')   

class tbl_issue_mst_user_view(APIView):
    def get(self, request):
        created_by = request.GET['created_by']
        user_id = request.GET['created_by']
        company_id = request.GET['company_id']

        cursor1 = connection.cursor()
        cursor1.execute("SELECT b.master_key FROM public.portal_tbl_company_mst as a JOIN public.portal_tbl_master as b on a.company_type_ref_id_id=b.id WHERE a.is_deleted='N' and a.id=" + company_id)
        x = dictfetchall(cursor1)

        if(x[0].get('master_key')=='Admin'):
            serializer_class = tbl_issue_mst.objects.filter(is_deleted='N').order_by('-id')
            serializer_result = tbl_issue_mst_serializer(serializer_class, many=True)

        elif(x[0].get('master_key')=='Customer'):
            cursor2 = connection.cursor()
            cursor2.execute("SELECT b.role_name FROM public.portal_tbl_login_mst as a JOIN public.portal_tbl_role_mst as b on a.role_ref_id_id=b.id and a.company_id_id=b.company_ref_id_id WHERE a.is_deleted='N' and a.user_id="+ user_id +" and a.company_id_id=" + company_id)
            y = dictfetchall(cursor2)

            if(y[0].get('role_name')=='Admin'):
                serializer_class = tbl_issue_mst.objects.filter(is_deleted='N').filter(company_ref_id=company_id).order_by('-id')
                serializer_result = tbl_issue_mst_serializer(serializer_class, many=True)
            elif(y[0].get('role_name')=='User'):
                serializer_class = tbl_issue_mst.objects.filter(is_deleted='N').filter(created_by=request.GET['created_by']).order_by('-id')
                serializer_result = tbl_issue_mst_serializer(serializer_class, many=True)
            else:
                pass

        else:
            pass

        return Response(serializer_result.data, status=status.HTTP_201_CREATED) 

class tbl_issue_mst_support_view(ListAPIView):
    def get(self, request):
        created_by=request.GET['created_by']
        cursor = connection.cursor()
        cursor.execute("SELECT end_user_ref_id FROM public.portal_tbl_login_mst where user_id=" + created_by)
        end_user_ref_id = dictfetchall(cursor)
        assigned_to_ref_id = end_user_ref_id[0].get('end_user_ref_id')
        serializer_class = tbl_issue_mst.objects.filter(is_deleted='N').filter(assigned_to_ref_id=assigned_to_ref_id).order_by('-id')
        serializer_result = tbl_issue_mst_serializer(serializer_class, many=True)
        return Response(serializer_result.data, status=status.HTTP_200_OK)  

class tbl_support_problem_issue_mst_view(APIView):
    def get(self, request):
        created_by=request.GET['created_by']
        cursor = connection.cursor()
        cursor.execute("SELECT end_user_ref_id FROM public.portal_tbl_login_mst where user_id=" + created_by)
        end_user_ref_id = dictfetchall(cursor)
        assigned_to_ref_id = end_user_ref_id[0].get('end_user_ref_id')
        serializer_class = tbl_problem_issue_mst.objects.filter(is_deleted='N').filter(assigned_to_ref_id=assigned_to_ref_id).order_by('-id')
        serializer_result = tbl_problem_issue_mst_serializer(serializer_class, many=True)
        return Response(serializer_result.data, status=status.HTTP_200_OK)  

# Help Desk
class help_desk_mst_view(viewsets.ModelViewSet):
    serializer_class = help_desk_mst_serializer
    queryset = tbl_issue_mst.objects.filter(is_deleted='N')

    def get_serializer_context(self):
            context = super(help_desk_mst_view, self).get_serializer_context()
            context.update({"submitAction": self.request.data.get("submitAction")})
            return context
class problem_help_desk_mst_view(viewsets.ModelViewSet):
    serializer_class = problem_help_desk_mst_serializer
    queryset = tbl_problem_issue_mst.objects.filter(is_deleted='N').order_by('-assigned_to_ref_id','-id')

class tbl_problem_issue_mst_view(viewsets.ModelViewSet):
    serializer_class = tbl_problem_issue_mst_serializer
    queryset = tbl_problem_issue_mst.objects.filter(is_deleted='N')  

""" # Help Desk 
class tbl_helpdesk_mst_view(viewsets.ModelViewSet):
    serializer_class = tbl_helpdesk_mst_serializer
    queryset = tbl_helpdesk_mst.objects.filter(is_deleted='N')

# Assignees Action 
class tbl_assignees_action_mst_view(viewsets.ModelViewSet):
    serializer_class = tbl_assignees_action_mst_serializer
    queryset = tbl_assignees_action_mst.objects.filter(is_deleted='N')  """ 

#Assignees Action
class assignees_action_mst_view(viewsets.ModelViewSet):
    serializer_class = assignees_action_mst_serializer
    queryset = tbl_issue_mst.objects.filter(is_deleted='N')

class problem_assignees_action_mst_view(viewsets.ModelViewSet):
    serializer_class = problem_assignees_action_mst_serializer
    queryset = tbl_problem_issue_mst.objects.filter(is_deleted='N')

class get_employee_acc_company(APIView):
    def get(self, request):
        serializer_class = tbl_employee_mst.objects.filter(is_deleted='N').filter(company_ref_id=request.GET['company_ref_id'])
        serializer_result = tbl_employee_mst_serializer(serializer_class, many=True)
        return Response(serializer_result.data, status=status.HTTP_201_CREATED)

class get_user_acc_company(APIView):
    def get(self, request):
        serializer_class = tbl_user_mst.objects.filter(is_deleted='N').filter(company_ref_id=request.GET['company_ref_id'])
        serializer_result = tbl_user_mst_serializer(serializer_class, many=True)
        return Response(serializer_result.data, status=status.HTTP_201_CREATED)

class get_priority_status_acc_service(APIView):
    def get(self, request):
        serializer_class = tbl_company_priority_link_mst.objects.filter(is_deleted='N').filter(company_ref_id=request.GET['company_ref_id'])
        serializer_result = tbl_company_priority_link_mst_serializer(serializer_class, many=True)
        return Response(serializer_result.data, status=status.HTTP_201_CREATED)

class get_application__acc_company(APIView):
    def get(self,request):
        if request.method=='GET':
            cursor = connection.cursor()
            cursor.execute("SELECT a.company_ref_id_id,a.id,b.header_ref_id_id,b.application_ref_id_id,c.name from public.portal_tbl_company_application_link_mst as a join public.portal_tbl_company_application_link_details as b on a.id=b.header_ref_id_id and a.company_ref_id_id ="+request.GET['company_ref_id']+" join public.portal_tbl_service_asset_mst as c on b.application_ref_id_id=c.id and c.is_deleted='N' where a.is_deleted='N' and b.is_deleted='N'")
            applicationData = dictfetchall(cursor)
            return Response(applicationData, status=status.HTTP_200_OK)

""" class get_resolution_time_acc_service(APIView):
    def get(self,request):
        if request.method=='GET':
            cursor = connection.cursor()
            cursor.execute("SELECT a.company_ref_id_id,a.id,b.header_ref_id_id,b.application_ref_id_id,c.name from public.portal_tbl_company_application_link_mst as a join public.portal_tbl_company_application_link_details as b on a.id=b.header_ref_id_id and a.company_ref_id_id ="+request.GET['company_ref_id']+"join public.portal_tbl_service_asset_mst as c on b.application_ref_id_id=c.id and c.is_deleted='N' where a.is_deleted='N' and b.is_deleted='N'")
            applicationData = dictfetchall(cursor)
            return Response(applicationData, status=status.HTTP_200_OK) """
         
# Assign Screen To Role
class tbl_assign_screen_to_role_mst_view(viewsets.ModelViewSet):
    serializer_class = tbl_assign_screen_to_role_mst_Serializer
    queryset = tbl_assign_screen_to_role_mst.objects.filter(is_deleted='N')
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self):
        self.queryset = tbl_assign_screen_to_role_mst.objects.filter(self=self).update(is_deleted='Y',is_active='N')

    def update(self,request, *args,**kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class get_screen_data(APIView):
    
    def get(self,request):
        if request.method=='GET':
            cursor = connection.cursor()
            cursor.execute("SELECT * from public.portal_tbl_assign_screen_to_role_mst where  is_deleted='N' and assigned_to_role_id="+request.GET['assigned_to_role_id'] )
            screenData = dictfetchall(cursor)
            return Response(screenData, status=status.HTTP_200_OK)

class get_data_acc_role(APIView):
    
    def get(self, request):
        serializer_class = tbl_assign_screen_to_role_mst.objects.filter(is_deleted='N').filter(company_ref_id=request.GET['company_ref_id'])
        serializer_result = tbl_assign_screen_to_role_mst(serializer_class, many=True)
        return Response(serializer_result.data, status=status.HTTP_200_OK)

class get_screen_to_role(APIView):
    def get(self,request):
        if request.method=='GET':
            cursor = connection.cursor()
            cursor.execute("SELECT  DISTINCT ON (result.assigned_to_role_id) result.assigned_to_role_id , c.company_name , a.role_name,result.company_ref_id_id,result.id,result from public.portal_tbl_assign_screen_to_role_mst result LEFT JOIN  public.portal_tbl_role_mst a on result.assigned_to_role_id = a.id left join public.portal_tbl_company_mst c on result.company_ref_id_id=c.id")
            ScreenToRoleData = dictfetchall(cursor)
          
            return Response(ScreenToRoleData, status=status.HTTP_200_OK) 

class getrole_acc_to_use(APIView):
    def get(self,request):
        if request.method=='GET':
            cursor = connection.cursor()
            cursor.execute("SELECT distinct result.role_name ,result.company_ref_id_id, result.id from  public.portal_tbl_role_mst  result left JOIN  public.portal_tbl_assign_screen_to_role_mst  a on result.id = a.assigned_to_role_id where result.id is null or  a.assigned_to_role_id  is null AND result.is_deleted='N'")
            RoleData = dictfetchall(cursor)
            return Response(RoleData, status=status.HTTP_200_OK)   

# Assign Roles To Enduser
class AssignRolesToEnduserViewSet(viewsets.ModelViewSet):
    serializer_class = AssignRolesToEnduserSerializer
    queryset = tbl_assign_roles_to_enduser_mst.objects.filter(is_deleted='N') 

# Company Priority link Master
class tbl_company_priority_link_mst_view(viewsets.ModelViewSet):
    serializer_class = tbl_company_priority_link_mst_serializer
    queryset = tbl_company_priority_link_mst.objects.filter(is_deleted='N')

class tbl_company_priority_link_details_view(viewsets.ModelViewSet):
    serializer_class = tbl_company_priority_link_details_mst_serializer
    queryset = tbl_company_priority_link_details.objects.filter(is_deleted='N')
    
# Sidebar
class sidebar_leftpanel(APIView):
    def get(self,request):
        cursor1 = connection.cursor()
        cursor1.execute("SELECT master_key FROM public.portal_tbl_master where master_type='Company Type' and master_value='" + request.GET['company_type_ref_id'] + "'")
        x = dictfetchall(cursor1)
        if(x[0].get('master_key')=='Admin'):
            cursor = connection.cursor()
            cursor.execute("select f.*, e.id, e.form_ref_id_id, d.header_ref_id_id, c.share_id, e.share_id, f.share_id, a.application_id, b.application_id, c.application_id, d.application_id, e.application_id, f.application_id from public.portal_tbl_login_mst as a join public.portal_tbl_employee_mst as b on a.end_user_ref_id = b.id and a.company_id_id = b.company_ref_id_id join public.portal_tbl_assign_roles_to_enduser_mst as c on b.id = c.assigned_to_employee_id and c.company_ref_id_id = b.company_ref_id_id join public.portal_tbl_assign_roles_to_enduser_details as d on c.id = d.header_ref_id_id join public.portal_tbl_assign_screen_to_role_mst as e on e.assigned_to_role_id = d.assigned_to_role_ref_id_id and e.company_ref_id_id = c.company_ref_id_id join public.portal_tbl_left_panel as f on e.form_ref_id_id = f.id where a.user_id = %s and a.company_id_id = %s and a.is_deleted = 'N' and b.is_deleted = 'N' and c.is_deleted = 'N' and d.is_deleted = 'N' and e.is_deleted = 'N' and f.is_deleted = 'N'", (request.GET['AUTH_USER_ID'], request.GET['company_ref_id']))
            sidebar = dictfetchall(cursor)
        elif(x[0].get('master_key')=='Customer'):
            cursor = connection.cursor()
            cursor.execute("select a.form_ref_id_id,a.id,b.* from public.portal_tbl_assign_screen_to_role_mst as a left join public.portal_tbl_left_panel as b on a.form_ref_id_id = b.id where a.company_ref_id_id = "+ request.GET['company_ref_id'] +" and a.is_deleted = 'N' and b.is_deleted = 'N' order by a.form_ref_id_id asc")
            sidebar = dictfetchall(cursor)


        return Response(sidebar, status=status.HTTP_200_OK)

class tbl_leftpanel(APIView):
    def get(self,request):
        cursor = connection.cursor()
        cursor.execute("select * from public.portal_tbl_left_panel where is_deleted = 'N' order by id asc")
        leftpanel = dictfetchall(cursor)
        return Response(leftpanel, status=status.HTTP_200_OK)

class getTotalTicketCount_view(APIView):
    def get(self, request): 
        cursor1 = connection.cursor()
        cursor2 = connection.cursor()
        cursor3 = connection.cursor()
        company_id=request.GET['company_id']
        company_type_ref_id=request.GET['company_type_ref_id']
        cursor = connection.cursor()
        cursor.execute("SELECT master_key FROM public.portal_tbl_master where master_type='Company Type' and master_value='" + company_type_ref_id + "'")
        x = dictfetchall(cursor)
        if(x[0].get('master_key')=='Admin'):
            cursor1.execute("Select((SELECT count(*) as num FROM public.portal_tbl_issue_mst where is_deleted='N')+(SELECT count(*) as num2 FROM public.portal_tbl_problem_issue_mst where is_deleted='N')) as total")
            cursor2.execute("Select((SELECT count(*) as num FROM public.portal_tbl_issue_mst where is_deleted='N' and status_ref_id_id=1)+(SELECT count(*) as num2 FROM public.portal_tbl_problem_issue_mst where is_deleted='N' and status_ref_id_id=1)) as total")
            cursor3.execute("Select((SELECT count(*) as num FROM public.portal_tbl_issue_mst where is_deleted='N' and status_ref_id_id=3)+(SELECT count(*) as num2 FROM public.portal_tbl_problem_issue_mst where is_deleted='N' and status_ref_id_id=3)) as total")
        else:
            cursor1.execute("Select((SELECT count(*) as num FROM public.portal_tbl_issue_mst where is_deleted='N' and company_ref_id_id="+ company_id +")+(SELECT count(*) as num2 FROM public.portal_tbl_problem_issue_mst where is_deleted='N' and company_ref_id_id="+ company_id +")) as total")
            cursor2.execute("Select((SELECT count(*) as num FROM public.portal_tbl_issue_mst where is_deleted='N' and company_ref_id_id="+ company_id +" and status_ref_id_id=1)+(SELECT count(*) as num2 FROM public.portal_tbl_problem_issue_mst where is_deleted='N' and company_ref_id_id="+ company_id +" and status_ref_id_id=1)) as total")
            cursor3.execute("Select((SELECT count(*) as num FROM public.portal_tbl_issue_mst where is_deleted='N' and company_ref_id_id="+ company_id +" and status_ref_id_id=3)+(SELECT count(*) as num2 FROM public.portal_tbl_problem_issue_mst where is_deleted='N' and company_ref_id_id="+ company_id +" and status_ref_id_id=3)) as total")

        total_ticket = dictfetchall(cursor1)
        open_ticket = dictfetchall(cursor2)
        close_ticket = dictfetchall(cursor3)
        response = total_ticket + open_ticket + close_ticket
        return Response(response, status=status.HTTP_201_CREATED)

class getAvgTime_view(APIView):###########################
    def get(self, request): 
        cursor1 = connection.cursor()
        cursor2 = connection.cursor()
        cursor1.execute("SELECT avg(actual_response_time) as average FROM public.portal_tbl_workflow_activity where is_deleted='N' and status='Initiated'")
        cursor2.execute("SELECT avg(b.sla) as average FROM public.portal_tbl_workflow_mst as a left join public.portal_tbl_workflow_activity as b on a.id=b.workflow_ref_id_id where b.is_deleted='N' and b.status='Closed' and b.screen_name like ('%Assignees%')")
        avg_response = dictfetchall(cursor1)
        avg_resolution = dictfetchall(cursor2)
        response = avg_response + avg_resolution
        return Response(response, status=status.HTTP_201_CREATED)

class getPieChartData_view(APIView):
    def get(self, request): 
        cursor1 = connection.cursor()
        ticket_type_ref_id_id=request.GET['ticket_type_ref_id_id']
        status_type_ref_id=request.GET['status_type_ref_id']
        company_id=request.GET['company_id']
        company_type_ref_id=request.GET['company_type_ref_id']
        cursor = connection.cursor()
        cursor.execute("SELECT master_key FROM public.portal_tbl_master where master_type='Company Type' and master_value='" + company_type_ref_id + "'")
        x = dictfetchall(cursor)
        if(x[0].get('master_key')=='Admin'):
            cursor1.execute("select count(b.*),a.master_key from public.portal_tbl_master as a left join public.portal_tbl_issue_mst as b on a.id=b.priority_ref_id_id  and  b.is_deleted='N' and b.status_ref_id_id="+ status_type_ref_id +" and b.ticket_type_ref_id_id="+ ticket_type_ref_id_id +" where a.master_type ='Priority' group by a.master_key")
        else:
            cursor1.execute("select count(b.*),a.master_key from public.portal_tbl_master as a left join public.portal_tbl_issue_mst as b on a.id=b.priority_ref_id_id  and  b.is_deleted='N' and b.status_ref_id_id="+ status_type_ref_id +" and b.ticket_type_ref_id_id="+ ticket_type_ref_id_id +" and company_ref_id_id="+ company_id +" where a.master_type ='Priority' group by a.master_key")
        
        total_ticket = dictfetchall(cursor1)
        return Response(total_ticket, status=status.HTTP_201_CREATED)

class getPieChartDataforProblem_view(APIView):
    def get(self, request): 
        cursor1 = connection.cursor()
        ticket_type_ref_id_id=request.GET['ticket_type_ref_id_id']
        status_type_ref_id=request.GET['status_type_ref_id']
        company_id=request.GET['company_id']
        company_type_ref_id=request.GET['company_type_ref_id']
        cursor = connection.cursor()
        cursor.execute("SELECT master_key FROM public.portal_tbl_master where master_type='Company Type' and master_value='" + company_type_ref_id + "'")
        x = dictfetchall(cursor)
        if(x[0].get('master_key')=='Admin'):
            cursor1.execute("select count(b.*),a.master_key from public.portal_tbl_master as a left join public.portal_tbl_problem_issue_mst as b on a.id=b.priority_ref_id_id  and  b.is_deleted='N' and b.status_ref_id_id="+ status_type_ref_id +" and b.ticket_type_ref_id_id="+ ticket_type_ref_id_id +" where a.master_type ='Priority' group by a.master_key")
        else:
            cursor1.execute("select count(b.*),a.master_key from public.portal_tbl_master as a left join public.portal_tbl_problem_issue_mst as b on a.id=b.priority_ref_id_id  and  b.is_deleted='N' and b.status_ref_id_id="+ status_type_ref_id +" and b.ticket_type_ref_id_id="+ ticket_type_ref_id_id +" and b.company_ref_id_id="+ company_id +" where a.master_type ='Priority' group by a.master_key")

        total_ticket = dictfetchall(cursor1)
        return Response(total_ticket, status=status.HTTP_201_CREATED)

class getIncidentCount_view(APIView):
    def get(self, request): 
        cursor1 = connection.cursor()
        cursor2 = connection.cursor()
        cursor3 = connection.cursor()

        today=request.GET['today']
        week_start=request.GET['week_start']
        week_end=request.GET['week_end']
        month_start=request.GET['month_start']
        month_end=request.GET['month_end']
        ticket_type_ref_id_id=request.GET['ticket_type_ref_id_id']
        status_ref_id_id=request.GET['status_ref_id_id']
        company_id=request.GET['company_id']
        company_type_ref_id=request.GET['company_type_ref_id']
        cursor = connection.cursor()
        cursor.execute("SELECT master_key FROM public.portal_tbl_master where master_type='Company Type' and master_value='" + company_type_ref_id + "'")
        x = dictfetchall(cursor)
        if(x[0].get('master_key')=='Admin'):
            cursor1.execute("SELECT count(*) FROM public.portal_tbl_issue_mst where ticket_type_ref_id_id="+ ticket_type_ref_id_id +" and status_ref_id_id="+ status_ref_id_id +" and CAST(created_date_time AS DATE) ='"+ today +"'")

            cursor2.execute("SELECT count(*) FROM public.portal_tbl_issue_mst where ticket_type_ref_id_id="+ ticket_type_ref_id_id +" and status_ref_id_id="+ status_ref_id_id +" and created_date_time<'"+ week_end +"' and created_date_time>'"+ week_start +"'")

            cursor3.execute("SELECT count(*) FROM public.portal_tbl_issue_mst where ticket_type_ref_id_id="+ ticket_type_ref_id_id +" and status_ref_id_id="+ status_ref_id_id +" and created_date_time<'"+ month_end +"' and created_date_time>'"+ month_start +"'")
        else:
            cursor1.execute("SELECT count(*) FROM public.portal_tbl_issue_mst where ticket_type_ref_id_id="+ ticket_type_ref_id_id +" and company_ref_id_id="+ company_id +" and status_ref_id_id="+ status_ref_id_id +" and CAST(created_date_time AS DATE) ='"+ today +"'")

            cursor2.execute("SELECT count(*) FROM public.portal_tbl_issue_mst where ticket_type_ref_id_id="+ ticket_type_ref_id_id +" and company_ref_id_id="+ company_id +" and status_ref_id_id="+ status_ref_id_id +" and created_date_time<'"+ week_end +"' and created_date_time>'"+ week_start +"'")

            cursor3.execute("SELECT count(*) FROM public.portal_tbl_issue_mst where ticket_type_ref_id_id="+ ticket_type_ref_id_id +" and company_ref_id_id="+ company_id +" and status_ref_id_id="+ status_ref_id_id +" and created_date_time<'"+ month_end +"' and created_date_time>'"+ month_start +"'")

        total_day = dictfetchall(cursor1)
        total_week = dictfetchall(cursor2)
        total_month = dictfetchall(cursor3)

        response = total_day + total_week + total_month

        return Response(response, status=status.HTTP_201_CREATED)

class getProblemCount_view(APIView):
    def get(self, request): 
        cursor1 = connection.cursor()
        cursor2 = connection.cursor()
        cursor3 = connection.cursor()

        today=request.GET['today']
        week_start=request.GET['week_start']
        week_end=request.GET['week_end']
        month_start=request.GET['month_start']
        month_end=request.GET['month_end']
        ticket_type_ref_id_id=request.GET['ticket_type_ref_id_id']
        status_ref_id_id=request.GET['status_ref_id_id']
        company_id=request.GET['company_id']
        company_type_ref_id=request.GET['company_type_ref_id']
        cursor = connection.cursor()
        cursor.execute("SELECT master_key FROM public.portal_tbl_master where master_type='Company Type' and master_value='" + company_type_ref_id + "'")
        x = dictfetchall(cursor)
        if(x[0].get('master_key')=='Admin'):
            cursor1.execute("SELECT count(*) FROM public.portal_tbl_problem_issue_mst where ticket_type_ref_id_id="+ ticket_type_ref_id_id +" and status_ref_id_id="+ status_ref_id_id +" and CAST(created_date_time AS DATE) ='"+ today +"'")

            cursor2.execute("SELECT count(*) FROM public.portal_tbl_problem_issue_mst where ticket_type_ref_id_id="+ ticket_type_ref_id_id +" and status_ref_id_id="+ status_ref_id_id +" and created_date_time<'"+ week_end +"' and created_date_time>'"+ week_start +"'")

            cursor3.execute("SELECT count(*) FROM public.portal_tbl_problem_issue_mst where ticket_type_ref_id_id="+ ticket_type_ref_id_id +" and status_ref_id_id="+ status_ref_id_id +" and created_date_time<'"+ month_end +"' and created_date_time>'"+ month_start +"'")
        else:
            cursor1.execute("SELECT count(*) FROM public.portal_tbl_problem_issue_mst where ticket_type_ref_id_id="+ ticket_type_ref_id_id +" and company_ref_id_id="+ company_id +" and status_ref_id_id="+ status_ref_id_id +" and CAST(created_date_time AS DATE) ='"+ today +"'")

            cursor2.execute("SELECT count(*) FROM public.portal_tbl_problem_issue_mst where ticket_type_ref_id_id="+ ticket_type_ref_id_id +" and company_ref_id_id="+ company_id +" and status_ref_id_id="+ status_ref_id_id +" and created_date_time<'"+ week_end +"' and created_date_time>'"+ week_start +"'")

            cursor3.execute("SELECT count(*) FROM public.portal_tbl_problem_issue_mst where ticket_type_ref_id_id="+ ticket_type_ref_id_id +" and company_ref_id_id="+ company_id +" and status_ref_id_id="+ status_ref_id_id +" and created_date_time<'"+ month_end +"' and created_date_time>'"+ month_start +"'")
        
       
        total_day = dictfetchall(cursor1)
        total_week = dictfetchall(cursor2)
        total_month = dictfetchall(cursor3)

        response = total_day + total_week + total_month

        return Response(response, status=status.HTTP_201_CREATED)
class get_data(APIView):
    
    def get(self,request):
        if request.method=='GET':
            cursor = connection.cursor()
            cursor.execute("SELECT * from public.portal_tbl_assign_screen_to_role_mst where  is_deleted='N' and assigned_to_role_id="+request.GET['assigned_to_role_id']+ "and company_ref_id_id="+request.GET['company_ref_id'] )
            screenData = dictfetchall(cursor)
            return Response(screenData, status=status.HTTP_200_OK)

class tbl_asset_mst_view(viewsets.ModelViewSet):
    serializer_class = tbl_asset_mst_serializer
    queryset = tbl_asset_mst.objects.filter(is_deleted='N')

class max_issue_id_view(APIView):
    def get(self,request):
        cursor = connection.cursor()
        cursor.execute("select max(id) from public.portal_tbl_issue_mst")
        max_issue_id = dictfetchall(cursor)
        return Response(max_issue_id, status=status.HTTP_200_OK)

class max_problem_issue_id_view(APIView):
    def get(self,request):
        cursor = connection.cursor()
        cursor.execute("select max(id) from public.portal_tbl_problem_issue_mst")
        max_problem_issue_id = dictfetchall(cursor)
        return Response(max_problem_issue_id, status=status.HTTP_200_OK)

class getTotalResolutionByForm_view(APIView):
    def get(self, request): 
        cursor1 = connection.cursor()
        form_ref_id_id=request.GET['form_ref_id_id']
        cursor1.execute("SELECT sum(actual_resolution_time) FROM public.portal_tbl_workflow_activity where form_ref_id=" + form_ref_id_id)
        total_resolution_time = dictfetchall(cursor1)
        return Response(total_resolution_time, status=status.HTTP_201_CREATED)

class getSLAVioResponseTime_view(APIView):##################################
    def get(self, request): 
        cursor1 = connection.cursor()
        month_start=request.GET['month_start']
        month_end=request.GET['month_end']
        cursor1.execute("select (avg(sla-actual_response_time))::numeric(10,2) as diff FROM public.portal_tbl_workflow_activity where created_date_time<='" + month_end + "' and created_date_time>='" + month_start + "' group by form_ref_id")
        sla_response_time = dictfetchall(cursor1)
        return Response(sla_response_time, status=status.HTTP_201_CREATED)

class getSLAVioResolutionTime_view(APIView):####################################
    def get(self, request): 
        cursor1 = connection.cursor()
        month_start=request.GET['month_start']
        month_end=request.GET['month_end']
        cursor1.execute("select (avg(sla-actual_resolution_time))::numeric(10,2) as diff FROM public.portal_tbl_workflow_activity where created_date_time<='" + month_end + "' and created_date_time>='" + month_start + "' group by form_ref_id")
        sla_resolution_time = dictfetchall(cursor1)
        return Response(sla_resolution_time, status=status.HTTP_201_CREATED)

class getEscalationIssue_view(APIView):
    def get(self, request): 
        cursor1 = connection.cursor()
        month_start=request.GET['month_start']
        month_end=request.GET['month_end']
        company_id=request.GET['company_id']
        ticket_type_ref_id=request.GET['ticket_type_ref_id']
        company_type_ref_id=request.GET['company_type_ref_id']
        cursor = connection.cursor()
        cursor.execute("SELECT master_key FROM public.portal_tbl_master where master_type='Company Type' and master_value='" + company_type_ref_id + "'")
        x = dictfetchall(cursor)
        if(x[0].get('master_key')=='Admin'):
            cursor1.execute("SELECT a.id,a.ticket_type_ref_id_id,avg(b.escalation_date_time - b.end_date_time) as diff from public.portal_tbl_issue_mst as a join public.portal_tbl_workflow_activity as b on b.form_ref_id = a.id where a.ticket_type_ref_id_id="+ ticket_type_ref_id +" and a.created_date_time<='" + month_end + "' and a.created_date_time>='" + month_start + "' group by a.id")
        else:
            cursor1.execute("SELECT a.id,a.ticket_type_ref_id_id,avg(b.escalation_date_time - b.end_date_time) as diff from public.portal_tbl_issue_mst as a join public.portal_tbl_workflow_activity as b on b.form_ref_id = a.id where a.ticket_type_ref_id_id="+ ticket_type_ref_id +" and a.company_ref_id_id="+ company_id +" and a.created_date_time<='" + month_end + "' and a.created_date_time>='" + month_start + "' group by a.id")

        escalation_diff_issue = dictfetchall(cursor1)
        return Response(escalation_diff_issue, status=status.HTTP_201_CREATED)

class getEscalationProblemIssue_view(APIView):
    def get(self, request): 
        cursor1 = connection.cursor()
        month_start=request.GET['month_start']
        month_end=request.GET['month_end']
        ticket_type_ref_id=request.GET['ticket_type_ref_id']
        company_id=request.GET['company_id']
        company_type_ref_id=request.GET['company_type_ref_id']
        cursor = connection.cursor()
        cursor.execute("SELECT master_key FROM public.portal_tbl_master where master_type='Company Type' and master_value='" + company_type_ref_id + "'")
        x = dictfetchall(cursor)
        if(x[0].get('master_key')=='Admin'):
            cursor1.execute("SELECT a.id,a.ticket_type_ref_id_id,avg(b.escalation_date_time - b.end_date_time) as diff from public.portal_tbl_problem_issue_mst as a join public.portal_tbl_workflow_activity as b on b.form_ref_id = a.id where a.ticket_type_ref_id_id="+ ticket_type_ref_id +" and a.created_date_time<='" + month_end + "' and a.created_date_time>='" + month_start + "' group by a.id")
        else:
            cursor1.execute("SELECT a.id,a.ticket_type_ref_id_id,avg(b.escalation_date_time - b.end_date_time) as diff from public.portal_tbl_problem_issue_mst as a join public.portal_tbl_workflow_activity as b on b.form_ref_id = a.id where a.ticket_type_ref_id_id="+ ticket_type_ref_id +" and a.company_ref_id_id="+ company_id +" and a.created_date_time<='" + month_end + "' and a.created_date_time>='" + month_start + "' group by a.id")
        escalation_diff_problemissue = dictfetchall(cursor1)
        return Response(escalation_diff_problemissue, status=status.HTTP_201_CREATED)

class getAllEmployeesByUserIdView(APIView):
    def get(self, request): 
        cursor1 = connection.cursor()
        cursor1.execute("select  a.id, b.end_user_ref_id, a.company_ref_id_id, b.company_id_id, c.id as user_id, a.first_name from public.portal_tbl_employee_mst as a join public.portal_tbl_login_mst as b on a.id = b.end_user_ref_id and a.company_ref_id_id = b.company_id_id join public.auth_user as c on b.user_id = c.id where a.is_deleted = 'N' and b.is_deleted = 'N'")
        employee_data = dictfetchall(cursor1)
        return Response(employee_data, status=status.HTTP_201_CREATED)

class getcompanybycompanyid_view(APIView):
    def get(self, request):
        company_type_ref_id=request.GET['company_type_ref_id']
        company_id=request.GET['company_id']
        cursor = connection.cursor()
        cursor.execute("SELECT master_key FROM public.portal_tbl_master where master_type='Company Type' and master_value='" + company_type_ref_id + "'")
        x = dictfetchall(cursor)
        if(x[0].get('master_key')=='Admin'):
            print(x[0].get('master_key'))
            serializer_class = tbl_company_mst.objects.filter(is_deleted='N')
            queryset = tbl_company_mst_serializer(serializer_class, many=True)
        else:
            print(x[0].get('master_key'))
            serializer_class = tbl_company_mst.objects.filter(is_deleted='N').filter(company_id=company_id)
            queryset = tbl_company_mst_serializer(serializer_class, many=True)
        
        return Response(queryset.data, status=status.HTTP_200_OK)

class getSLAPriorityData_view(APIView):
    def get(self, request):
        priority_id=request.GET['priority_id']
        company_id=request.GET['company_id']
        cursor = connection.cursor()
        cursor.execute("SELECT a.* FROM public.portal_tbl_company_priority_link_details as a JOIN public.portal_tbl_company_priority_link_mst as b on b.id=a.header_ref_id_id where b.company_ref_id_id=" + company_id + " and b.revision_status='Effective' and a.is_deleted='N' and b.is_deleted='N' and a.priority_ref_id_id=" + priority_id )
        priority_time_data = dictfetchall(cursor)
        return Response(priority_time_data, status=status.HTTP_201_CREATED)

class inActivateUser_view(APIView):
    def get(self, request):
        user_id=request.GET['user_id']
        cursor = connection.cursor()
        cursor.execute("SELECT a.id FROM public.auth_user as a JOIN public.portal_tbl_login_mst as b on b.user_id=a.id JOIN public.portal_tbl_user_mst as c on c.id=b.end_user_ref_id where c.id=" + user_id)
        auth_id = dictfetchall(cursor)[0].get('id')
        cursor1 = connection.cursor()
        cursor1.execute("Update public.auth_user SET is_active='false' WHERE id=" + str(auth_id))
        return Response(auth_id, status=status.HTTP_201_CREATED)