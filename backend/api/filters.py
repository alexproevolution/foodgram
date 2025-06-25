from django_filters.rest_framework import FilterSet, filters
from recipes.models import Ingredient, Recipe


class IngredientFilter(FilterSet):
    """Фильтр для поиска ингредиентов."""

    name = filters.CharFilter(
        field_name='name',
        lookup_expr='istartswith',
        help_text='Название ингредиента (по начальным буквам)',
    )

    class Meta:
        model = Ingredient
        fields = ['name']


class RecipeFilter(FilterSet):
    """Фильтр для рецептов."""

    tags = filters.AllValuesMultipleFilter(
        field_name='tags__slug',
        help_text='Фильтрация по слагам тегов',
    )
    is_favorited = filters.BooleanFilter(
        field_name='is_favorited',
        help_text='Фильтр по избранному',
    )
    is_in_shopping_cart = filters.BooleanFilter(
        field_name='is_in_shopping_cart',
        help_text='Фильтр по корзине',
    )

    class Meta:
        model = Recipe
        fields = [
            'tags',
            'author',
            'is_favorited',
            'is_in_shopping_cart',
        ]

    def filter_queryset(self, queryset):
        """Отключение фильтров для анонимных пользователей."""
        if not self.request.user.is_authenticated:
            self.form.cleaned_data.pop('is_favorited', None)
            self.form.cleaned_data.pop('is_in_shopping_cart', None)

        return super().filter_queryset(queryset)
