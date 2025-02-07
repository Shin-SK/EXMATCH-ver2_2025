# master/dummy_app/live.py
from django.urls import re_path
from . import views

app_name = 'live'

urlpatterns = [
    # ルート
    re_path(r'^$', views.dummy_view, name='index'),

    # ex_member_update：m_id を任意（空文字も許容）
    re_path(
        r'^ex_member_update(?:/(?P<m_id>[0-9]*))?/?$',
        views.dummy_view,
        name='ex_member_update'
    ),

    # ex_member_create：l_rid を任意
    re_path(
        r'^ex_member_create(?:/(?P<l_rid>[0-9]*))?/?$',
        views.dummy_view,
        name='ex_member_create'
    ),

    # ex_management_update：pk を任意
    re_path(
        r'^ex_management_update(?:/(?P<pk>[0-9]*))?/?$',
        views.dummy_view,
        name='ex_management_update'
    ),

    # ex_management_detail：pk を任意
    re_path(
        r'^ex_management_detail(?:/(?P<pk>[0-9]*))?/?$',
        views.dummy_view,
        name='ex_management_detail'
    ),

    # ex_member_detail：pk を任意
    re_path(
        r'^ex_member_detail(?:/(?P<pk>[0-9]*))?/?$',
        views.dummy_view,
        name='ex_member_detail'
    ),

    # ex_profile_detail：pk を任意（空文字も許容）
    re_path(
        r'^ex_profile_detail(?:/(?P<pk>[0-9]*))?/?$',
        views.dummy_view,
        name='ex_profile_detail'
    ),

    # member-profile-check：必須の pk
    re_path(
        r'^member_profile_check/(?P<pk>[0-9]+)/?$',
        views.dummy_view,
        name='member-profile-check'
    ),

    # ex_change_paid_membership：m_id を任意
    re_path(
        r'^ex_change_paid_membership(?:/(?P<m_id>[0-9]*))?/?$',
        views.dummy_view,
        name='ex_change_paid_membership'
    ),

    # ex_change_optional_membership：m_id を任意
    re_path(
        r'^ex_change_optional_membership(?:/(?P<m_id>[0-9]*))?/?$',
        views.dummy_view,
        name='ex_change_optional_membership'
    ),

    # ex_change_free_membership：m_id を任意
    re_path(
        r'^ex_change_free_membership(?:/(?P<m_id>[0-9]*))?/?$',
        views.dummy_view,
        name='ex_change_free_membership'
    ),

    # ex_profile_create：パラメータ不要
    re_path(
        r'^ex_profile_create/?$',
        views.dummy_view,
        name='ex_profile_create'
    ),

    # ex_profile_update：引数（msg_id）があっても空文字の場合も許容
    re_path(
        r'^ex_profile_update(?:/(?P<msg_id>[0-9]*))?/?$',
        views.dummy_view,
        name='ex_profile_update'
    ),

    # price_list
    re_path(
        r'^price_list/?$',
        views.dummy_view,
        name='price_list'
    ),

    # profile_detail_message：オプショナルな数値引数（空文字も許容）
    re_path(
        r'^profile_detail_message(?:/(?P<msg_id>[0-9]*))?/?$',
        views.dummy_view,
        name='profile_detail_message'
    ),

    # ex_profile_search：nick_name 引数（英数字、ハイフン）を任意に
    re_path(
        r'^ex_profile_search(?:/(?P<nick_name>[\w-]+))?/?$',
        views.dummy_view,
        name='ex_profile_search'
    ),

    # profile_search：nick_name 引数を任意に
    re_path(
        r'^profile_search(?:/(?P<nick_name>[\w-]+))?/?$',
        views.dummy_view,
        name='profile_search'
    ),

    # my_page
    re_path(
        r'^my_page/?$',
        views.dummy_view,
        name='my_page'
    ),

    # ex_dailyrate
    re_path(
        r'^ex_dailyrate/?$',
        views.dummy_view,
        name='ex_dailyrate'
    ),

    # event: イベント用
    re_path(
        r'^event/?$',
        views.dummy_view,
        name='event'
    ),

    # currentlocation_delete
    re_path(
        r'^currentlocation_delete/?$',
        views.dummy_view,
        name='currentlocation_delete'
    ),

    # service
    re_path(
        r'^service/?$',
        views.dummy_view,
        name='service'
    ),

    # services_provided
    re_path(
        r'^services_provided/?$',
        views.dummy_view,
        name='services_provided'
    ),

    # faq
    re_path(
        r'^faq/?$',
        views.dummy_view,
        name='faq'
    ),

    # business_flow
    re_path(
        r'^business_flow/?$',
        views.dummy_view,
        name='business_flow'
    ),

    # service_area
    re_path(
        r'^service_area/?$',
        views.dummy_view,
        name='service_area'
    ),

    # terms_service
    re_path(
        r'^terms_service/?$',
        views.dummy_view,
        name='terms_service'
    ),

    # operation
    re_path(
        r'^operation/?$',
        views.dummy_view,
        name='operation'
    ),

    # bank_accounts
    re_path(
        r'^bank_accounts/?$',
        views.dummy_view,
        name='bank_accounts'
    ),

    # ex_inquiry
    re_path(
        r'^ex_inquiry/?$',
        views.dummy_view,
        name='ex_inquiry'
    ),
]
