from rest_framework import serializers

from published_news.models import PublishedNew, Comment

class PublishedNewsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    url = serializers.CharField(max_length=200)
    by = serializers.CharField(max_length=200)
    score = serializers.IntegerField(default=0)
    item_type = serializers.CharField(max_length=50)
    comments = serializers.IntegerField(default=0)
    hacker_news_id = serializers.IntegerField(default=0)


    def create(self, validated_data):
        return PublishedNew.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.url = validated_data.get('url', instance.url)
        instance.by = validated_data.get('by', instance.by)
        instance.score = validated_data.get('score', instance.score)
        instance.item_type = validated_data.get('item_type', instance.item_type)
        instance.comments = validated_data.get('comments', instance.comments)
        instance.hacker_news_id = validated_data.get('hacker_news_id', instance.hacker_news_id)
        instance.save()
        return instance


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'