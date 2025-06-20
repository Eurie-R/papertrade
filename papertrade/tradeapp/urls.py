from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('livemarket/', views.liveMarket, name="livemarket"),
    path('strategymanagement', views.strategyManagement, name='strategymanagement')
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
app_name = 'tradeapp'