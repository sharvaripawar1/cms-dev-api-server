from django.urls import include, path
from ntpath import basename
from rest_framework import routers
from . import views
from drf_jwt_2fa.views import obtain_auth_token, obtain_code_token, refresh_auth_token
from django.urls.conf import re_path
from rest_framework.decorators import action, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

router = routers.DefaultRouter()
router.register(r'country', views.tbl_country_mst_view)
router.register(r'state', views.tbl_state_mst_view, basename='state')
router.register(r'city', views.tbl_city_mst_view, basename='city')
router.register(r'location', views.tbl_location_mst_view, basename='location')
router.register(r'company', views.tbl_company_mst_view, basename = 'company')
router.register(r'user', views.UserViewSet, basename='user')
router.register(r'login', views.tbl_login_mst_view, basename='login')
router.register(r'master', views.MasterViewSet, basename='master')
router.register(r'tickettype',views.tbl_ticket_type_mst_view,basename='tickettype')
router.register(r'currency', views.tbl_currency_mst_view)
router.register(r'reason', views.tbl_reason_mst_view)
router.register(r'employeemst',views.tbl_employee_mst_view)
router.register(r'user', views.UserViewSet, basename='user')
router.register(r'application', views.tbl_service_asset_mst_view)
router.register(r'channel', views.tbl_channel_mst_view)
router.register(r'company-application-link',views.tbl_company_application_link_mst_view)
router.register(r'sla', views.tbl_sla_mst_view,basename='sla')
router.register(r'sla_details', views.tbl_sla_details_mst_view,basename='sla_details')
router.register(r'company-application-link',views.tbl_company_application_link_mst_view)
router.register(r'company-application-link-details',views.tbl_company_application_link_details_view)
router.register(r'message', views.tbl_message_mst_view)
router.register(r'role', views.RoleViewset)
router.register(r'role_master', views.tbl_role_master_view)
router.register(r'role-application-link',views.tbl_role_application_mst_view)
router.register(r'workflowmst', views.tbl_workflow_mst_view)
router.register(r'activity', views.ActivityViewSet)
router.register(r'left-panel', views.LeftPanelViewSet)
router.register(r'level', views.LevelViewSet)
router.register(r'level-details', views.LevelDetailsViewSet)
router.register(r'action', views.ActionViewSet)
router.register(r'workflow', views.WorkflowViewSet)
router.register(r'workflow-routing', views.WorkflowRoutingViewSet)
router.register(r'workflow-routing-details', views.WorkflowRoutingDetailsViewSet)
router.register(r'employee', views.EmployeeViewSet)
router.register(r'currency', views.CurrencyViewSet)
router.register(r'file',views.file_view)
router.register(r'issue-master',views.tbl_issue_mst_view)
router.register(r'help-desk',views.help_desk_mst_view)
router.register(r'problem-help-desk',views.problem_help_desk_mst_view)
router.register(r'assignees-action',views.assignees_action_mst_view)
router.register(r'problem-assignees-action',views.problem_assignees_action_mst_view)
router.register(r'assign_to_screen',views.tbl_assign_screen_to_role_mst_view)
router.register(r'roles_to_enduser', views.AssignRolesToEnduserViewSet)
router.register(r'company-priority-link',views.tbl_company_priority_link_mst_view)
router.register(r'company-priority-link-details',views.tbl_company_priority_link_details_view)
router.register(r'problem-issue-master',views.tbl_problem_issue_mst_view)
router.register(r'asset-master',views.tbl_asset_mst_view)
router.register(r'deleteuser',views.tbl_user_mst_view)


urlpatterns = [
    path('auth/code/', obtain_code_token),
    path('auth/login/', obtain_auth_token),
    path('auth/refresh-token/', refresh_auth_token),
    re_path('currency/ofcountry/(?P<country_id>.+)/$', views.tbl_currency_mst_view.as_view({'get': 'list'})),  #Using only one viewset pass country_id
    re_path('master/oftype/(?P<master_type>.+)/$', views.MasterViewSet.as_view({'get' : 'list'})),  #Using only one viewset pass country_id
    re_path('getchannel/', views.tbl_channel_mst_view.as_view({'get' : 'list'})),  #Using only one viewset pass country_id
    re_path('getapplication/', views.tbl_service_asset_mst_view.as_view({'get' : 'list'})),
    re_path('getLocation/', views.tbl_location_mst_view.as_view({'get' : 'list'})),
    re_path('getemployee/', views.tbl_employee_mst_view.as_view({'get' : 'list'})),
    re_path('getcompany/', views.tbl_company_mst_view.as_view({'get' : 'list'})),
    re_path('getcompanybycompanyid/', views.getcompanybycompanyid_view.as_view()),
    path(r'add_company/', views.add_company_view.as_view(), name='add_company'),
    re_path('getcompany-priority-link/',views.tbl_company_priority_link_mst_view.as_view({'get':'list'})),
    re_path('currency/ofcountry/(?P<country_id>.+)/$', views.tbl_currency_mst_view.as_view({'get': 'list'})),
    re_path('sla/ofcompany/(?P<company_id>.+)/$', views.tbl_sla_mst_view.as_view({'get': 'list'})), 
    re_path('sla/ofapplication/(?P<application_id>.+)/$', views.tbl_sla_mst_view.as_view({'get': 'list'})), 
    re_path('sla/ofcompany/(?P<ticket_id>.+)/$', views.tbl_sla_mst_view.as_view({'get': 'list'})), #Using only one viewset pass country_id
    re_path('assign-to-screen/ofcompany/(?P<company_id>.+)/$',views.tbl_assign_screen_to_role_mst_view.as_view({'get':'list'})),
    re_path('assign-to-screen/ofcompany/(?P<left_panel_id>.+)/$',views.tbl_assign_screen_to_role_mst_view.as_view({'get':'list'})),
    re_path('assign-to-screen/bycomapnyid/(?P<company_id>.+)/$',views.tbl_assign_screen_to_role_mst_view.as_view({'get':'list'})),
    re_path('master/oftype/(?P<master_type>.+)/$', views.MasterViewSet.as_view({'get' : 'list'})), #Using only one viewset pass country_id
    re_path('channel/', views.tbl_channel_mst_view.as_view({'get' : 'list'})),  #Using only one viewset pass country_id
    re_path('gettickettype/', views.tbl_ticket_type_mst_view.as_view({'get' : 'list'})),
    re_path('getsla/',views.tbl_sla_mst_view.as_view({'get':'list'})),
    re_path('getmessage/',views.tbl_message_mst_view.as_view({'get':'list'})),
    re_path('getuser/',views.tbl_user_mst_view.as_view({'get':'list'})),
    re_path('employee_acc_company/', views.get_employee_acc_company.as_view()),
    re_path('user_acc_company/', views.get_user_acc_company.as_view()),
    re_path('priority_acc_service/',views.get_priority_status_acc_service.as_view()),
    re_path('application_acc_company/',views.get_application__acc_company.as_view()),
    re_path('get_screen_to_role/',views.get_screen_to_role.as_view()),
    re_path('get_role_to_use/',views.getrole_acc_to_use.as_view()),
    re_path('get_data_acc_role/',views.get_data_acc_role.as_view()),
    re_path('get_data/',views.get_screen_data.as_view()),
    re_path('issue-master-user/', views.tbl_issue_mst_user_view.as_view()),
    re_path('issue-master-support/', views.tbl_issue_mst_support_view.as_view()),
    re_path('problem-issue-support-master/', views.tbl_support_problem_issue_mst_view.as_view()),
    re_path('max-issue-id', views.max_issue_id_view.as_view()),
    re_path('max-problem-issue-id', views.max_problem_issue_id_view.as_view()),
    re_path('total-resolution-time-by-formid', views.getTotalResolutionByForm_view.as_view()),
    re_path('sla-vio-response-data', views.getSLAVioResponseTime_view.as_view()),
    re_path('sla-vio-resolution-data', views.getSLAVioResolutionTime_view.as_view()),
    re_path('get-employee-resolution-data', views.getAllEmployeesByUserIdView.as_view()),
    re_path('escalation-issue-data', views.getEscalationIssue_view.as_view()),
    re_path('escalation-problemissue-data', views.getEscalationProblemIssue_view.as_view()),
    path('sidebar/', views.sidebar_leftpanel.as_view()),
    path('leftpanel/', views.tbl_leftpanel.as_view()),

    path(r'employeeregistration/', views.employee_registration_view.as_view(), name='employeeregistration'),
    path(r'employeeregistration/<int:pk>/', views.employee_registration_view.as_view(), name='employeeregistration'),
    path(r'userregistration/', views.user_registration_view.as_view(), name='userregistration'),
    path(r'userregistration/<int:pk>/', views.user_registration_view.as_view(), name='userregistration'),
    path(r'roleMstEmp/', views.get_role_ref_id_view.as_view(), name='roleMstEmp'),
    path(r'getcompanyname/', views.company_name_view.as_view(), name='company_name_view'),
    path(r'general_mst_label/<app_label>/<model_name>', views.GeneralViewSet.as_view({'get': 'list'})),
    path(r'uploadFile/', views.file_upload_view.as_view(), name='uploadFile'),
    path(r'getTicketStatus/', views.tbl_ticket_status_view.as_view({'get': 'list'}), name='getTicketStatus'),      
    path(r'getTotalTicketCount/', views.getTotalTicketCount_view.as_view(), name="getTotalTicketCount_view"),
    path(r'getAvgTime/', views.getAvgTime_view.as_view(), name="getAvgTime_view"),
    path(r'getPieChartData/', views.getPieChartData_view.as_view(), name="getPieChartData_view"),
    path(r'getPieChartDataforProblem/', views.getPieChartDataforProblem_view.as_view(), name="getPieChartDataforProblem_view"),
    path(r'getProblemCount/', views.getProblemCount_view.as_view(), name="getProblemCount_view"),
    path(r'getIncidentCount/', views.getIncidentCount_view.as_view(), name="getIncidentCount_view"),
    path(r'get-company-priority-data', views.getSLAPriorityData_view.as_view(), name="getSLAPriorityData_view"),
    path('', include(router.urls)),
]
