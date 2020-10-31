from django.contrib import admin
from .models import SliderIndex,SliderGaleria,MisionVision,Insumos


# Register your models here.

class SliderIndexAdmin(admin.ModelAdmin):
    list_display=['ident','imagen']
    search_fields=['ident','imagen']
    list_per_page = 10

class SliderGaleriaAdmin(admin.ModelAdmin):
    list_display=['ident','slider1','slider2']
    search_fields=['ident','slider1','slider2']
    list_per_page = 10

class MisionVisionAdmin(admin.ModelAdmin):
    list_display=['ident','mision','vision']
    search_fields=['ident','mision','vision']
    list_per_page = 10

class InsumosAdmin(admin.ModelAdmin):
    list_display=['nombre','precio','descripcion','stock']
    search_fields=['nombre','precio','descripcion','stock']
    list_per_page = 10




admin.site.register(SliderIndex,SliderIndexAdmin)
admin.site.register(SliderGaleria,SliderGaleriaAdmin)
admin.site.register(MisionVision,MisionVisionAdmin)
admin.site.register(Insumos,InsumosAdmin)

