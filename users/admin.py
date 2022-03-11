from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.forms import UserChangeForm, UserCreationForm
from users.models import CustomUser, UserProfile

"""
class CustomUserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ("email",)
    # list_filter = ("is_admin",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        # ("Personal info", {"fields": ("date_of_birth",)}),
        # ("Permissions", {"fields": ("is_admin",)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = ()


# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
"""


class UserProfileInline(admin.StackedInline):
    model = UserProfile


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    inlines = [UserProfileInline]


admin.site.register(UserProfile)
