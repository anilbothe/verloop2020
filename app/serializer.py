from rest_framework import serializers
from app.models import GoodReadsAudit


class GoodReadsAuditSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodReadsAudit
        fields = '__all__'
        