from rest_framework import serializers

from apps.banks.models import Bank, Branch


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ('id', 'name')


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('id', 'bank', 'ifsc', 'branch', 'address', 'city', 'district', 'state')

    bank = BankSerializer()
