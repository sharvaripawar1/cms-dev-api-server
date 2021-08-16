from datetime import datetime
from calendar import timegm
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .serializers import tbl_login_mst_serializer, RoleSerializer , tbl_company_mst_serializer,tbl_service_asset_mst_serializer

def jwt_payload_handler(user):
    """
    Custom payload handler 
    Token encrypts the dictionary returned by this function, and can be decoded by rest_framework_jwt.utils.jwt_decode_handler
    """
    login_data = tbl_login_mst_serializer.get(user)
    print(login_data,'iiiiiiiiiiiiiiiiiii')
    print(login_data.company_id.id,'company_id')
    role_data = RoleSerializer.get(tbl_login_mst_serializer.get(user).role_ref_id)
    company_data = tbl_company_mst_serializer.get(login_data.company_id)
    print(company_data,"In custom")
    return {
        'ID': user.pk,
        'username': user.username,
        'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA,
        'email': user.email,
        'orig_iat': timegm(
            datetime.utcnow().utctimetuple()
        ),
        'role': role_data.role_name,
        'role_ref_id': role_data.id,
        'APPLICATION_ID': login_data.application_id,
        'SUB_APPLICATION_ID': login_data.sub_application_id,
        'COMPANY_ID': login_data.company_id.id,
        'COMPANY_TYPE_REF_ID': company_data.company_type_ref_id.id,
        'COMPANY_SHARE_ID': company_data.share_id
        
    }   

    