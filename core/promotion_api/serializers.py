from rest_framework import serializers


class Clients(serializers.Serializer):
    client_id = serializers.UUIDField(required=True)
    business_name = serializers.CharField(required=True, max_length=200)
    prefix = serializers.CharField(required=True, max_length=4)
    description = serializers.CharField(required=True, max_length=250)

    def create(self, validated_data):
        return Clients.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.business_name = validated_data.get('business_name', instance.business_name)
        instance.prefix = validated_data.get('prefix', instance.prefix)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


"""class PromotionsSerializer(serializers.Serializer):
     description
    name
    url
    active
    start_date
    end_date
    img_url
    promotion_type_id
    promotion_status_id
    client_id
    return instance

    """
