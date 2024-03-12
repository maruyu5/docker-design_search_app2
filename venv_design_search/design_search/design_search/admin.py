from django.contrib import admin
from .models import EmailModel
from .models import Inquiry

# /adminの表示を制御
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('shiji_no', 'name', 'email', 'purpose', 'created_at')
    readonly_fields = ('created_at',)

admin.site.register(Inquiry, InquiryAdmin)

admin.site.register(EmailModel)

