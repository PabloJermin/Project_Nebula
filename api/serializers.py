from rest_framework import serializers
from .models import Students

class StudSerializers(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'


# serializing the db credentials from user
class DbSerializer(serializers.Serializer):
    engine = serializers.ChoiceField(choices=[('postgresql', 'PostgreSQL'), ('mysql', 'MySQL'), ('sqlite3', 'SQLite')])
    name = serializers.CharField(max_length=100)
    user = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100, write_only=True, required=False)
    host = serializers.CharField(max_length=100, required=False, default='localhost')
    port = serializers.IntegerField() 