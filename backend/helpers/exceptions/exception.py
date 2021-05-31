from backend.helpers.exceptions.base import ApiCoreException


class AppBaseException(ApiCoreException):
    pass


class AppBadRequest(AppBaseException):
    status_code = 400
