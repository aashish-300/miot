from django.contrib import admin
from .models import User


# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'role', 'date_joined')
    search_fields = ('name', 'email', 'role', 'date_joined')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ('date_joined',)


admin.site.register(User, UserAdmin)
