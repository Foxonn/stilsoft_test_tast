from rest_framework.exceptions import APIException


class UserIsNotAuthor(APIException):
    status_code = 200
    default_detail = 'You don`t have permissions.'
    default_code = 'permissions_error'
