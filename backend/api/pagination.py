from rest_framework.pagination import PageNumberPagination


class RecipePagination(PageNumberPagination):
    """Пагинация рецептов."""

    page_size_query_param = 'limit'
    max_page_size = 6


class UserPagination(PageNumberPagination):
    """Пагинация пользователей."""

    page_size_query_param = 'limit'
    max_page_size = 100
