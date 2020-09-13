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
    path('expired_list/', views.expired_list, name='expired_list'),
    path('mail_detail/<str:status>/<int:pk>', views.mail_detail, name='mail_detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
