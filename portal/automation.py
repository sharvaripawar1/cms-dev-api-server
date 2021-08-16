#from asyncio.windows_events import NULL
from .models import *
from django.apps import apps 
from datetime import datetime
from datetime import timedelta
import pytz
import sys

fieldname_values_dict = {}
fieldname_level_dict = {}
approval_fieldname = None
approval_dict = {}
max_level_approval_required = None
workflow_ref_id = None
workflow_details_ids = []
workflow_subdetails_details_ids = []



def initiate_activity_tbl(left_panel_id, form_ref_id, form_company_ref_id, form_service_asset_ref_id, form_ticket_type_ref_id, form_priority_ref_id):

    print('Inside function initiate_activity_tbl')
    max_level_approval_required = 1
    obtained_left_panel = tbl_left_panel.objects.filter(id=left_panel_id).filter(is_deleted='N')
    print('Obtained Left Panel Table 1 : ',obtained_left_panel)
    print('Left Panel ID : ',left_panel_id)
    print('Form Ref ID : ',form_ref_id)

    #screen_names = tbl_left_panel.objects.filter()

    screen_name = tbl_left_panel.objects.filter(id=left_panel_id).filter(is_deleted='N')[0].form_name
    print('Screen Name 1 : ', screen_name)
    if obtained_left_panel:
        ### Fetch model name for left panel object 
        left_panel_model_name = obtained_left_panel.first().backend_model_name
        print('Left Panel Model Name : ',left_panel_model_name)
        obtained_backend_model_name = left_panel_model_name  ############## Variable inconsistency for field name
        print('Obtained Left Panel Table 2 : ', obtained_backend_model_name)
        obtained_model = apps.get_model('portal', obtained_backend_model_name)
        left_panel_object = obtained_model.objects.filter(id=form_ref_id).first() ### Used to get actual value of field with constraints
        print('Obtained Model : ',obtained_model)
        print('Left Panel Object : ',left_panel_object)
        ### Traverse through workflow to get level rules
        #selected_level = tbl_workflow_level_data_mst.objects.filter(level = 1, level_name="Help Desk Page")
        '''selected_level_ids = []
        for sl in selected_level:
            selected_level_ids.append(sl.id)'''
        #print('Selected Level', selected_level.first())

        print('form_company_ref_id : ',form_company_ref_id)
        print('form_service_asset_ref_id : ',form_service_asset_ref_id)
        print('form_ticket_type_ref_id : ',form_ticket_type_ref_id)
        print('form_priority_ref_id : ',form_priority_ref_id)

        sla_header_data = tbl_sla_mst.objects.filter(company_ref_id=form_company_ref_id,revision_status='Effective').filter(is_deleted='N')
        print('SLA Header data : ',sla_header_data)
        for sla_id_data in sla_header_data:
            sla_header_id = sla_id_data.id
            print('sla_header_id : ',sla_header_id)
            sla_escalation_data = tbl_sla_details.objects.filter(header_ref_id=sla_header_id,  application_ref_id=form_service_asset_ref_id, ticket_type_ref_id=form_ticket_type_ref_id, priority_ref_id=form_priority_ref_id).filter(is_deleted='N')
            print('sla_escalation_data : ',sla_escalation_data)
            if sla_escalation_data:
                for escalation_data in sla_escalation_data:
                    escalation_hours = escalation_data.escalation_time
            else:
                escalation_hours = 0
        print('escalation hours', escalation_hours)
        hours_added = timedelta(hours = round(escalation_hours))
        print('hours added', hours_added)
                
        header_data = tbl_workflow_mst.objects.filter(company_ref_id=form_company_ref_id,service_asset_ref_id=form_service_asset_ref_id).filter(is_deleted='N')
        print('Header data : ',header_data)
        for header_id_data in header_data:
                header_id = header_id_data.id
                level_rules_data = tbl_workflow_details.objects.filter(header_ref_id=header_id, left_panel_ref_id=left_panel_id).filter(is_deleted='N')
                if level_rules_data:
                    level_rules = level_rules_data
        print('Level Rules : ',level_rules)
        print('Screen Name 2 : ',screen_name)  

        if level_rules:
            ### Populate workflow_details_ids and approval_dict = {level: amount}
            workflow_details_ids = []
            for level_rule in level_rules:
                workflow_ref_id = level_rule.header_ref_id
                approval_fieldname = level_rule.field_name
                approval_dict[level_rule.id] = level_rule.approval_field_value
                workflow_details_ids.append(level_rule.id)
                print('Level Rule : ', level_rule)
                print('Dict : ', approval_dict)

            print('Workflow Details IDs : ', workflow_details_ids)
            print('Workflow Sub Details IDs : ', [x.id for x in tbl_workflow_sub_details.objects.filter(header_ref_id=workflow_ref_id, details_ref_id__in=workflow_details_ids)])
            print('Level Rules - Field Name : ', level_rules.first().field_name)
            print('Approval Dict : ', approval_dict)
            print('Approval Field Name : ', approval_fieldname)
            print('Workflow Ref ID : ', workflow_ref_id.id)
            print('Screen Name 3 : ',screen_name)
            print('Max Level Approval Required : ', max_level_approval_required)

            status_details_for_screens = {"Issue":"Closed", "Help Desk Incident":"Closed", "Assignees Action Incident":"Closed"}

            for subdetails_entry in tbl_workflow_sub_details.objects.filter(id__in=[x.id for x in tbl_workflow_sub_details.objects.filter(header_ref_id=workflow_ref_id, details_ref_id__in=workflow_details_ids)]).order_by('id'):
                print('Sub Details Entry : ', subdetails_entry)
                if subdetails_entry.level_sub_details_ref_id.level <= max_level_approval_required:
                    blob_1 = None
                    if screen_name=="Issue":
                        print('In Issue')
                        
                        blob_1 = tbl_workflow_activity(
                                share_id = tbl_left_panel.objects.get(pk=left_panel_id).share_id,
                                workflow_ref_id = workflow_ref_id,
                                form_ref_id = form_ref_id,
                                screen_name = screen_name,
                                level = subdetails_entry.level_sub_details_ref_id.level,
                                is_assigned_role_person = 'Y' if subdetails_entry.role_ref_id==0 else 'N',
                                assigned_role = 'NA' if subdetails_entry.role_ref_id.id==0 else subdetails_entry.role_ref_id.id,
                                assigned_person = subdetails_entry.employee_ref_id if subdetails_entry.role_ref_id==0 else 'NA',
                                activity_ref_id = subdetails_entry.activity_ref_id,
                                action_ref_id = subdetails_entry.action_ref_id,
                                #user_action_ref_id = -1,
                                sequence_number = subdetails_entry.sequence_number,
                                next_sequence_number = subdetails_entry.next_sequence_number,
                                status = 'Closed',
                                sla = subdetails_entry.sla_response_time,
                                start_date_time = datetime.now().astimezone(pytz.utc),
                                escalation_date_time = datetime.now().astimezone(pytz.utc) + hours_added,
                                end_date_time = datetime.now().astimezone(pytz.utc),
                                is_active = 'Y',
                                is_deleted = 'N',
                                sub_application_id = subdetails_entry.sub_application_id,
                                application_id = subdetails_entry.application_id,
                            )
                        print('Blob 1 A : ', blob_1)
                    elif screen_name=="Help Desk Incident":
                        print('In Help Desk', subdetails_entry.sequence_number, subdetails_entry.activity_ref_id.id, subdetails_entry.action_ref_id.id)
                        if subdetails_entry.sequence_number == 1 and subdetails_entry.activity_ref_id.id == 2 and subdetails_entry.action_ref_id.id ==1:
                            print('In Elif - If')
                            print('Sub Details Role ID - Assigned Role : ', subdetails_entry.role_ref_id.id)
                            blob_1 = tbl_workflow_activity(
                                share_id = tbl_left_panel.objects.get(pk=left_panel_id).share_id,
                                workflow_ref_id = workflow_ref_id,
                                form_ref_id = form_ref_id,
                                screen_name = screen_name,
                                level = subdetails_entry.level_sub_details_ref_id.level,
                                is_assigned_role_person = 'Y' if subdetails_entry.role_ref_id==0 else 'N',
                                assigned_role = 'NA' if subdetails_entry.role_ref_id.id==0 else subdetails_entry.role_ref_id.id,
                                assigned_person = subdetails_entry.employee_ref_id if subdetails_entry.role_ref_id==0 else 'NA',
                                activity_ref_id = subdetails_entry.activity_ref_id,
                                action_ref_id = subdetails_entry.action_ref_id,
                                user_action_ref_id = subdetails_entry.action_ref_id,
                                sequence_number = subdetails_entry.sequence_number,
                                next_sequence_number = subdetails_entry.next_sequence_number,
                                status = 'Initiated',
                                start_date_time = datetime.now().astimezone(pytz.utc),
                                escalation_date_time = datetime.now().astimezone(pytz.utc) + hours_added,
                                sla = subdetails_entry.sla_response_time,
                                is_active = 'Y',
                                is_deleted = 'N',
                                sub_application_id = subdetails_entry.sub_application_id,
                                application_id = subdetails_entry.application_id,
                            )
                            status_details_for_screens[screen_name] = "Initiated"
                            print('Blob 1 B : ', blob_1)
                        else:
                            print('In Elif - Else')
                            print('Sub Details Role ID - Assigned Role : ', subdetails_entry.role_ref_id)
                            blob_1 = tbl_workflow_activity(
                                share_id = tbl_left_panel.objects.get(pk=left_panel_id).share_id,
                                workflow_ref_id = workflow_ref_id,
                                form_ref_id = form_ref_id,
                                screen_name = screen_name,
                                level = subdetails_entry.level_sub_details_ref_id.level,
                                is_assigned_role_person = 'Y' if subdetails_entry.role_ref_id==0 else 'N',
                                assigned_role = 'NA' if subdetails_entry.role_ref_id.id==0 else subdetails_entry.role_ref_id.id,
                                assigned_person = subdetails_entry.employee_ref_id if subdetails_entry.role_ref_id==0 else 'NA',
                                activity_ref_id = subdetails_entry.activity_ref_id,
                                action_ref_id = subdetails_entry.action_ref_id,
                                #user_action_ref_id = -1,
                                sequence_number = subdetails_entry.sequence_number,
                                next_sequence_number = subdetails_entry.next_sequence_number,
                                status = 'Not Initiated',
                                sla = subdetails_entry.sla_response_time,
                                is_active = 'Y',
                                is_deleted = 'N',
                                sub_application_id = subdetails_entry.sub_application_id,
                                application_id = subdetails_entry.application_id,
                            )
                            print('Blob 1 C : ', blob_1.workflow_ref_id)

                    elif screen_name=="Assignees Action Incident":
                        print('In Assignees Action', subdetails_entry.sequence_number, subdetails_entry.activity_ref_id.id, subdetails_entry.action_ref_id.id)
                        if subdetails_entry.sequence_number == 1 and subdetails_entry.activity_ref_id.id == 2 and subdetails_entry.action_ref_id.id ==1:
                            print('In Elif - If')
                            print('Sub Details Role ID - Assigned Role : ', subdetails_entry.role_ref_id.id)
                            blob_1 = tbl_workflow_activity(
                                share_id = tbl_left_panel.objects.get(pk=left_panel_id).share_id,
                                workflow_ref_id = workflow_ref_id,
                                form_ref_id = form_ref_id,
                                screen_name = screen_name,
                                level = subdetails_entry.level_sub_details_ref_id.level,
                                is_assigned_role_person = 'Y' if subdetails_entry.role_ref_id==0 else 'N',
                                assigned_role = 'NA' if subdetails_entry.role_ref_id.id==0 else subdetails_entry.role_ref_id.id,
                                assigned_person = subdetails_entry.employee_ref_id if subdetails_entry.role_ref_id==0 else 'NA',
                                activity_ref_id = subdetails_entry.activity_ref_id,
                                action_ref_id = subdetails_entry.action_ref_id,
                                user_action_ref_id = subdetails_entry.action_ref_id,
                                sequence_number = subdetails_entry.sequence_number,
                                next_sequence_number = subdetails_entry.next_sequence_number,
                                status = 'Initiated',
                                start_date_time = datetime.now().astimezone(pytz.utc),
                                escalation_date_time = datetime.now().astimezone(pytz.utc) + hours_added,
                                sla = subdetails_entry.sla_response_time,
                                is_active = 'Y',
                                is_deleted = 'N',
                                sub_application_id = subdetails_entry.sub_application_id,
                                application_id = subdetails_entry.application_id,
                            )
                            status_details_for_screens[screen_name] = "Initiated"
                            print('Blob 1 B : ', blob_1)
                        else:
                            print('In Elif - Else')
                            print('Sub Details Role ID - Assigned Role : ', subdetails_entry.role_ref_id)
                            blob_1 = tbl_workflow_activity(
                                share_id = tbl_left_panel.objects.get(pk=left_panel_id).share_id,
                                workflow_ref_id = workflow_ref_id,
                                form_ref_id = form_ref_id,
                                screen_name = screen_name,
                                level = subdetails_entry.level_sub_details_ref_id.level,
                                is_assigned_role_person = 'Y' if subdetails_entry.role_ref_id==0 else 'N',
                                assigned_role = 'NA' if subdetails_entry.role_ref_id.id==0 else subdetails_entry.role_ref_id.id,
                                assigned_person = subdetails_entry.employee_ref_id if subdetails_entry.role_ref_id==0 else 'NA',
                                activity_ref_id = subdetails_entry.activity_ref_id,
                                action_ref_id = subdetails_entry.action_ref_id,
                                #user_action_ref_id = -1,
                                sequence_number = subdetails_entry.sequence_number,
                                next_sequence_number = subdetails_entry.next_sequence_number,
                                status = 'Not Initiated',
                                sla = subdetails_entry.sla_response_time,
                                is_active = 'Y',
                                is_deleted = 'N',
                                sub_application_id = subdetails_entry.sub_application_id,
                                application_id = subdetails_entry.application_id,
                            )
                            print('Blob 1 C : ', blob_1.workflow_ref_id)

                    else:
                        print('In else', subdetails_entry.sequence_number, subdetails_entry.activity_ref_id.id, subdetails_entry.action_ref_id.id)
                        if subdetails_entry.sequence_number == 1:
                            print('In Else - If')
                            print('Sub Details Role ID - Assigned Role : ', subdetails_entry.role_ref_id.id)
                            blob_1 = tbl_workflow_activity(
                                share_id = tbl_left_panel.objects.get(pk=left_panel_id).share_id,
                                workflow_ref_id = workflow_ref_id,
                                form_ref_id = form_ref_id,
                                screen_name = screen_name,
                                level = subdetails_entry.level_sub_details_ref_id.level,
                                is_assigned_role_person = 'Y' if subdetails_entry.role_ref_id==0 else 'N',
                                assigned_role = 'NA' if subdetails_entry.role_ref_id.id==0 else subdetails_entry.role_ref_id.id,
                                assigned_person = subdetails_entry.employee_ref_id if subdetails_entry.role_ref_id==0 else 'NA',
                                activity_ref_id = subdetails_entry.activity_ref_id,
                                action_ref_id = subdetails_entry.action_ref_id,
                                user_action_ref_id = subdetails_entry.action_ref_id,
                                sequence_number = subdetails_entry.sequence_number,
                                next_sequence_number = subdetails_entry.next_sequence_number,
                                status = 'Initiated',
                                start_date_time = datetime.now().astimezone(pytz.utc),
                                escalation_date_time = datetime.now().astimezone(pytz.utc) + hours_added,
                                sla = subdetails_entry.sla_response_time,
                                is_active = 'Y',
                                is_deleted = 'N',
                                sub_application_id = subdetails_entry.sub_application_id,
                                application_id = subdetails_entry.application_id,
                            )
                            status_details_for_screens[screen_name] = "Initiated"
                            print('Blob 1 B : ', blob_1)
                        else:
                            print('In Else - Else')
                            print('Sub Details Role ID - Assigned Role : ', subdetails_entry.role_ref_id)
                            blob_1 = tbl_workflow_activity(
                                share_id = tbl_left_panel.objects.get(pk=left_panel_id).share_id,
                                workflow_ref_id = workflow_ref_id,
                                form_ref_id = form_ref_id,
                                screen_name = screen_name,
                                level = subdetails_entry.level_sub_details_ref_id.level,
                                is_assigned_role_person = 'Y' if subdetails_entry.role_ref_id==0 else 'N',
                                assigned_role = 'NA' if subdetails_entry.role_ref_id.id==0 else subdetails_entry.role_ref_id.id,
                                assigned_person = subdetails_entry.employee_ref_id if subdetails_entry.role_ref_id==0 else 'NA',
                                activity_ref_id = subdetails_entry.activity_ref_id,
                                action_ref_id = subdetails_entry.action_ref_id,
                                #user_action_ref_id = -1,
                                sequence_number = subdetails_entry.sequence_number,
                                next_sequence_number = subdetails_entry.next_sequence_number,
                                status = 'Not Initiated',
                                sla = subdetails_entry.sla_response_time,
                                is_active = 'Y',
                                is_deleted = 'N',
                                sub_application_id = subdetails_entry.sub_application_id,
                                application_id = subdetails_entry.application_id,
                            )
                            print('Blob 1 C : ', blob_1.workflow_ref_id)

                    print(screen_name , "Screen Name")
                    print(blob_1 , "blob_1")
                    if blob_1 != None:
                        blob_1.save()
                        print('Blob 1 C : ', blob_1)
                        print('Records inserted in tbl_workflow_activity!')
                    blob_2 = tbl_workflow_activity_notification_details(
                        header_ref_id = blob_1,
                        is_notification_applicable= 'Y' if subdetails_entry.is_reminder_required == True else 'N',
                        is_email = 'Y' if subdetails_entry.is_email_required else 'N',
                        is_text_message = 'Y' if subdetails_entry.is_sms_required else 'N',
                        is_whatsapp = 'Y' if subdetails_entry.is_whatsapp_required else 'N',
                        is_additional_email = 'Y' if subdetails_entry.is_whatsapp_required else 'N',
                        ### is_additional_notification_to_senior_management = ,                             #################### ASK
                        sub_application_id = subdetails_entry.sub_application_id,
                        application_id = subdetails_entry.application_id
                    )
                    blob_2.save()
                    print('Blob 2 : ', blob_2)
                    print('Records inserted in tbl_workflow_activity_notification_details!')

            for routing_details_entry in tbl_workflow_routing_details.objects.filter(workflow_ref_id=workflow_ref_id.id):
                print('Routing Details Entry : ', routing_details_entry)
                if routing_details_entry:
                    if routing_details_entry.sequence_number == 1 and screen_name != "Assignees Action Incident":
                        blob_3 = tbl_workflow_routing_activity(
                            workflow_routing_ref_id=routing_details_entry.header_ref_id,
                            workflow_routing_details_ref_id = routing_details_entry,
                            sequence_number = routing_details_entry.sequence_number,
                            next_sequence_number = routing_details_entry.next_sequence_number,
                            status = status_details_for_screens[screen_name],
                            sub_application_id= routing_details_entry.sub_application_id,
                            application_id= routing_details_entry.application_id
                        )
                        blob_3.save()
                        print('Blob 3 A : ', blob_3)
                        print('Records inserted in tbl_workflow_routing_activity!')
                    elif screen_name != "Assignees Action Incident":
                        blob_3 = tbl_workflow_routing_activity(
                            workflow_routing_ref_id=routing_details_entry.header_ref_id,
                            workflow_routing_details_ref_id = routing_details_entry,
                            sequence_number = routing_details_entry.sequence_number,
                            next_sequence_number = routing_details_entry.next_sequence_number,
                            status = status_details_for_screens[screen_name],
                            sub_application_id= routing_details_entry.sub_application_id,
                            application_id= routing_details_entry.application_id
                        )
                        blob_3.save()
                        print('Blob 3 B : ', blob_3)
                        print('Records inserted in tbl_workflow_routing_activity!')



def routing_activity_for_Assignees_Action(left_panel_id, form_ref_id, form_company_ref_id, form_service_asset_ref_id):

    print('Inside function routing_activity_for_Assignees_Action')
    screen_name = tbl_left_panel.objects.filter(id=left_panel_id).filter(is_deleted='N')[0].form_name
    max_level_approval_required = 1
    obtained_left_panel = tbl_left_panel.objects.filter(id=left_panel_id).filter(is_deleted='N')

    if obtained_left_panel:
        ### Fetch model name for left panel object 
        left_panel_model_name = obtained_left_panel.first().backend_model_name
        obtained_backend_model_name = left_panel_model_name  ############## Variable inconsistency for field name
        obtained_model = apps.get_model('portal', obtained_backend_model_name)
        left_panel_object = obtained_model.objects.filter(id=form_ref_id).first() ### Used to get actual value of field with constraints
        ### Traverse through workflow to get level rules
        #selected_level = tbl_workflow_level_data_mst.objects.filter(level = 1, level_name="Help Desk Page")
        '''selected_level_ids = []
        for sl in selected_level:
            selected_level_ids.append(sl.id)'''
        #print('Selected Level', selected_level.first())
        print('form_company_ref_id : ',form_company_ref_id)
        print('form_service_asset_ref_id : ',form_service_asset_ref_id)
        header_data = tbl_workflow_mst.objects.filter(company_ref_id=form_company_ref_id,service_asset_ref_id=form_service_asset_ref_id).filter(is_deleted='N')
        print('Header data : ',header_data)
        for header_id_data in header_data:
                header_id = header_id_data.id
                level_rules_data = tbl_workflow_details.objects.filter(header_ref_id=header_id, left_panel_ref_id=left_panel_id).filter(is_deleted='N')
                if level_rules_data:
                    level_rules = level_rules_data
        print('Level Rules : ',level_rules)
        
        print('Screen Name 2 : ',screen_name)  
        if level_rules:
            ### Populate workflow_details_ids and approval_dict = {level: amount}
            workflow_details_ids = []
            for level_rule in level_rules:
                workflow_ref_id = level_rule.header_ref_id
                approval_fieldname = level_rule.field_name
                approval_dict[level_rule.id] = level_rule.approval_field_value
                workflow_details_ids.append(level_rule.id)
                print('Level Rule : ', level_rule)
                print('Dict : ', approval_dict)

    for routing_details_entry in tbl_workflow_routing_details.objects.filter(workflow_ref_id=workflow_ref_id.id):
        print('Routing Details Entry : ', routing_details_entry)
        if routing_details_entry:
            if routing_details_entry.sequence_number == 1:
                blob_3 = tbl_workflow_routing_activity(
                    workflow_routing_ref_id=routing_details_entry.header_ref_id,
                    workflow_routing_details_ref_id = routing_details_entry,
                    sequence_number = routing_details_entry.sequence_number,
                    next_sequence_number = routing_details_entry.next_sequence_number,
                    status = 'Not Initiated',
                    sub_application_id= routing_details_entry.sub_application_id,
                    application_id= routing_details_entry.application_id
                )
                blob_3.save()
                print('Records inserted in tbl_workflow_routing_activity!')
            else:
                blob_3 = tbl_workflow_routing_activity(
                    workflow_routing_ref_id=routing_details_entry.header_ref_id,
                    workflow_routing_details_ref_id = routing_details_entry,
                    sequence_number = routing_details_entry.sequence_number,
                    next_sequence_number = routing_details_entry.next_sequence_number,
                    status = 'Not Initiated',
                    sub_application_id= routing_details_entry.sub_application_id,
                    application_id= routing_details_entry.application_id
                )
                blob_3.save()
                print('Records inserted in tbl_workflow_routing_activity!')



def update_activity_tbl(left_panel_id, form_ref_id, user_action_ref_id, form_company_ref_id, form_service_asset_ref_id):
    print('Inside function update_activity_tbl',left_panel_id, form_ref_id, user_action_ref_id)
    max_level_approval_required = 0
    next_triggered_sequence_number = None
    next_triggered_routing_sequence_number = None
    obtained_left_panel = tbl_left_panel.objects.filter(id=left_panel_id)
    is_workflow_activity_completed = False
    is_workflow_routing_activity_completed = False

    if obtained_left_panel:
        ### Fetch model name for left panel object 

        left_panel_model_name = obtained_left_panel.first().backend_model_name
        obtained_backend_model_name = left_panel_model_name  ############## Variable inconsistency for field name
        obtained_model = apps.get_model('portal', obtained_backend_model_name)
        left_panel_object = obtained_model.objects.filter(id=form_ref_id).first() ### Used to get actual value of field with constraints

        ### Traverse through workflow to get level rules
        print('form_company_ref_id : ',form_company_ref_id)
        print('form_service_asset_ref_id : ',form_service_asset_ref_id)
        header_data = tbl_workflow_mst.objects.filter(company_ref_id=form_company_ref_id,service_asset_ref_id=form_service_asset_ref_id).filter(is_deleted='N')
        print('Header data : ',header_data)
        for header_id_data in header_data:
                header_id = header_id_data.id
                level_rules_data = tbl_workflow_details.objects.filter(header_ref_id=header_id, left_panel_ref_id=left_panel_id).filter(is_deleted='N')
                if level_rules_data:
                    level_rules = level_rules_data

        
        if level_rules:
            ### Populate workflow_details_ids and approval_dict = {level: amount}
            for level_rule in level_rules:
                workflow_ref_id = level_rule.header_ref_id.id
                approval_fieldname = level_rule.field_name
                approval_dict[level_rule.id] = level_rule.approval_field_value
                workflow_details_ids.append(level_rule.id)

            activity_data = tbl_workflow_activity.objects.filter(workflow_ref_id=workflow_ref_id, form_ref_id=form_ref_id, status="Initiated")
            for data in activity_data:
                start_time = data.start_date_time
            end_date_time = datetime.now()
            end_time_utc = end_date_time.astimezone(pytz.utc)
            diff = end_time_utc - start_time
            days, seconds = diff.days, diff.seconds
            hours = format((days * 24 + seconds / 3600), ".2f")

            ### Change 'Initiated' to 'Closed'
            for activity_entry in tbl_workflow_activity.objects.filter(workflow_ref_id=workflow_ref_id, form_ref_id=form_ref_id, status="Initiated"):
                if activity_entry:
                    activity_entry.user_action_ref_id = user_action_ref_id
                    activity_entry.status = "Closed"
                    activity_entry.end_date_time = datetime.now().astimezone(pytz.utc)
                    activity_entry.actual_response_time = hours
                    activity_entry.actual_resolution_time = hours
                    if activity_entry.action_ref_id.id == user_action_ref_id:
                        next_triggered_sequence_number = activity_entry.next_sequence_number
                    activity_entry.save()
                else:
                    print('Workflow Activity Completed! - In Else')
                    is_workflow_activity_completed = True
            
            ### 'Initiate' the next sequence number
            if is_workflow_activity_completed == False:
                tbl_workflow_activity.objects.filter(sequence_number=next_triggered_sequence_number, workflow_ref_id=workflow_ref_id, form_ref_id=form_ref_id).update(status="Initiated")

            ### Get filteration keys for tbl_workflow_routing_activity table
            routing_details_object = tbl_workflow_routing_details.objects.filter(workflow_ref_id=workflow_ref_id).first()
            print('routing_details_object', routing_details_object)
            workflow_routing_mst_id = routing_details_object.header_ref_id
            workflow_routing_details_id = routing_details_object.id

            ### Update tbl_workflow_routing_activity
            for workflow_routing_activity_entry in tbl_workflow_routing_activity.objects.filter(workflow_routing_ref_id=workflow_routing_mst_id, workflow_routing_details_ref_id=workflow_routing_details_id, status="Initiated"):
                if workflow_routing_activity_entry: 
                    if is_workflow_activity_completed == True:
                        workflow_routing_activity_entry.status = "Closed"
                        next_triggered_routing_sequence_number = workflow_routing_activity_entry.next_sequence_number
                else:
                    is_workflow_routing_activity_completed = True

            ### 'Initiate' next workflow_routing_activity 
            if is_workflow_routing_activity_completed == False:
                tbl_workflow_routing_activity.objects.filter(sequence_number=next_triggered_routing_sequence_number, workflow_routing_ref_id=workflow_routing_mst_id, workflow_routing_details_ref_id=workflow_routing_details_id, status="Initiated").update(status="Initiated")



def update_activity_for_NOT_INITIATED(left_panel_id, form_ref_id, user_action_ref_id, form_company_ref_id, form_service_asset_ref_id):
    print('Inside function update_activity_for_NOT_INITIATED')

    max_level_approval_required = 0
    next_triggered_sequence_number = None
    next_triggered_routing_sequence_number = None
    obtained_left_panel = tbl_left_panel.objects.filter(id=left_panel_id)
    is_workflow_activity_completed = False
    is_workflow_routing_activity_completed = False

    if obtained_left_panel:
        ### Fetch model name for left panel object 

        left_panel_model_name = obtained_left_panel.first().backend_model_name
        obtained_backend_model_name = left_panel_model_name  ############## Variable inconsistency for field name
        obtained_model = apps.get_model('portal', obtained_backend_model_name)
        left_panel_object = obtained_model.objects.filter(id=form_ref_id).first() ### Used to get actual value of field with constraints

        ### Traverse through workflow to get level rules
        print('form_company_ref_id : ',form_company_ref_id)
        print('form_service_asset_ref_id : ',form_service_asset_ref_id)
        header_data = tbl_workflow_mst.objects.filter(company_ref_id=form_company_ref_id,service_asset_ref_id=form_service_asset_ref_id).filter(is_deleted='N')
        print('Header data : ',header_data)
        for header_id_data in header_data:
                header_id = header_id_data.id
                level_rules_data = tbl_workflow_details.objects.filter(header_ref_id=header_id, left_panel_ref_id=left_panel_id).filter(is_deleted='N')
                if level_rules_data:
                    level_rules = level_rules_data

        if level_rules:
            ### Populate workflow_details_ids and approval_dict = {level: amount}
            for level_rule in level_rules:
                workflow_ref_id = level_rule.header_ref_id.id
                approval_fieldname = level_rule.field_name
                approval_dict[level_rule.id] = level_rule.approval_field_value
                workflow_details_ids.append(level_rule.id)

            ### Change 'Not Initiated' to 'Closed'
            for activity_entry in tbl_workflow_activity.objects.filter(workflow_ref_id=workflow_ref_id, form_ref_id=form_ref_id, status="Not Initiated"):
                if activity_entry:
                    activity_entry.user_action_ref_id = user_action_ref_id
                    activity_entry.status = "Closed"
                    activity_entry.end_date_time = datetime.now().astimezone(pytz.utc)
                    if activity_entry.action_ref_id.id == user_action_ref_id:
                        next_triggered_sequence_number = activity_entry.next_sequence_number
                    activity_entry.save()
                else:
                    print('Workflow Activity Completed! - In Else')
                    is_workflow_activity_completed = True
            
"""             ### 'Initiate' the next sequence number
            if is_workflow_activity_completed == False:
                tbl_workflow_activity.objects.filter(sequence_number=next_triggered_sequence_number, workflow_ref_id=workflow_ref_id, form_ref_id=form_ref_id).update(status="Initiated")

            ### Get filteration keys for tbl_workflow_routing_activity table
            routing_details_object = tbl_workflow_routing_details.objects.filter(workflow_ref_id=workflow_ref_id).first()
            workflow_routing_mst_id = routing_details_object.header_ref_id
            workflow_routing_details_id = routing_details_object.id

            ### Update tbl_workflow_routing_activity
            for workflow_routing_activity_entry in tbl_workflow_routing_activity.objects.filter(workflow_routing_ref_id=workflow_routing_mst_id, workflow_routing_details_ref_id=workflow_routing_details_id, status="Initiated"):
                if workflow_routing_activity_entry: 
                    if is_workflow_activity_completed == True:
                        workflow_routing_activity_entry.status = "Closed"
                        next_triggered_routing_sequence_number = workflow_routing_activity_entry.next_sequence_number
                else:
                    is_workflow_routing_activity_completed = True

            ### 'Initiate' next workflow_routing_activity 
            if is_workflow_routing_activity_completed == False:
                tbl_workflow_routing_activity.objects.filter(sequence_number=next_triggered_routing_sequence_number, workflow_routing_ref_id=workflow_routing_mst_id, workflow_routing_details_ref_id=workflow_routing_details_id, status="Initiated").update(status="Initiated") """

