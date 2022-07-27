# docregister
Installations 
pip install django 
pip install pillow
pip install mysqlclient


Add to settings 
For media files 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')  
MEDIA_URL = '/media/'

For static files 
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

Add to urls.py
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
 
 for configurations of images
