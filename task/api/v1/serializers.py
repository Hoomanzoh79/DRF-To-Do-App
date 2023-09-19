from rest_framework import serializers
from task.models import Task
from accounts.models import Profile


class TaskSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField(method_name='get_absolute_url')
    class Meta:
        model = Task
        fields = ['id','title','is_done','author','datetime_created','absolute_url']
        read_only_fields = ['author']
    

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author'] = Profile.objects.get(user_id = request.user.id)
        return super().create(validated_data)
    
    def get_absolute_url(self,obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)