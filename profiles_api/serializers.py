from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView"""
    name = serializers.CharField(max_length=10)
# from rest_framework import serializers
#
#
# class HelloSerializer(serializers.Serializer):
#     """seriallize name field for testing APIVIEW"""
#     ## Serializer that accepts name input into the api view to test POST functionality
#     ## Seraializer also takes care of validation, ensure the type of the content
#     name = serializers.CharField(max_length=10)
