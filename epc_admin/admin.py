# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import *

def make_invalid(modeladmin, request, queryset):
        queryset.update(is_del=1)
make_invalid.short_description = '删除所选项'

def make_valid(modeladmin, request, queryset):
    queryset.update(is_del=0)
make_valid.short_description = '恢复所选项'



class bmAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_type', 'type', 'sn', 'ipmi_ip', 'ipmi_user', 'ipmi_password', 'tor_manger_ip', 'mac', 'is_del', 'is_sale')
    search_fields = ['sn', 'ipmi_ip', 'mac']

    list_filter = ['is_del', 'is_sale']

    actions_on_top = False
    actions_on_bottom = True

    actions = [make_invalid, make_valid]



class bmtypeAdmin(admin.ModelAdmin):
    list_display = ('id', "product_type", 'type', 'cpu', 'cpu_freq', 'cpu_count', 'cpu_corecount', 'memory', 'system_disk_type', 'system_disk_size', 'data_disk_type',
                    'data_disk_size', 'system_disk_raid', 'system_disk_iocap', 'data_disk_raid', 'data_disk_iocap', 'data_disk_count')

    actions_on_top = False
    actions_on_bottom = True

    actions = [make_invalid, make_valid]




class bmimageAdmin(admin.ModelAdmin):
    list_display = ('id', 'uuid', 'name', 'show_name', 'os_name', 'os_type', 'create_time', 'update_time', 'is_del')

    actions_on_top = False
    actions_on_bottom = True

    search_fields = ['name', 'show_name', 'os_type']

    actions = [make_invalid, make_valid]

class bminfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'bm_sn', 'uuid', 'user_id', 'bm_type', 'image_name','vnet_id', 'raid', 'create_time', 'status')

    list_filter = ['status']

    search_fields = ['user_id']


    def image_name(self, obj):
        return bmimage.objects.get(uuid=obj.image_id).name

    def vnet_id(self, obj):
        vpc = bmvpc.objects.get(bm_uuid=obj.uuid)
        if (vpc != None):
            return vpc.vnet_uuid
        return None


admin.site.register(bm, bmAdmin)
admin.site.register(bmtype, bmtypeAdmin)
admin.site.register(bmimage, bmimageAdmin)
admin.site.register(bminfo, bminfoAdmin)

admin.site.disable_action('delete_selected')
