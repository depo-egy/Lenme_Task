from django.db import models
import random
from string import ascii_uppercase
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from dateutil.relativedelta import relativedelta

CHOICES = (
	('Funded' , 'Funded'),
	('Completed','Completed')
	)

class Borrower(models.Model):
	fName = models.CharField(blank=False, max_length=50)
	lName = models.CharField(blank=False, max_length=50)
	email = models.CharField(blank=False, max_length=100)
	hasRequest = models.BooleanField(default=False)
	amntToBorrow = models.IntegerField(blank=False , default = 0)
	reasonToBorrow = models.TextField(blank=False, max_length=50)
	loanPeriod = models.IntegerField(blank=False , default = 1)
	offerReceived = models.BooleanField(default=False)
	offerAccepted = models.BooleanField(default=False)

	def __str__(self):
		return self.fName +" " +self.lName

class Investor(models.Model):
	fName = models.CharField(blank=False, max_length=50)
	lName = models.CharField(blank=False, max_length=50)
	email = models.CharField(blank=False, max_length=100)
	investorBalance = models.IntegerField(blank=False , default = 0)
	makeOffer = models.BooleanField(default=False)

	def make_offer(self ,pk):
		pass

	def __str__(self):
		return self.fName +" " +self.lName

class Loan(models.Model):
	investor = models.ForeignKey(Investor , on_delete= models.CASCADE)
	borrower = models.ForeignKey(Borrower , on_delete= models.CASCADE)
	loanAmount = models.IntegerField(null=False)
	totalLoanAmount = models.IntegerField(null=False) # loan amount + lenme fee + 0.15*loan amount
	loanPeriod =  models.DurationField()
	annualInterestRate  = models.FloatField()
	startDate = models.DateField()
	status  = models.CharField(choices = CHOICES , max_length= 10 , default="Funded")

	def __str__(self):
		letters = ascii_uppercase
		code= ''.join(random.choice(letters) for i in range(8))
		return code
    
	@property
	def loan_duration(self , instance):
		period = Borrower.open(instance.loanPeriod)
		d1 = datetime.date.today()
		self.loanPeriod = + relativedelta(months=period)
		return self.loanPeriod

	@property
	def totalLoan(self , instance):
		self.totalLoanAmount = 1.15*self.loanAmount + 3 
		return self.totalLoanAmount

    

@receiver(post_save, sender=Borrower)
@receiver(post_save, sender=Investor)
def initiate_loan(sender, bfName , blName , ifName , ilName, **kwargs):
	borrower = Borrower.objects.get(fName = bfName , lName = blName)
	investor = Investor.objects.get(fName = ifName , lName = ilName)
post_save.connect(initiate_loan, sender = Borrower)
post_save.connect(initiate_loan, sender = Investor)    