from django.shortcuts import render
from .serializers import BorrowSerializer , InvestorSerializer , BorrowerAcceptSerializer , FinalizeLoanSerializer
from rest_framework.parsers import JSONParser 
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# REST:
  #1. Borrower ==> Request.
  #2. Investor ==> Make an offer
  #3. Borrower ==> Accepts


class BorrowerCreateView(CreateAPIView):
    serializer_class = BorrowSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)  


class InvestorCreateOffer(CreateAPIView):
      serializer_class = InvestorSerializer

      def post(self, request, *args, **kwargs):
            return self.create(request, *args, **kwargs) 


class BorrowerAcceptOffer(CreateAPIView):
      serializer_class = BorrowSerializer

      def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)  



class FinalizeOffer(CreateAPIView):
      '''
      Finalize offer ==> make loan status = Completed
      '''
      serializer_class = FinalizeLoanSerializer

      def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) 








