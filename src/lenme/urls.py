from django.urls import path
from . import views

#from rest_framework.authtoken.views import obtain_auth_token
app_name = 'lenme'
urlpatterns = [
    path('api/request-loan',views.BorrowerCreateView.as_view(), name='loan_request'),
    path('api/make-offer', views.InvestorCreateOffer.as_view(), name='make_offer'),
    path('api/accept-offer', views.BorrowerAcceptOffer.as_view(), name='clients'),
    path('clients/', views.FinalizeOffer.as_view(), name='clients'),
    
]