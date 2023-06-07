from django.contrib import admin
from .models import Candidate
from django.utils.html import format_html

# Register your models here.

class CandidateAdmin(admin.ModelAdmin):
    list_filter = ['situation']
    list_display=['firstname', 'lastname', 'email', 'job', 'age','created_at', 'status', '_']
    search_fields =['firstname', 'lastname', 'email', 'age', 'situation']
    list_per_page = 10
    
    # function to change the icons
    def _(self, obj):
        if obj.situation == 'Approved':
            return True
        elif obj.situation == 'Pending':
            return None
        else:
            return False
    _.boolean = True

    # function to color the text
    def status(self, obj):
        if obj.situation == 'Approved':
            color = '#28a745'
        elif obj.situation == 'Pending':
            color = '#f2a95e'
        else:
            color = 'red'
        return format_html('<strong><p style="color:{}>{}</p></strong>'.format(color, obj.situation))
    status.allow_tags = True

admin.site.register(Candidate, CandidateAdmin)