from rest_framework import serializers
from .models import Borrower , Investor , Loan



class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower 
        fields = '__all__'
        exclude = ('offerReceived', 'offerAccepted')



class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor
        fields = '__all__'

        @property
        def validate_balance(self ,fName, lName ): #first name and last name of certain borrower
            defaults = {'offerReceived': 'False'}
            new_value = {'offerReceived': 'True'}
            borrower = Borrower.objects.get(fName=fName, lName = lName)
            if self.investorBalance >= (borrower.amntToBorrow + 3):
                borrower = Borrower(**new_value)
                borrower.save()



class BorrowerAcceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower 
        fields = ('offerAccepted')

        @property
        def accept_offer(self ,fName, lName ): #first name and last name of certain borrower
            defaults = {'offerAccepted': 'False'}
            new_value = {'offerAccepted': 'True'}
            borrower = Borrower.objects.get(fName=fName, lName = lName)
            if borrower.offerReceived == True:
                borrower = Borrower(**new_value)
                borrower.save()

        



class FinalizeLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ('status')


    