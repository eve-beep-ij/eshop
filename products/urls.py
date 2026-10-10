from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ProductImageViewSet, CategoryViewSet

router = DefaultRouter()

router.register("products", ProductViewSet, basename="products")
router.register("product-images", ProductImageViewSet, basename="product-images")
router.register("product-categories", CategoryViewSet, basename="categories")

urlpatterns = router.urls