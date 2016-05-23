# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
from django.contrib import admin
from django.utils import timezone
import datetime

DELETE_CHOICES = (
    (0, '可用'),
    (1, '无效')
)

PRODUCT_CHOICES = (
    (1, 'CAL'),
    (2, "DB")
)

SALE_CHOICES = (
    (0, '可售'),
    (1, '已售')
)

class bm(models.Model):
    id = models.BigIntegerField(primary_key=True)

    PRODUCT_CHOICES = (
        (1, 'CAL'),
        (2, 'DB')
    )

    product_type = models.IntegerField(null=True, blank=True, choices=PRODUCT_CHOICES)
    type = models.CharField(max_length=16)
    region = models.CharField(max_length=32)
    image_id = models.CharField(max_length=50)
    sn = models.CharField(max_length=32, unique=True)
    ipmi_ip = models.CharField(max_length=32)
    ipmi_user = models.CharField(max_length=32)
    ipmi_password = models.CharField(max_length=32)
    tor_manger_ip = models.CharField(max_length=64)
    tor_index = models.IntegerField(null=True, blank=True)
    mac = models.CharField(max_length=64)
    is_del = models.IntegerField(null=True, blank=True, choices=DELETE_CHOICES)
    is_sale = models.IntegerField(null=True, blank=True, choices=SALE_CHOICES)
    create_time = models.DateTimeField
    update_time = models.DateTimeField



    def __str__(self):
        return self.ipmi_ip

    class Meta:
        db_table = 'bm'
        # verbose_name = '哈哈'
        verbose_name_plural = '物理机信息'


class bmtype(models.Model):
    id = models.BigIntegerField(primary_key=True)
    product_type = models.IntegerField(null=True, blank=True, verbose_name='产品类型', choices=PRODUCT_CHOICES)
    type = models.CharField(max_length=16, verbose_name='套餐类型')
    cpu = models.CharField(max_length=32)
    memory = models.CharField(max_length=16)
    system_disk_type = models.CharField(max_length=16)
    system_disk_size = models.CharField(max_length=16)
    data_disk_type = models.CharField(max_length=16)
    data_disk_size = models.CharField(max_length=32)
    cpu_freq = models.CharField(max_length=10)
    cpu_count = models.IntegerField(null=True, blank=True)
    cpu_corecount = models.IntegerField(null=True, blank=True)
    system_disk_raid = models.CharField(max_length=45)
    system_disk_iocap = models.CharField(max_length=45)
    data_disk_raid = models.CharField(max_length=45)
    data_disk_iocap = models.CharField(max_length=45)
    data_disk_count = models.IntegerField(null=True, blank=True)

    is_del = models.IntegerField(null=True, blank=True, choices=DELETE_CHOICES)


    class Meta:
        db_table = 'bm_type'
        verbose_name_plural = '物理机产品类型'




class bmimage(models.Model):
    id = models.BigIntegerField(primary_key=True)
    uuid = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    show_name = models.CharField(max_length=50)
    os_name = models.CharField(max_length=45)
    os_type = models.CharField(max_length=45)
    is_del = models.IntegerField(null=True, blank=True, choices=DELETE_CHOICES)
    create_time = models.DateTimeField(auto_now=False)
    update_time = models.DateTimeField(auto_now=False)


    class Meta:
        db_table = 'bm_image'
        verbose_name_plural = '操作系统镜像'

RUNNING_CHOICE = (
    (2,'Initializing'),
    (3,'Stopped'),
    (5,'Reinstalling'),
    (12,'InstallFailed'),
    (14,'ReinstallFailed'),
    (20,"Running"),
    (30,"Locked"),
    (50,"Deleted")

)

class bminfo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    uuid = models.CharField(max_length=50)
    bm_sn = models.CharField(max_length=50)
    user_id = models.IntegerField(null=True, blank=True)
    bm_name = models.CharField(max_length=128)
    bm_type = models.CharField(max_length=128)

    image_id = models.CharField(max_length=50)
    raid = models.CharField(max_length=45)
    create_time = models.DateTimeField(auto_now=False)
    update_time = models.DateTimeField(auto_now=False)
    status = models.IntegerField(null=True,blank=True, choices=RUNNING_CHOICE)


    class Meta:
        db_table = 'bm_info'
        verbose_name_plural = '用户主机信息'


class bmvpc(models.Model):
    id = models.BigIntegerField(primary_key=True)
    bm_uuid = models.CharField(max_length=64)
    vnet_uuid = models.CharField(max_length=64)
    ip = models.CharField(max_length=64)

    class Meta:
        db_table = 'bm_vpc'