from django.shortcuts import render

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import *


def dogovor_new(request):
    return render(request, 'blog/dogovor_new.html', {})

def company_list(request):
    dogovors = Dogovor.objects.order_by('id')
    companys = OwnCompany.objects.order_by('id')
    context = {
        'dogovors': dogovors,
        'companys': companys,
    }
    return render(request, 'blog/company_list.html', context)

def dogovor_list(request, pk, pk_alt):
    dogovors = Dogovor.objects.filter(own_company_id = pk).filter(side_two_id = pk_alt)
    company = OwnCompany.objects.get(id=pk)
    side_two = Entity.objects.get(id = pk_alt)
    context = {
        'dogovors': dogovors,
        'company': company,
        'side_two': side_two,
    }
    return render(request, 'blog/dogovor_list.html', context)

    

def entity_list(request, pk):
    dogovors = Dogovor.objects.filter(own_company_id = pk)
    company = OwnCompany.objects.get(id=pk)
    entitys = Entity.objects.order_by('name')

    context = {
        'dogovors': dogovors,
        'company': company,
        'entitys': entitys,
    }
    return render(request, 'blog/entity_list.html', context)


def zapros_delete(request, pk, token):
    currents = Zapros.objects.filter(id=pk)
    currents.update(status='finished')
    # send_mail(
    # subject = 'That’s your subject',
    # message = 'That’s your message body',
    # from_email = 'mailer@btu.kz',
    # recipient_list = ['mailer@btu.kz',],
    # auth_user = 'mailer@btu.kz',
    # auth_password = 'Pass1234',
    # fail_silently = False,
    # )

    context = {
        'currents': currents
    }
    return render(request, 'blog/zapros_detail.html', context)
