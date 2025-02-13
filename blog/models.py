from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django import forms
from datetime import datetime
from django.core.exceptions import ValidationError
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .choices import *

import os, random



class OwnCompany(models.Model):
    name = models.CharField('Название Юр.  Лица', max_length=200)
    ebin = models.CharField('БИН РК', max_length=14, blank=True)
    adress = models.CharField('Адрес', max_length=200, blank=True)


    def __str__(self):
        return self.name + str(self.id)


class Entity(models.Model):
    name = models.CharField('Название Юр. Лица', max_length=200)
    side_one = models.CharField('Резидент РК', max_length=1, choices=resident_choice, default='1')
    ebin = models.CharField('БИН РК', max_length=12, blank=True)
    etype = models.CharField('Тип организаций', max_length=1, choices=entity_type)
    adress = models.CharField('Адрес', max_length=200, blank=True)
    ebin2 = models.CharField('Иностранный Номер', max_length=200, blank=True)


    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name +', ' + self.get_etype_display()



def file_path(instance, filename):
    basefilename, file_extension= os.path.splitext(filename)
    chars= 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    randomstr= ''.join((random.choice(chars)) for x in range(10))
    _datetime = datetime.now()
    datetime_str = _datetime.strftime("%Y-%m-%d")
    basefilename = datetime_str+randomstr
    return 'dogovora/{basename}{ext}'.format(basename= basefilename, ext= file_extension)



class Sub(models.Model):
    created_at = models.DateField(auto_now_add=True, null=True,)
    number = models.IntegerField('Номер Допника')
    date_start = models.DateField('Дата Допника', null=True)
    date_end = models.DateField('Окончание Допника', null=True)
    upload_file1 = models.FileField(null=True, blank=True, upload_to=file_path)
    upload_file2 = models.FileField(null=True, blank=True, upload_to=file_path)
    upload_file3 = models.FileField(null=True, blank=True, upload_to=file_path)

    def __str__(self):
        return str(self.number)


class Worker(models.Model):
    name = models.CharField('Имя', max_length=200, default='')
    surname = models.CharField('Фамилия', max_length=200, default='')
    email = models.CharField('E-mail', max_length=200, default='')
    phone = models.CharField('Номер Телефона', max_length=200, default='')

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name + ' ' + self.surname


class Dogovor(models.Model):
    created_at = models.DateField(auto_now_add=True, null=True,)
    init = models.ForeignKey(Worker, on_delete=models.CASCADE, verbose_name='Инициатор', default='')
    own_company = models.ForeignKey(OwnCompany, on_delete=models.CASCADE, null=True, verbose_name='Сторона 1')
    signer_one = models.CharField('Подписант 1', max_length=1, choices=signer_choice, default='1')
    side_two = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, verbose_name='Сторона 2', related_name='Side 2+')
    signer_two = models.CharField('Подписант 2', max_length=1, choices=signer_choice, default='1')
    side_three = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Сторона 3', related_name='Side 3+')
    signer_three = models.CharField('Подписант 3', max_length=1, choices=signer_choice, blank=True, default='1')
    number = models.CharField('Номер Договора', max_length=100, blank=True, default='')
    originity = models.CharField('Имеется Оригинал', max_length=1, choices=resident_choice, default='1')
    renew = models.CharField('Авто Продление', max_length=1, choices=resident_choice, default='1')
    date_start = models.DateField('Дата Договора', null=True)
    date_end = models.DateField('Окончание Договора', null=True)
    upload_file = models.FileField(null=True, blank=True, upload_to=file_path)
    subs = models.ForeignKey(Sub, on_delete=models.CASCADE, null=True, blank= True, verbose_name='Допника')
    status = models.CharField('Статус', max_length=20, default='current', editable=False)
    upload_file2 = models.FileField(null=True, blank=True, upload_to=file_path)
    upload_file3 = models.FileField(null=True, blank=True, upload_to=file_path)
    upload_file4 = models.FileField(null=True, blank=True, upload_to=file_path)
    upload_file5 = models.FileField(null=True, blank=True, upload_to=file_path)



    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.number) + 'here'



class Upload(models.Model):
    upload_file = models.FileField()
    upload_date = models.DateTimeField(auto_now_add =True)



class InMail(models.Model):
    status = models.CharField('Статус', max_length=20, default='incoming', editable=False)
    init = models.ForeignKey(Worker, on_delete=models.CASCADE, verbose_name='Инициатор', default='')
    created_at = models.DateField(auto_now_add=True, null=True,)
    own_company = models.ForeignKey(OwnCompany, on_delete=models.CASCADE, null=True, verbose_name='Наши компаний')
    side_two = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, verbose_name='От кого')
    in_number = models.IntegerField('Входящий Номер')
    upload_file = models.FileField(null=True, upload_to=file_path, blank=True)
    response_to = models.ForeignKey('OutMail', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Ответ на письмо')
    topic = models.TextField('Тема', max_length=20000, null=True, blank=True)
    state = models.CharField('Состояние', max_length=20, default='editable')
    track_number = models.FileField(null=True, upload_to=file_path, blank=True)

    class Meta:
        unique_together = ('in_number', 'own_company',)

    def __str__(self):
        return str(self.own_company) + " " + str(self.side_two) 

class OutMail(models.Model):
    status = models.CharField('Статус', max_length=20, default='outcoming', editable=False)
    init = models.ForeignKey(Worker, on_delete=models.CASCADE, verbose_name='Инициатор', default='')
    created_at = models.DateField(auto_now_add=True, null=True,)
    own_company = models.ForeignKey(OwnCompany, on_delete=models.CASCADE, null=True, verbose_name='Наши компаний')
    side_two = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, verbose_name='Кому')
    out_number = models.IntegerField('Исходящий Номер')
    upload_file = models.FileField(null=True, upload_to=file_path, blank=True)
    response_to = models.ForeignKey('InMail', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Ответ на письмо')
    topic = models.TextField('Тема', max_length=20000, null=True, blank=True)
    state = models.CharField('Состояние', max_length=20, default='editable')
    track = models.CharField('Номер Трэка', max_length=20, default='', null=True, blank=True)    
    track_number = models.FileField(null=True, upload_to=file_path, blank=True)

    class Meta:
        unique_together = ('out_number', 'own_company',)
    def __str__(self):
        return str(self.side_two) + " " + str(self.own_company)


class UploadView(CreateView):
    model = Upload
    fields = ['upload_file', ]
    success_url = reverse_lazy('fileupload')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Upload.objects.all()
        return context