"""langtuteng URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.views.static import serve
from django.conf import settings
from blog.uploads import upload_image
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('account/', include('account.urls')),
    re_path("^uploads/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT},),
    re_path('^admin/upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image')

]

urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


handler404 = "blog.views.page_not_found"
handler500 = "blog.views.page_error"