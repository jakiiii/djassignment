from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from accounts.models import User

from accounts.forms import UserAdminCreationForm, UserAdminChangeForm


@admin.register(User)
class UserAdmin(UserAdmin):
    add_form = UserAdminCreationForm
    form = UserAdminChangeForm
    model = User

    list_display = ['username', 'email', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'is_operator', 'is_active']
    list_filter = ['is_superuser', 'is_staff', 'is_operator']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    readonly_fields = ['last_login', 'date_joined']

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_superuser', 'is_staff', 'is_operator')}),
        ('Others', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_active', 'is_superuser', 'is_staff', 'is_operator')}
         ),
    )


admin.site.unregister(Group)
