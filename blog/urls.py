from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.mail_list, name='mail_list'),
    path('company_list', views.company_list, name='company_list'),
    path('dogovor_new', views.dogovor_new, name='dogovor_new'),
    path('entity_list/<int:pk>/', views.entity_list, name='entity_list'),
    path('dogovor_list/<int:pk>/<int:pk_alt>', views.dogovor_list, name='dogovor_list'),
    path('dogovor_detail/<int:pk>/<int:pk_alt>/<int:pk_altos>', views.dogovor_detail, name='dogovor_detail'),
    path('dogovor_delete/<int:pk>/<int:pk_alt>/<int:pk_altos>/', views.dogovor_delete, name='dogovor_delete'),
    path('delete_list/', views.delete_list, name='delete_list'),
    path('search_list/', views.search_list, name='search_list'),
    path('mail_search/', views.mail_search, name='mail_search'),
    path('expired_list/', views.expired_list, name='expired_list'),
    path('mail_detail/<str:status>/<int:pk>', views.mail_detail, name='mail_detail'),
    path('mail_edit/<str:status>/<int:pk>', views.mail_edit, name='mail_edit'),
    path('mail_send/<str:status>/<int:pk>', views.mail_send, name='mail_send'),
    path('mail_new/<str:status>', views.mail_new, name='mail_new'),
    path('sub_detail/<int:pk>', views.sub_detail, name='sub_detail'),
    path('some_view/<int:pk>/<str:status>', views.some_view, name='some_view'),
    path('entity_edit/<int:pk>', views.entity_edit, name='entity_edit'),
    path('user_login', views.user_login, name='user_login'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
