from rest_framework import serializers
from django.db.models import Avg
from .models import Like


class LikePinSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Like
        fields = '__all__'

    def get_rate(self, object) -> float:
        rate =object.likes.aggregate(Avg('likes'))['likes__avg']
        if rate: return round(rate, 1)
        return None

