from api_yamdb import settings


class TestSettings:
    def test_settings(self):
        assert not settings.DEBUG, 'Проверьте, что DEBUG в настройках Django выключен'
