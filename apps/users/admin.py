from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

from django.contrib.auth.models import User
from apps.users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user', 'getfullname', 'picture']
    list_display_links = ['pk']
    search_fields = ['user__email', 'user__username']
    list_filter = ['updated_at', 'user__date_joined', 'user__is_active']

    # readonly_fields = ['user']
    fieldsets = (
        ('Profile', {
            'fields': ('user', 'picture')
        }),
        ('Extra Information', {
            'fields': (
                # ('phone_number', 'biography', 'updated_at')
            )
        })
    )
    # list_editable = ['phone_number', 'picture']


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
