import math
import requests
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.conf import settings

from .models import Newsletter
from .serializers import NewsletterSerializer

MAIL_CHIMP_API_KEY = settings.MAIL_CHIMP_API_KEY
MAIL_CHIMP_DATA_CENTER = settings.MAIL_CHIMP_DATA_CENTER
MAIL_CHIMP_EMAIL_LIST_ID = settings.MAIL_CHIMP_EMAIL_LIST_ID

api_url = f'https://{MAIL_CHIMP_DATA_CENTER}.api.mailchimp.com/3.0/'

members_endpoint = f'{api_url}/lists/{MAIL_CHIMP_EMAIL_LIST_ID}/members'


def subscribe_email(email,first_name):
    """[Adds email to subscriber list in mailchimp]

    Args:
        email ([str]): [email of user]
        first_name ([str]): [name of user]

    Returns:
        [JSON]: [returns response from mailchimp api ]
    """
    data = {
        'email_address': email,
        'status': 'subscribed',
        'full_name': first_name,
        }
    r = requests.post(
        members_endpoint,
        auth = ("", MAIL_CHIMP_API_KEY),
        data = json.dumps(data),
        
    )
    
    return r.status_code, r.json()


class LetterSignUpView(APIView):
    """[View to allow user to post data as well as get data for newsletter]

    Args:
        APIView ([type]): [django APIView]
    """
    def post(self,request,format=None):
        """[Allows user to post data from endpoint]

        Args:
            request ([type]): [data received from endpoint]
            format ([type], optional): [description]. Defaults to None.

        Returns:
            [JSON]: [response from endpoint]
        """
        data = self.request.data  
        first_name = data['first_name']
        email = data['email']
        agree = data['agree']
        try:
            try:
                agree = bool(agree)
            except:
                return Response(
                    {'error': 'Please agree to Privacy Policy and Terms of Service'},
                    status= status.HTTP_400_BAD_REQUEST
                )
        
            if not agree:
                return Response(
                    {'error': 'Please agree to Privacy Policy and Terms of Service'},
                    status= status.HTTP_400_BAD_REQUEST
                )
            user_signed_up_already = Newsletter.objects.filter(firstname=first_name)
            if user_signed_up_already:
                 return Response(
                    {'Success': 'You have already signed up for newsletter list'},
                    status= status.HTTP_200_OK
                )
            else: 
                Newsletter.objects.create(firstname=first_name, email=email,agree=agree)
                # adding to subscriber list in mailchimp
                mail_sent = subscribe_email(email,first_name)
                return Response(
                    {'Success': 'Contact added successfully to newsletter list'},
                    status= status.HTTP_200_OK
                )
        except Exception as e:
            return Response(
                {'error': f"{e}"},
                status= status.HTTP_400_BAD_REQUEST
            )
            
    def get(self, request, *args, **kwargs):
        """[Returns paginated response for all user signed up through newsletter]

        Args:
            request ([type]): [expects page number in request]

        Returns:
            [JSON]: [Response from Database, page number and Status code]
        """
        page = int(request.GET.get("page", 1))
        per_page = 9
        data = Newsletter.objects.all()
        serializer = NewsletterSerializer(data,many=True)
        total = len(serializer.data)
        start = (page - 1) * per_page
        end = page + per_page
            
        return Response({
                    "data": serializer.data[start:end],
                    "total": total,
                    "page": page,
                    "last_page": math.ceil(total / per_page),
                })
        