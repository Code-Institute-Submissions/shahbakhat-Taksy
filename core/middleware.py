from django.contrib.auth import get_user_model

class ProfileMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        UserModel = get_user_model()
        user_id = request.session.get('user_id')

        if user_id:
            try:
                user = UserModel.objects.get(pk=user_id)
                if not hasattr(user, 'role'):
                    # Handle the case when the user model doesn't have a 'role' attribute
                    pass
                elif user.role == UserModel.Role.TAXIPASSENGER:
                    # Handle the logic for Taxi Passenger role
                    pass
                elif user.role == UserModel.Role.TAXIDRIVER:
                    # Handle the logic for Taxi Driver role
                    pass
            except UserModel.DoesNotExist:
                # Handle the case when the user is not found
                pass
        else:
            # Handle the case when the user is not authenticated
            pass

        response = self.get_response(request)
        return response
