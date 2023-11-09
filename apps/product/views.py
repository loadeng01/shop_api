from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .models import Product
from .serializers import *
from .permissions import IsAuthorOrAdmin
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class Pagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = Pagination
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('title',)
    filterset_fields = ('category', 'stock')

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return IsAuthenticated(), IsAuthorOrAdmin(),
        return IsAuthenticatedOrReadOnly(),

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
