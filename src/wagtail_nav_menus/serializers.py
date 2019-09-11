from rest_framework import serializers
from .models import NavMenu


class NavMenuSerializer(serializers.ModelSerializer):
    menu = serializers.SerializerMethodField()

    class Meta:
        model = NavMenu
        fields = ('site', 'name', 'menu')
    
    def get_menu(self, obj):
        return obj.menu.stream_data
