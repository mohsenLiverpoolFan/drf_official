    'default':
        {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': '127.0.0.1',
            'PORT': 5438

        }

	STATIC_URL = "static/"
MEDIA_URL = "media/"

STATICFILES_DIRS = [
    BASE_DIR / "static"
]
MEDIA_ROOT = [BASE_DIR / "media"]
#------------------------------------
#url---------------------------------
from django.conf.urls.static import static
from django.conf import settings
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





