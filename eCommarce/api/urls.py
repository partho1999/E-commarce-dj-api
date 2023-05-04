from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

#from rest_framework_nested import routers


router = DefaultRouter()

router.register("products", views.ProductsViewSet)
router.register("categories", views.CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
    # path("products/", views.ApiProducts.as_view()),
    # path("products/<str:pk>/", views.ApiProduct.as_view()),
    # # path("products/", views.api_products),
    # # path("products/<str:pk>/", views.api_product),
    # path("categories/", views.api_categories),
    # path("categories/<str:pk>", views.api_category),
]  