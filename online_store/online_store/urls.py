from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# handler404 = "core.views.page_not_found" здесь будет кастомная обработка ошиибки 404
# handler403 = 'core.views.permission_denied'здесь будет кастомная обработка ошиибки 403

urlpatterns = [
    path("admin/", admin.site.urls),
    path("cart/", include("cart.urls", namespace="cart")),
    path('orders/', include('orders.urls', namespace='orders')),
    path('payment/', include('payment.urls', namespace='payment')),
    path("posts/", include("posts.urls", namespace="posts")),
    path("", include("shop.urls", namespace="shop")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
