from django.urls import path
from .views import (
    CustomObtainAuthToken, QRCodeScanView, WarehouseListCreateView, WarehouseRetrieveUpdateDestroyView,
    ProductListCreateView, ProductRetrieveUpdateDestroyView,
    ProductStockListCreateView, ProductStockRetrieveUpdateDestroyView,
    InventoryTransactionListCreateView, InventoryTransactionRetrieveUpdateDestroyView
)

urlpatterns = [
    #login
    path('token-auth/', CustomObtainAuthToken.as_view(), name='api_token_auth'),

    # Bodegas
    path('warehouses/', WarehouseListCreateView.as_view(), name='warehouse-list-create'),
    path('warehouses/<int:pk>/', WarehouseRetrieveUpdateDestroyView.as_view(), name='warehouse-detail'),

    # Productos
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
    path('scan-qr/', QRCodeScanView.as_view(), name='scan-qr'),  

    # Stock de productos en bodegas
    path('product-stocks/', ProductStockListCreateView.as_view(), name='product-stock-list-create'),
    path('product-stocks/<int:pk>/', ProductStockRetrieveUpdateDestroyView.as_view(), name='product-stock-detail'),

    # Transacciones de inventario
    path('transactions/', InventoryTransactionListCreateView.as_view(), name='transaction-list-create'),
    path('transactions/<int:pk>/', InventoryTransactionRetrieveUpdateDestroyView.as_view(), name='transaction-detail'),

]
