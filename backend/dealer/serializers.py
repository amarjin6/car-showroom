from rest_framework import serializers

from dealer.models import Dealer


class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = ('id', 'name', 'location', 'created_at', 'last_update')
