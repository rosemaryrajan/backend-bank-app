from rest_framework.routers import DefaultRouter

from apps.banks.viewsets import BankAndBranchViewSet

default_router = DefaultRouter()
default_router.register(r'branch-details', BankAndBranchViewSet, basename='branch-details')

urlpatterns = default_router.urls
