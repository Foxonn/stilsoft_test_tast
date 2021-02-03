from rest_framework import generics
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin
)
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

from blog import serializers
from blog.models import Post
from blog.filters import PostsFilter
from blog import services


class ListPostsAPIView(
    ListModelMixin,
    CreateModelMixin,
    generics.GenericAPIView,
):
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)
    serializer_class = serializers.ListPostsSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    queryset = Post.objects.all()
    filterset_class = PostsFilter
    ordering_fields = ['title', 'publish', 'status']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer(self, *args, **kwargs):
        return super().get_serializer(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PostAPIView(
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    generics.GenericAPIView,
):
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)
    serializer_class = serializers.ListPostsSerializer
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['GET', 'POST', 'PUT', 'PATCH']:
            self.serializer_class = serializers.ListPostsSerializer

            if self.request.user.is_superuser and self.request.method != 'GET':
                self.serializer_class = serializers.PostSerializer

        return super(PostAPIView, self).get_serializer_class()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @services.is_author_post
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @services.is_author_post
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @services.is_author_post
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
