from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.db.models import Q 
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


def dogovor_detail(request, pk, pk_alt, pk_altos):
    dogovor = Dogovor.objects.get(id=pk_altos)
    company = OwnCompany.objects.get(id=pk)
    side_two = Entity.objects.get(id = pk_alt)
    context = {
        'dogovor': dogovor,
        'company': company,
        'side_two': side_two,
    }
    return render(request, 'blog/dogovor_detail.html', context)

    
def dogovor_delete(request, pk, pk_alt, pk_altos):
    dogovor = Dogovor.objects.filter(id=pk)
    dogovor.update(status='trash')

    dogovors = Dogovor.objects.filter(own_company_id = pk_alt).filter(side_two_id = pk_altos)
    company = OwnCompany.objects.get(id=pk_alt)
    side_two = Entity.objects.get(id = pk_altos)
    context = {
        'dogovors': dogovors,
        'company': company,
        'side_two': side_two,
    }
    return render(request, 'blog/dogovor_list.html', context)


    

def entity_list(request, pk):
    dogovors = Dogovor.objects.filter(own_company_id = pk).filter(status='current')
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



def delete_list(request):
    dogovors = Dogovor.objects.filter(status='trash')
    context = {
        'dogovors': dogovors
    }
    return render(request, 'blog/delete_list.html', context)


def search_list(request):
    own = request.GET.get('own')
    other = request.GET.get('other')
    original = request.GET.get('original')
    date_start = request.GET.get('date_start')
    date_end = request.GET.get('date_end')

    
    own_ids = []
    other_ids = []


    if(len(original)<1):
        original_ids = [1,2]
    else: 
        original_ids = original

    
    def check_list(target, order, model):
        counter = model.objects.all().count()

        if len(target) > 0:    
            for i in target:
                if i != ",":
                    order.append(int(i))
        else:
            for j in range(counter):
                order.append(j+1)
        
    check_list(own, own_ids, OwnCompany)
    check_list(other, other_ids, OwnCompany)

    entitys = Entity.objects.all()
    dogovors = Dogovor.objects.filter(own_company_id__in = own_ids).filter(side_two_id__in = other_ids).filter(originity__in = original_ids).filter(date_start__range=[date_start, date_end]).order_by('own_company')
    # dogovors = Dogovor.objects
    
    companys = OwnCompany.objects.all()
    context = {
        'dogovors': dogovors,
        'entitys': entitys,
        'companys': companys,
    }


    return render(request, 'blog/search_list.html', context)
