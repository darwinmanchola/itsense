
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework import status, generics
from pyzbar.pyzbar import decode
from PIL import Image
import io

from .models import Warehouse, Product, ProductStock, InventoryTransaction
from .serializers import WarehouseSerializer, ProductSerializer, ProductStockSerializer, InventoryTransactionSerializer


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = token.user
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
            'email': user.email
        })




class WarehouseListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

class WarehouseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductStockListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = ProductStock.objects.all()
    serializer_class = ProductStockSerializer

    def perform_create(self, serializer):
        product = serializer.validated_data['product']
        warehouse = serializer.validated_data['warehouse']
        quantity = serializer.validated_data['quantity']
        # Lógica adicional si es necesario
        serializer.save()

class ProductStockRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    queryset = ProductStock.objects.all()
    serializer_class = ProductStockSerializer


class InventoryTransactionListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = InventoryTransaction.objects.all()
    serializer_class = InventoryTransactionSerializer

    def perform_create(self, serializer):
        transaction = serializer.save()
        # Actualiza el stock basado en la transacción
        stock, created = ProductStock.objects.get_or_create(
            product=transaction.product,
            warehouse=transaction.warehouse,
        )
        print(stock.quantity)
        print(transaction.transaction_type)
        print(transaction.quantity)
        if transaction.transaction_type == 'IN':
            stock.quantity += transaction.quantity
        elif transaction.transaction_type == 'OUT':
            stock.quantity -= transaction.quantity
        stock.save()
        print(stock.quantity)


class InventoryTransactionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    queryset = InventoryTransaction.objects.all()
    serializer_class = InventoryTransactionSerializer




class QRCodeScanView(APIView):
    def post(self, request, *args, **kwargs):
        image_file = request.FILES['image']
        image = Image.open(image_file)
        decoded_objects = decode(image)
        if decoded_objects:
            sku = decoded_objects[0].data.decode('utf-8')
            try:
                product = Product.objects.get(sku=sku)
                return Response({'product': product.name, 'sku': product.sku}, status=status.HTTP_200_OK)
            except Product.DoesNotExist:
                return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error': 'Invalid QR code'}, status=status.HTTP_400_BAD_REQUEST)