from django.db import models
from django.core.urlresolvers import reverse

#------------Drop Down Fields------------------

#kids Field dropdown @ RegistrationPersonal
ADD_KIDS_NUMBER = (
	("0","NONE"),
	("1","01"),
	("2","02"),
	("3","03"),
	("4","04"),
	("5","05"),

)

#gender Field dropdown @ RegistrationPersonal
GENDER_TYPE = (
	('Male','MALE'),
	('Female','FEMALE'),
	('Others','OTHERS')
)

#gender Field dropdown @ RegistrationPersonal
BLOOD_GROUP = (
	('A+','A +ve'),
	('B+','B +ve'),
	('O+','O +ve'),
	('AB+','AB +ve'),
	('A-','A -ve'),
	('B-','B -ve'),
	('O-','O -ve'),
	('AB-','AB -ve')
)
#------------Drop Down Fields For Address------------------

#MateNmber dropdown @ RegistrationPersonal
MATE_NUMBER = (
	("0","NONE"),
	("1","01")
	)

SPOUS_NUMBER = (
	("0","NONE"),
	("1","01")
	)
KIDS_NUMBER = (
	("0","NONE"),
	("1","01"),
	("2","02"),
	("3","03"),
	("4","04"),
	("5","05"),

)
GUEST_NUMBER = (
	("0","NONE"),
	("1","01"),
	("2","02"),
	("3","03"),
	("4","04"),
	("5","05")
	)
OTHERS_NUMBER = (
	("0","NONE"),
	("1","01"),
	("2","02"),
	("3","03"),
	("4","04"),
	("5","05")
	)

DIVISION_ADDRESS = (
	("Barisal","Barisal"),
	("Chittagong","Chittagong"),
	("Dhaka","Dhaka"),
	("Khulna","Khulna"),
	("Mymensingh","Mymensingh"),
	("Rajshahi","Rajshahi"),
	("Rangpur","Rangpur"),
	("Sylhet","Sylhet")
	)


#------------Drop Down Fields For Payment------------------

#payment status dropdown @ RegistrationPersonal
PAYMENT_STATUS = (
	('Pending','PENDING'),
	('Processing','PROCESSING'),
	('Paid', 'PAID'),
    ('Unpaid','UNPAID')
)

#payment metho dropdown @ RegistrationPersonal
PAYMENT_METHOD = (
	('None','NONE'),
	('Cash','CASH'),
	('Bank','BANK'),
	('BKash', 'BKASH'),
    ('Others','OTHERS')
) 

# Create your models here.
class RegistrationPersonal(models.Model):
	name           = models.CharField(max_length=150) 
	image          = models.FileField(null=True, blank=True)
	spousname      = models.CharField(max_length=150, null=True, blank=True)
	gender         = models.CharField(max_length=30, choices=GENDER_TYPE, default='Male')
	kids           = models.CharField(max_length=30, null=True, blank=True,choices=ADD_KIDS_NUMBER, default="0" )
	mobilenumber   = models.CharField(max_length=30, unique=True)
	email          = models.EmailField(max_length=250, null=True, blank=True)
	bloodgroup     = models.CharField(max_length=30, choices=BLOOD_GROUP, default='None')
	profession     = models.CharField(max_length=150, null=True, blank=True)
	organization   = models.CharField(max_length=150, null=True, blank=True)
	timestamp      = models.DateTimeField(auto_now_add=True)
	updated        = models.DateTimeField(auto_now=True)

	def get_absolute_url(self):
		return reverse('author-detail', kwargs={'pk': self.pk})

	def __str__(self):
		return "%s %s" %(self.mobilenumber, self.name)

class RegistrationAddress(models.Model):
	registrationpersonal         = models.ForeignKey(RegistrationPersonal, on_delete=models.CASCADE)
	mobilenumber      = models.CharField(max_length=30, unique=True)
	address           = models.TextField(max_length=300)
	postcode          = models.CharField(max_length=10)
	thana             = models.CharField(max_length=60)
	district          = models.CharField(max_length=60)
	division          = models.CharField(max_length=45, choices=DIVISION_ADDRESS, default="Dhaka") 
	mate              = models.CharField(max_length=30,choices=MATE_NUMBER, default="1")
	spous             = models.CharField(max_length=30, choices=SPOUS_NUMBER, default="1")
	kids              = models.CharField(max_length=30, choices=KIDS_NUMBER, default="0")
	guests            = models.CharField(max_length=30, choices=GUEST_NUMBER, default="0")
	others            = models.CharField(max_length=30, choices=OTHERS_NUMBER, default="0")
	total             = models.CharField(max_length=100)
	note              = models.CharField(max_length=100)
	timestamp         = models.DateTimeField(auto_now_add=True)
	updated           = models.DateTimeField(auto_now=True)
	def __str__(self):
		return "%s %s %s" %(self.mobilenumber, self.total, self.district)

class RegistrationPayment(models.Model):
	registrationaddress   = models.ForeignKey(RegistrationAddress, on_delete=models.CASCADE)
	mobilenumber    	  = models.CharField(max_length=30, unique=True)
	payableamount   	  = models.CharField(max_length=200)
	paidamount      	  = models.CharField(max_length=200)
	method          	  = models.CharField(max_length=30, choices=PAYMENT_METHOD, default='None')
	details         	  = models.CharField(max_length=120)
	status                = models.CharField(max_length=30, choices=PAYMENT_STATUS, default='Unpaid')
	remarks         	  = models.CharField(max_length=120)
	timestamp       	  = models.DateTimeField(auto_now_add=True)
	updated          	 = models.DateTimeField(auto_now=True)
	def __str__(self):
		return "%s %s" %(self.mobilenumber, self.paidamount)


          						
