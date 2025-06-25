from api.views import redirect_short_link
from django.urls import path

urlpatterns = [
    path(
        's/<str:short_code>/',
        redirect_short_link,
        name='redirect_short_link',
    ),
]
