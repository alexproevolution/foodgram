from django.core.validators import RegexValidator

USERNAME_PATTERN_VALIDATOR = RegexValidator(
    regex=r'^[\w.@+-]+$',
    message=(
        'Имя пользователя может содержать только буквы, '
        'цифры и символы @/./+/-/_'
    )
)
