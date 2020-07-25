from django.contrib import admin

from .models import Referral, ReferralResponse

admin.site.register(
    Referral,
    list_display=[
        "user",
        "code",
        "label",
        "redirect_to",
        "target_content_type",
        "target_object_id"
    ],
    readonly_fields=["code", "created_at"],
    list_filter=["target_content_type", "created_at"],
    search_fields=["user__first_name", "user__last_name", "user__email", "user__username", "code"]
)

admin.site.register(
    ReferralResponse,
    list_display=[
        "referral",
        "created_at",
        "user",
        "ip_address",
        "referral_url",
        "action"
    ],
    readonly_fields=["referral", "session_key", "user", "ip_address", "action", "referral_url"],
    list_filter=["action", "created_at"],
    search_fields=["referral__code", "referral__user__username", "ip_address"]
)
