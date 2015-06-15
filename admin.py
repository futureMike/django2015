from django.contrib import admin

# Register your models here.

from .models import Join

class JoinAdmin(admin.ModelAdmin):
    list_display = ['email', 'timestamp', 'updated','join_reason', 'ip_address']
    class Meta:
        model = Join

admin.site.register(Join, JoinAdmin)
