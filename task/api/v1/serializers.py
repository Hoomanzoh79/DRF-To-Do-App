from rest_framework import serializers
from task.models import Task
from accounts.models import Profile


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','title','is_done','author','datetime_created']
        read_only_fields = ['author']
    

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author'] = Profile.objects.get(user_id = request.user.id)
        return super().create(validated_data)