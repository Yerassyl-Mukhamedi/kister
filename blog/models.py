from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django import forms
from datetime import datetime
from django.core.exceptions import ValidationError
from .choices import *
import os, random



class OwnCompany(models.Model):
    name = models.CharField('Название Юр. Лица', max_length=200)
    ebin = models.CharField('БИН РК', max_length=12, blank=True)


    def __str__(self):
        return self.name 


class Entity(models.Model):
    name = models.CharField('Название Юр. Лица', max_length=200)
    side_one = models.CharField('Резидент РК', max_length=1, choices=resident_choice, default='1')
    ebin = models.CharField('БИН РК', max_length=12, blank=True)
    etype = models.CharField('Тип организаций', max_length=1, choices=entity_type)
    ebin2 = models.CharField('Иностранный Номер', max_length=200, blank=True)


    def __str__(self):
        return '"' + self.name +'", ' + self.get_etype_display()


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

class Dogovor(models.Model):
    created_at = models.DateField(auto_now_add=True, null=True,)
    own_company = models.ForeignKey(OwnCompany, on_delete=models.CASCADE, null=True, verbose_name='Сторона 1')
    signer_one = models.CharField('Подписант 1', max_length=1, choices=signer_choice, default='1')
    side_two = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, verbose_name='Сторона 2')
    signer_two = models.CharField('Подписант 2', max_length=1, choices=signer_choice, default='1') 
    number = models.IntegerField('Номер Договора')
    originity = models.CharField('Имеется Оригинал', max_length=1, choices=resident_choice, default='1')
    date_start = models.DateField('Дата Договора', null=True)
    date_end = models.DateField('Окончание Договора', null=True)
    upload_file = models.FileField(null=True, upload_to=file_path)
    subs = models.ForeignKey(Sub, on_delete=models.CASCADE, null=True, blank= True, verbose_name='Допника')
    status = models.CharField('Статус', max_length=20, default='current', editable=False) 



    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.number)



class Upload(models.Model):
    upload_file = models.FileField()    
    upload_date = models.DateTimeField(auto_now_add =True)