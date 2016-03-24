from django.http import *
from django.shortcuts import render
from last_app.models import *
from django.views.decorators.csrf import csrf_exempt
from django.template import Template, Context


components = []
formid = ""
myurl = ""
bypass_to_next_page = 0



'''
	1)This function will render the index.html initially. 
	2)After Pressing sign up button Again this will function will be called and if part will get executed.
	3)In else part it will redirect to homepage.html 
'''
@csrf_exempt	
def render_index_page(request):
	print "render"
	return render(request,'index.html')
	
@csrf_exempt	
def signup_function(request):
	if request.method == 'POST' :
		print "inside post"
		ash = request.POST.keys()
		print ash
		name = request.POST['username']
		username = request.POST['userid']
		password = request.POST['passid']
		email = request.POST['email']
		
		obj = Users(UserName = username , Password = password ,  Name = name , Email = email)
		obj.save()
		
		return HttpResponseRedirect('/index/')
	else:
		return render(request,'signup.html')
#===================================================================================================================================		
'''
	1)This function will aceept the data which is sent by ajax script by 'dta_user'
	2)It will verify username and password
	3)It will also handle whether all the fiels are filled or not
'''
@csrf_exempt	
def checkuser(request):
	global bypass_to_next_page
	if request.method == 'POST':
		ash = request.POST.keys() 
		print ash[0]
		str1 = ash[0]
		print str1
		i=0
		uname = ""
		while str1[i]!='\n':
			uname = uname + str1[i]
			i += 1
		password = ""	
		i = i+1
		while i<len(str1):
			print "loop"
			password = password + str1[i]
			i += 1
		
		print "Username is :- ",uname
		print "Password is :- ",password
		
		if uname=='' or password=='':
			return HttpResponse('empty')
		
		obj = Users.objects.filter(UserName = uname,Password = password)
		print str(obj)
		
		if len(obj)!=0:
			print "if"
			bypass_to_next_page = 1
			return HttpResponse("correct")
		else:
			print "else"
			return HttpResponse("Incorrect")
		return HttpResponse('Incorrect')	
#=========================================================================================================================================		



def render_homepage(request):
	global bypass_to_next_page
	print "In render_homepage function bypass_to_next_page = ",bypass_to_next_page 
	if bypass_to_next_page == 1:
		bypass_to_next_page = 0
		return render(request,'myfirstpage.html')
	else:
		return HttpResponseRedirect('/index/')
@csrf_exempt	
def render_generated_form(request,url_val):
	print "render_generated_form function"
	obtained_url = url_val
	print obtained_url
	obj = Myforms.objects.filter(form_id = obtained_url)
	print "obj is = ",obj
	if(len(obj)==0):
		return HttpResponse('Form not present')
	if request.method == 'POST':
		if 'submit' in request.POST:
			print "Submit pressed"
			ash = request.POST.keys()
			print ash
			#increment response count
			print "going to create answer objects..."
			answers_obj=answers.objects.filter(form_id=url_val)
			print answers_obj			
			temp_answer_cnt=int(answers_obj[0].answer_id)+1 
			print temp_answer_cnt
			print answers_obj[0].answer_id
			answers_obj.update(answer_id=str(temp_answer_cnt))
			print answers_obj[0].answer_id
			answers_obj[0].save()
			print answers_obj[0].answer_id

			for i in range(0,len(ash)):
				if 'txtlabel' in ash[i]:
					print ash[i]
					ans = Answer_TextField(form_id = obtained_url,answer_id = answers_obj[0].answer_id,textfield_id = ash[i],answer = request.POST[ash[i]])
					ans.save()
					print "saved"
						
					
		print "In POST"
		return HttpResponse("Thank you!!")
	else:
		list_of_elements = obj[0].components
		button_y = 0
		string_wtn_to_html = """<html>
		<body>
		<form action="" method=\"POST\">
		<table cellspacing="30">
		"""	
					
		#style = "position:absolute; left:"""+str(txt[0].x)+"""; top:"""+str(txt[0].y)+""" \"
		for i in range(0,len(list_of_elements)):
			if 'txtlabel' in list_of_elements[i]:
				txt = TextField.objects.filter(textfield_id = list_of_elements[i],form_id=url_val)
				print txt[0].textfield_id
				string_wtn_to_html = string_wtn_to_html + """
				<tr id=\""""+txt[0].textfield_id+"""\"  >
				<td><label>"""+txt[0].label_name+"""</label></td><td><input type=\""""+txt[0].type_name+"""\" placeholder = \""""+txt[0].place_holder+"""\"  name = \""""+txt[0].textfield_id+"""\" ></td>
				</tr>				
				"""
				if button_y < txt[0].y:
					button_y = txt[0].y
		
						
			#if ends here
		#for loop ends here
		print button_y
		string_wtn_to_html = string_wtn_to_html + """
	</table>
	{%csrf_token%}
	<input type=\"submit\" name=\"submit\" value=\"Submit\" style="position:absolute;left:10;top:"""+str(button_y+40)+""";\">
	</form>
	\n</body></html>"""
	
		fp = open('asdf.html','w')
		fp.write(string_wtn_to_html)
		fp.close()
	
		t = Template(string_wtn_to_html)
		html = t.render(Context({'error': 'fg'}))	
		return HttpResponse(html) 


@csrf_exempt
def checkfo(request):
	global formid
	global myurl
	if request.method == 'POST':
		ash = request.POST.keys()
		myurl = ash[0]
		obj = Myforms.objects.filter(form_id = myurl)
		print obj
		if(len(obj)==0):
			formid = myurl
			return HttpResponse('absent')
		else:
			return HttpResponse('present')				
	return HttpResponse('nopost')


@csrf_exempt	
def receive_ajax(request):
	global components
	global myurl
	
	if request.method == 'POST':
		ash = request.POST.keys()
		print "The ash contains:",str(ash)
		txtlabel_cnt = int(request.POST['txtlabel_cnt'])
		print txtlabel_cnt
		for i in range(0,txtlabel_cnt):
			temp = 'txtlabel'+str(i+1)
			chec = temp + '[name]'
			print i+1,"\n\n"
			if chec in ash:
				print "I am in"
				#if temp in components:
				#	print "already exists!!"
				#else:
				components.append(temp)
				name = request.POST[temp+'[name]']
				left = request.POST[temp+'[left]']
				top = request.POST[temp+'[top]']
				placeholder = request.POST[temp+'[placeholder]']
				typ = request.POST[temp+'[type]']
				ash.remove(temp+'[name]')
				ash.remove(temp+'[left]')
				ash.remove(temp+'[top]')
				ash.remove(temp+'[placeholder]')
				ash.remove(temp+'[type]')
				print ash
				try:
					obj = TextField(form_id=myurl,textfield_id = temp,x = int(float(left)),y = int(float(top)),label_name = name,type_name = typ,place_holder = placeholder,size = 20,maxlength = 50)
				except Exception as sd:
					print sd
				print "formid :- "+myurl
				print "id = "+temp
				print "x = "+left
				print "y = "+top
				#obj = TextField(form_id=str(myurl),textfield_id = str(temp),x = left,y = top,label_name = "sheyas",type_name = "text",place_holder = "sd",size = 20,maxlength = 50)
				print obj
				try:
					obj.save()
				except Exception as s:
					print s
					
				print "texlabel id = "+temp+" saved"
		print "exiting for loop"
	#------------------finally components is ready---------------------------------------------------------
	print "niru"	
	print components
	print "new form"
	nwf = Myforms(form_id = myurl,components = components)
	nw_answers=answers(form_id=myurl,answer_id=0)
	nwf.save()
	print "saved"
	nw_answers.save()
	components = []			
	print "sa"		
	return HttpResponse('{"message":"success"}',mimetype = 'application/json')				

