from rest_framework import mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination

from rest_framework.viewsets import GenericViewSet

from apps.banks.models import Branch
from apps.banks.serializers.bank_and_branches import BranchSerializer


class ResponsePagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100


class BankAndBranchViewSet(mixins.ListModelMixin,
                           mixins.RetrieveModelMixin,
                           GenericViewSet):
    model = Branch
    serializer_class = BranchSerializer
    pagination_class = ResponsePagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['bank__name', 'city']
    lookup_field = 'ifsc'
    queryset = Branch.objects.all()
