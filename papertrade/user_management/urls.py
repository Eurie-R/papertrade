from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('tradehistory/', views.tradehistory, name='tradehistory'),
    path('portfolio/', views.portfolio, name='portfolio')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
app_name = 'user_management'