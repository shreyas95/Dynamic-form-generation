from django.db import models
from djangotoolbox.fields import EmbeddedModelField,ListField
# Create your models here.

class Users(models.Model):
    UserName = models.CharField(max_length = 50)
    Password = models.CharField(max_length = 20)
    Name = models.CharField(max_length = 50)
    Email = models.CharField(max_length = 50)
    
#-----------------------------------------------------------------------------------------    
class Myforms(models.Model):
    form_id = models.CharField(max_length = 50)                               #url or form name
    components = ListField(models.CharField())				   #list of id of all components

# This will contain information for rendering the form    
# -------------------------------------start----------------------------------------------
class TextField(models.Model):                                 #All attributes of textfield
	textfield_id = models.CharField(max_length = 50)
	form_id = models.CharField(max_length = 50)
	x = models.IntegerField()
	y = models.IntegerField()
	label_name = models.CharField(max_length = 50)
	type_name = models.CharField(max_length = 50)
	place_holder = models.CharField(max_length = 50)
	size = models.IntegerField()
	maxlength = models.IntegerField()
	
class Label(models.Model):									   #All attributes of label
	label_id = models.CharField(max_length = 50)
	form_id = models.CharField(max_length = 50)
	x = models.IntegerField()
	y = models.IntegerField()
	label_name = models.CharField(max_length = 50)	

class label_number(models.Model):							   #All attributes of label_number
	label_number_id = models.CharField(max_length = 50)
	x = models.IntegerField()
	form_id = models.CharField(max_length = 50)
	y = models.IntegerField()
	label_name = models.CharField(max_length = 50)
	place_holder = models.CharField(max_length = 50)
	size = models.IntegerField()
	maxlength = models.IntegerField()
	min_number = models.FloatField()
	max_number = models.FloatField()
	step = models.FloatField()

class label_date(models.Model):								   #All attributes of label_date
	label_date_id = models.CharField(max_length = 50)
	form_id = models.CharField(max_length = 50)
	x = models.IntegerField()
	y = models.IntegerField()
	label_name = models.CharField(max_length = 50)
	
class label_textarea(models.Model):  						   #All attributes of textarea
	label_textarea_id = models.CharField(max_length = 50)
	form_id = models.CharField(max_length = 50)
	x = models.IntegerField()
	y = models.IntegerField()
	label_name = models.CharField(max_length = 50)
	place_holder = models.CharField(max_length = 50)
	maxlength = models.IntegerField()
	num_of_rows = models.IntegerField()
	num_of_column = models.IntegerField()	
	
class mcq(models.Model):									   #All attributes of mcq
	mcq_id = models.CharField(max_length = 50)
	form_id = models.CharField(max_length = 50)
	mcq_type = models.CharField(max_length = 50)
	x = models.IntegerField()
	y = models.IntegerField()
	question = models.CharField(max_length = 50)
	comment = models.CharField(max_length = 50)
	options = ListField(models.CharField())
#-------------------------------------------end-------------------------------------------------
#This section contains answers filled by the enduser in particular form
#-------------------------------------start------------------------------------------------------
class answers(models.Model):
	form_id = models.CharField(max_length = 50)                              #same form_id used in Myforms class            
	answer_id = models.CharField(max_length = 50)							  #count of response or can be treated as number of people who fill this form
	
class Answer_TextField(models.Model):						  #Answers of all textfields in all forms of all people i.e. of all responses
	form_id = models.CharField(max_length = 50)
	answer_id = models.CharField(max_length = 50)
	textfield_id = models.CharField(max_length = 50)
	answer = models.CharField(max_length = 50)
	
class Answer_label_number(models.Model):					  #Answers of all label_number in all forms of all people i.e. of all responses
	form_id = models.CharField(max_length = 50)
	answer_id = models.CharField(max_length = 50)
	label_number_id = models.CharField(max_length = 50)
	answer = models.FloatField()
	
class Answer_label_date(models.Model):                        #Answers of all label_date in all forms of all people i.e. of all responses
	form_id = models.CharField(max_length = 50)
	answer_id = models.CharField(max_length = 50)
	label_date_id = models.CharField(max_length = 50)
	answer = models.DateField()

class Answer_TextArea(models.Model):                          #Answers of all textarea in all forms of all people i.e. of all responses
	form_id = models.CharField(max_length = 50)
	answer_id = models.CharField(max_length = 50)
	textarea_id = models.CharField(max_length = 50)
	answer = models.CharField(max_length = 50)	
	
class Answer_mcq(models.Model):                               #Answers of all mcq in all forms of all people i.e. of all responses
	form_id = models.CharField(max_length = 50)
	answer_id = models.CharField(max_length = 50)
	mcq_id = models.CharField(max_length = 50)
	answer = ListField(models.CharField(max_length = 50))
	comment = models.CharField(max_length = 50)
#----------------------------------------end-----------------------------------------------------	    
