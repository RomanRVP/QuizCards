from django.shortcuts import redirect


class RedirectionUnauthorizedUsersMiddleware:
    """
    Users who are not logged in have a limited list of available URLs.
    """

    def __init__(self, get_response):
        self._get_response = get_response
        self.available_urls = ('/account/registration_and_login/',)

    def __call__(self, request):
        if not request.user.is_authenticated:
            if request.path not in self.available_urls:
                return redirect('reg_and_log')
        response = self._get_response(request)
        return response
