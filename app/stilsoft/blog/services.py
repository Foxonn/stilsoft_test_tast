from functools import wraps
from blog.exceptions import UserIsNotAuthor

from users.models import User
from blog.models import Post


def is_author_post(func):
    @wraps(func)
    def wrapper(self, request, *args, **kwargs):
        user = User.objects.only('id', 'is_superuser').get(id=request.user.pk)

        queryset_ = Post.objects.select_related('author').filter(
            author__id=user.id,
            id=kwargs.get('pk', None),
        )

        if not user.is_superuser and not queryset_:
            raise UserIsNotAuthor

        return func(self, request, *args, **kwargs)

    return wrapper
