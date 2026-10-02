from rest_framework.routers import DefaultRouter
from .views import ProductsViewSet, ProductImageViewSet, CategoryViewSet

router = DefaultRouter()

router.register("products", ProductsViewSet, basename="products")
router.register("product-images", ProductImageViewSet, basename="product-images")
router.register("product-categories", CategoryViewSet, basename="categories")

urlpatterns = router.urls