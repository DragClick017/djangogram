"""
Navigation settings.
Icons are: https://fonts.google.com/icons
"""
from django.urls import reverse_lazy

MAIN = {
    "title": "Main",
    "separator": True,
    "items": [
        {
            "title": ("Users"),
            "icon": "groups",
            "link": reverse_lazy("admin:bot_users_changelist"),
        },
    ],
}

NAVIGATION = [
    MAIN,
]
