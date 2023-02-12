from rest_framework import serializers
from.models import desc



# class descserializers(serializers.Serializer):
# 	keyword = serializers.CharField(max_length=100)
# 	types = serializers.CharField(max_length=100)
# 	city = serializers.CharField(max_length=100)
# 	bedrooms = serializers.CharField(max_length=100)
# 	garages = serializers.CharField(max_length=100)
# 	price = serializers.CharField(max_length=100)
# 	avatar = serializers.ImageField(null=True,upload_to="../img",default="../default_avatar.png")

class modescserializers(serializers.ModelSerializer):
     class Meta:
         model=desc
         fields='__all__'