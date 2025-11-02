"""
unfold ui settings.
"""
from src.settings import base
from src.settings.dashboard import sidebar
from src.settings.dashboard import site

IS_UNFOLD_UI_ENABLED = True


if IS_UNFOLD_UI_ENABLED:
    for index, app in enumerate([
        'unfold',
        'unfold.contrib.forms',
        'unfold.contrib.filters',
        'unfold.contrib.import_export',
        'unfold.contrib.guardian',
        'unfold.contrib.simple_history',
    ]):
        base.INSTALLED_APPS.insert(
            index, app,
        )

    UNFOLD = {}

    UNFOLD.update(
        site.SITE,
    )
    UNFOLD.update(
        sidebar.SIDEBAR
    )
