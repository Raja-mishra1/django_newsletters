import math
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Newsletter
from .serializers import NewsletterSerializer


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
        print(data)
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
                
            Newsletter.objects.create(firstname=first_name, email=email,agree=agree) 
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
        