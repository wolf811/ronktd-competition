from django.contrib import admin

from users.models import CustomUser, UserProfile

# Register your models here.


class UserProfileInline(admin.StackedInline):
    model = UserProfile


# admin.site.register(CustomUser)


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    inlines = [UserProfileInline]


admin.site.register(UserProfile)
