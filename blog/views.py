from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import redirect

# from django.http import HttpResponse
# from django.views.generic import View

# from .utils import * #created in step 4

# from django import template
# from django.template.loader import get_template

from datetime import datetime

from .models import *
from .forms import *

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
    dogovors_two = Dogovor.objects.filter(own_company_id = pk).filter(side_two_id = pk_alt)
    dogovors_three = Dogovor.objects.filter(own_company_id = pk).filter(side_three_id = pk_alt)
    company = OwnCompany.objects.get(id=pk)
    side_two = Entity.objects.get(id = pk_alt)
    side_three = Entity.objects.get(id = pk_alt)
    context = {
        'dogovors_two': dogovors_two,
        'dogovors_three': dogovors_three,
        'company': company,
        'side_two': side_two,
        'side_three': side_three,
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


def delete_list(request):
    dogovors = Dogovor.objects.filter(status='trash')
    context = {
        'dogovors': dogovors
    }
    return render(request, 'blog/delete_list.html', context)


def check_list(klit, target, order, model):
    counter = model.objects.all().count()
    dlina = len(target)

    def recursion(number):
        if(',' in target):
            comma = target.count(',')
            for i in range(comma+1):
                san = target.split(',')[i]
                order.append(int(san))
                klit.append(comma)
        else:
            order.append(int(target))

    if dlina > 0:
        recursion(1)
    else:
        for j in range(counter+10):
            order.append(j+1)

def search_list(request):
    own = request.GET.get('own')
    other = request.GET.get('other')
    init = request.GET.get('init')
    original = request.GET.get('original')
    auto = request.GET.get('auto')
    date_start = request.GET.get('date_start')
    date_end = request.GET.get('date_end')
    own_ids = []
    other_ids = []
    init_ids = []
    klits = []

    if(len(original)<1):
        original_ids = [1,2]
    else:
        original_ids = original

    if(len(auto)<1):
        auto_ids = [1,2]
    else:
        auto_ids = auto

    check_list(klits, own, own_ids, OwnCompany)
    check_list(klits, other, other_ids, Entity)
    check_list(klits, init, init_ids, Worker)

    entitys = Entity.objects.all()
    inits = Worker.objects.all()
    companys = OwnCompany.objects.all()
    # dogovors = Dogovor.objects.filter(own_company_id__in = own_ids).filter(init_id__in = init_ids).filter(side_two_id__in = other_ids).filter(originity__in = original_ids).filter(renew__in = auto_ids).filter(date_start__range=[date_start, date_end]).order_by('id')
    dogovors_two = Dogovor.objects.filter(own_company_id__in = own_ids).filter(init_id__in = init_ids).filter(side_three_id__in = other_ids).filter(originity__in = original_ids).filter(renew__in = auto_ids).filter(date_start__range=[date_start, date_end]).order_by('id')
    # dogovors = Dogovor.objects
    dogovors = Dogovor.objects.filter(side_two_id__in = other_ids)
    context = {
        'dogovors': dogovors,
        'entitys': entitys,
        'inits': inits,
        'companys': companys,
        'dogovors_two': dogovors_two,
        'companys': companys,
        'klits': klits,
    }


    return render(request, 'blog/search_list.html', context)



def mail_search(request):
    own = request.GET.get('own')
    other = request.GET.get('other')
    own_ids = []
    other_ids = []
    klits = []
    entitys = Entity.objects.all()
    inits = Worker.objects.all()
    companys = OwnCompany.objects.all()

    check_list(klits, own, own_ids, OwnCompany)
    check_list(klits, other, other_ids, Entity)

    if(request.GET.get('track_number') != None):
        track_number = request.GET.get('track_number')
    else:
        track_number = ''



    mails = OutMail.objects.filter(own_company_id__in = own_ids).filter(side_two_id__in = other_ids).filter(track__contains = track_number)

    context = {
        'mails': mails,
        'entitys': entitys,
        'inits': inits,
        'companys': companys,
    }
    return render(request, 'blog/mail_search.html', context)

def expired_list(request):
    dogovora = Dogovor.objects.all()
    now = datetime.now().date()
    spisok = []
    for dog in dogovora:
        if(now - dog.date_end >= now - now ):
            spisok.append(dog.id)

    dogovors = Dogovor.objects.filter(id__in = spisok)



    context = {
        'dogovors': dogovors
    }
    return render(request, 'blog/expired_list.html', context)


def mail_list(request):
    inmails = InMail.objects.all()
    outmails = OutMail.objects.all().order_by('id')
    context = {
        'inmails': inmails,
        'outmails': outmails,
    }
    return render(request, 'blog/mail_list.html', context)



def mail_detail(request, status, pk):
    if(status == 'incoming'):
        mail = InMail.objects.get(id=pk)
        try:
            responses = OutMail.objects.filter(response_to_id = pk)
        except:
            responses = None
    elif(status == 'outcoming'):
        mail = OutMail.objects.get(id=pk)
        try:
            responses = InMail.objects.filter(response_to_id = pk)
        except:
            responses = None


    context = {
        'mail': mail,
        'responses': responses,
    }
    return render(request, 'blog/mail_detail.html', context)


def mail_edit(request, status, pk):
    if(status == 'incoming'):
        mail = InMail.objects.get(id=pk)
        if request.method == "POST":
            form = InMailForm(request.POST, request.FILES, instance = mail)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('mail_list')
        else:
            form = InMailForm()
        try:
            responses = OutMail.objects.filter(response_to_id = pk)
        except:
            responses = None


    elif(status == 'outcoming'):
        mail = OutMail.objects.get(id=pk)
        if request.method == "POST":
            form = OutMailForm(request.POST, request.FILES, instance = mail)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('mail_list')
        else:
            form = OutMailForm()

        try:
            responses = InMail.objects.filter(response_to_id = pk)
        except:
            responses = None


    context = {
        'mail': mail,
        'responses': responses,
        'form': form,
    }

    return render(request, 'blog/mail_edit.html', context)


def mail_send(request, status, pk):

    if(status=='incoming'):

        InMail.objects.filter(id=pk).update(state='noneditable')
        mail = InMail.objects.get(id=pk)
        try:
            responses = InMail.objects.filter(response_to_id = pk)
        except:
            responses = None

    elif(status=='outcoming'):
        OutMail.objects.filter(id=pk).update(state='noneditable')
        mail = OutMail.objects.get(id=pk)
        try:
            responses = OutMail.objects.filter(response_to_id = pk)
        except:
            responses = None



    context = {
        'mail': mail,
        'responses': responses,
    }

    return render(request, 'blog/mail_detail.html', context)





def mail_new(request, status):
    context = {}
    if(status=='in'):
        own1 = InMail.objects.filter(own_company__name = 'Planeta doors').last()
        own2 = InMail.objects.filter(own_company__name = 'Двери.опт').last()
        own3 = InMail.objects.filter(own_company__name = 'Kendala IMPEX').last()
        own4 = InMail.objects.filter(own_company__name = 'Двери.класс').last()
        own5 = InMail.objects.filter(own_company__name = 'ИП Арынов').last()
        own6 = InMail.objects.filter(own_company__name = 'ИП Таишев').last()
        own7 = InMail.objects.filter(own_company__name = 'ТОО Beltaus').last()
        own8 = InMail.objects.filter(own_company__name = 'Kendala KG').last()
        own9 = InMail.objects.filter(own_company__name = 'Kendala Logistics').last()
        if request.method == "POST":
            form = InMailForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('mail_list')
        else:
            form = InMailForm()


    elif(status=='out'):
        own1 = OutMail.objects.filter(own_company__name = 'Planeta doors').last()
        own2 = OutMail.objects.filter(own_company__name = 'Двери.опт').last()
        own3 = OutMail.objects.filter(own_company__name = 'Kendala IMPEX').last()
        own4 = OutMail.objects.filter(own_company__name = 'Двери.класс').last()
        own5 = OutMail.objects.filter(own_company__name = 'ИП Арынов').last()
        own6 = OutMail.objects.filter(own_company__name = 'ИП Таишев').last()
        own7 = OutMail.objects.filter(own_company__name = 'ТОО Beltaus').last()
        own8 = OutMail.objects.filter(own_company__name = 'Kendala KG').last()
        own9 = OutMail.objects.filter(own_company__name = 'Kendala Logistics').last()
        if request.method == "POST":
            form = OutMailForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('mail_list')
        else:
            form = OutMailForm()

    context ={
        'form': form,
        'own1': own1,
        'own2': own2,
        'own3': own3,
        'own4': own4,
        'own5': own5,
        'own6': own6,
        'own7': own7,
        'own8': own8,
        'own9': own9,
    }


    return render(request, 'blog/mail_new.html', context)



def sub_detail(request, pk):
    sub = Sub.objects.get(id=pk)
    dogovors = Dogovor.objects.filter(subs_id = pk)
    context = {
        'sub': sub,
        'dogovors': dogovors,
    }
    return render(request, 'blog/sub_detail.html', context)







def some_view(request, pk, status):

    mail = OutMail.objects.get(id=pk)
    context = {
        "invoice_id": 123,
        "customer_name": "John Cooper",
        "amount": 1399.99,
        "today": "Today",
        'mail': mail,
        'time': datetime.now()
    }

    return render(request, 'blog/mail_pdf.html', context)
