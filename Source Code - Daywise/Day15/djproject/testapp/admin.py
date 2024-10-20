from django.contrib import admin
from testapp.models import Hydjobs,blrjobs,Punejobs,Chennaijobs



# Register your models here.
class hydjobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']
    
class chennaijobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']
        
class blrjobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']
            
class punejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

admin.site.register(Hydjobs,hydjobsAdmin)
admin.site.register(Chennaijobs,chennaijobsAdmin)
admin.site.register(blrjobs,blrjobsAdmin)
admin.site.register(Punejobs,punejobsAdmin)


            