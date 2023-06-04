from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from ..models import Notification


def create_notification(recipient, ad, content):
    try:
        if not isinstance(recipient, User):
            raise ValidationError('Invalid user instance')
        notification = Notification(recipient=recipient, ad=ad, content=content)
        notification.save()

    except ValidationError as e:
        error_message = 'Пользователь не авторизован.'
        print(error_message)
        pass

    except Exception as e:
        error_message = 'Возникла ошибка.'
        print(error_message)
        pass
