from rest_framework.generics import ListCreateAPIView
from .seralizers import CategorySerializer, ProductSerializer
from .models import Category, Product


# Create your views here.

class CategoryListCreateApiView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListCreateApiView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
