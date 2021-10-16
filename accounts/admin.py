from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import User


class UserAdminstrator(UserAdmin):

    ordering = ('username',)
    list_display = ('username', 'email', 'is_admin',)
    search_fields = ('username', 'email',)
    readonly_fields = ('date_joined', 'last_login',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Information', {
         'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_staff',
         'is_admin', 'is_superuser', 'is_active')}),
        ('Important Dates', {'fields': ('date_joined', 'last_login')}),
    )


admin.site.register(User, UserAdminstrator)
