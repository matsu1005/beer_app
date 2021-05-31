from .settings_common import *

DEBUG = True

# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'メールアドレス'
# EMAIL_HOST_PASSWORD = 'パスワード'
# EMAIL_USE_TLS = True
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

