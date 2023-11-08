from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from apps.category.views import CategoryViewSet

router = SimpleRouter()
router.register('category', CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/account/', include('apps.account.urls')),
    path('api/v1/', include(router.urls)),
]

