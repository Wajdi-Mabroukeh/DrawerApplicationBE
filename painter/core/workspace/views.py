from django.http.multipartparser import MultiPartParser
from rest_framework import generics
from rest_framework.parsers import FormParser

from core.workspace.models import WorkSpace

from core.workspace.serializers import WorkSpaceSerializer, WorkSpaceMiniSerializer
from pagination.pagination import StandardResultsSetPagination


class WorkSpaceListAPIView(generics.ListAPIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = WorkSpaceMiniSerializer
    pagination_class = StandardResultsSetPagination
    ordering = ['-created_at']
    queryset = WorkSpace.objects.all()


class WorkSpaceCreateAPIView(generics.CreateAPIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = WorkSpaceSerializer
    queryset = WorkSpace


class WorkSpaceRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    # permission_classes = (IsAuthenticated,)
    # parser_classes = (MultiPartParser, FormParser,)
    lookup_field = 'uuid'
    serializer_class = WorkSpaceSerializer
    queryset = WorkSpace





