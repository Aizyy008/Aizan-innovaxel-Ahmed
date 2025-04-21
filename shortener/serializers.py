# from rest_framework import serializers
# from .models import URL

# class URLSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = URL
#         fields = ['id', 'url', 'short_code', 'created_at', 'updated_at']
#         read_only_fields = ['id', 'short_code', 'created_at', 'updated_at']

# class URLStatsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = URL
#         fields = ['id', 'url', 'short_code', 'created_at', 'updated_at', 'access_count']
#         read_only_fields = ['id', 'short_code', 'created_at', 'updated_at', 'access_count']