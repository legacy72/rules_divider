from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions

from permissions import *
from .serializers import *


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    permission_classes = [BookPermission, ]
    filter_backends = [DjangoFilterBackend, ]
    filter_fields = ['id', 'name', 'author', 'date_of_issue', 'count_of_pages', 'price', ]

    def get_queryset(self):
        return Book.objects.all()


class FilmViewSet(viewsets.ModelViewSet):
    serializer_class = FilmSerializer
    permission_classes = [FilmPermission, ]
    filter_backends = [DjangoFilterBackend, ]
    filter_fields = ['id', 'name', 'date_of_issue', 'timing', 'price', ]

    def get_queryset(self):
        return Film.objects.all()


class MusicViewSet(viewsets.ModelViewSet):
    serializer_class = MusicSerializer
    permission_classes = [MusicPermission, ]
    filter_backends = [DjangoFilterBackend, ]
    filter_fields = ['id', 'name', 'date_of_issue', 'timing', 'price', ]

    def get_queryset(self):
        return Music.objects.all()
