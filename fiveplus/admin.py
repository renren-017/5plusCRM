from django.contrib import admin

from fiveplus.models import Social


class SocialAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Social Links",
            {"fields": (("facebook", "twitter"), ("instagram", "linkedin"))},
        ),
    )
    empty_value_display = "-empty-"


admin.site.register(Social, SocialAdmin)
