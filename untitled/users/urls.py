from django.urls import path
from .views import SignUpView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns  = [
    path('signup/', SignUpView.as_view(), name='signup'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)