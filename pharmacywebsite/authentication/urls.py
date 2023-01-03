# from django.urls import path
# from . views import LoginView

# urlpattern = [
#     path('login', LoginView.as_view(), name='login')
# ]


from django.urls import path
from .views import LoginView

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
]
