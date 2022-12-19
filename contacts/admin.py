from django.contrib import admin
from .models import Categories, Contacts


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'country', 'category',
                    'hidecontact')
    list_display_links = ('id', 'name', 'surname')
    list_filter = ('country', 'category')
    list_per_page = 15
    list_editable = ('hidecontact',)


admin.site.register(Categories)
admin.site.register(Contacts, ContactsAdmin)
