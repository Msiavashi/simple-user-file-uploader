from rest_framework import serializers
from .models import Template

class TemplateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Template
        fields = ('id', 'date_created', 'date_modified', 'file', 'owner', 'is_published', 'name')
        read_only_fields = ('date_created', 'date_modified')

        