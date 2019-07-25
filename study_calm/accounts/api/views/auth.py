import requests
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response

client_id = '104920276036-rjej0o22m2f66onl14j5104bqmac59ri.apps.googleusercontent.com'
client_secret = 'IMidycICAwGJv6jvwqZ3pTso'
redirect_uri = 'http://localhost:1234/auth/callback/'
# https://www.googleapis.com/oauth2/v4/token
class CallBackView(views.APIView):

    def get(self, request, **kwargs):
        error = request.GET.get('error')
        state = request.GET.get('state')
        code = request.GET.get('code')
        scope = request.GET.get('scope')
        session_state = request.GET.get('state')
        prompt = request.GET.get('prompt')
        print(scope)
        if error:
            print('worng')

        r = requests.post(
            'https://www.googleapis.com/oauth2/v4/token/',
            data = {
                'code': code,
                'client_id': client_id,
                'client_secret': client_secret,
                'redirect_uri': redirect_uri,
                'grant_type': 'authorization_code'
            }
        )
        if r.status_code == 200:
            return Response(data=r.content,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


callback = CallBackView.as_view()


class TokenView(views.APIView):

    def get(self, request, **kwargs):
        print('cegeg')
        print(request.GET)
        print(kwargs)
        return Response(data='token 123415',status=status.HTTP_200_OK)

token = TokenView.as_view()


'''
https://accounts.google.com/o/oauth2/v2/auth?
 scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdrive.metadata.readonly&
 access_type=offline&
 include_granted_scopes=true&
 state=state_parameter_passthrough_value&
 redirect_uri=http%3A%2F%2Flocalhost:1234/auth/callback/&
 response_type=code&
 client_id=client_id

'''