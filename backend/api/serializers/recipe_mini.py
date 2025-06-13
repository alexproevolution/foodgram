from drf_extra_fields.fields import Base64ImageField
from recipes.models import Recipe
from rest_framework import serializers


class RecipeMiniSerializer(serializers.ModelSerializer):
    """
    Базовый сериализатор рецепта.
    """
    image = Base64ImageField()

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'image', 'cooking_time')
