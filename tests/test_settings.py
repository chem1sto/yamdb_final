from django.test import override_settings

from api_yamdb import settings


class TestSettings:
    @override_settings(DEBUG=False)
    def test_settings(self):
        assert not settings.DEBUG, 'Проверьте, что DEBUG в настройках Django выключен'
