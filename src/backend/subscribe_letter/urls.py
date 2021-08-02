from django.urls import path,include
from .views import LetterSignUpView

urlpatterns = [
    path('email-signup/', LetterSignUpView.as_view()),
]