from rest_framework import serializers

from promotions.models import Promotion
from dealer.serializers import DealerSerializer


class PromotionSerializer(serializers.ModelSerializer):
    dealer = DealerSerializer()

    class Meta:
        model = Promotion
        fields = ('id', 'name', 'start_date', 'end_date', 'discount', 'dealer', 'created_at')
