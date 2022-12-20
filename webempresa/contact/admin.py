from django.contrib import admin
from .models import Contact


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'email', 'content', 'created')
    list_display = ('name', 'email', 'created')


admin.site.register(Contact, ContactAdmin)
