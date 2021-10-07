from django.shortcuts import render
import pymongo

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.contrib import messages 
import ssl
import dns
import pymongo
from pymongo import MongoClient




# loginpage views.
def loginform(request):    
    return render(request, 'authenticate/login.html')

# questionidpage views.
def questionid(request):    
    print(request.method)
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # print(email)
        # print(password)
        connection_url= "your-connection_url"
        client = pymongo.MongoClient(connection_url, ssl_cert_reqs=ssl.CERT_NONE)
        db = client.'your-dbname'
        udetails = db.get_collection("your-collectionname")

        ##checking user email and password. 
        userdetails = udetails.find({ "email": email, "password": password })
        questiondata = []

        ## get all questions.
        if len(list(userdetails.clone())) > 0:
            for updatequestion in userdetails:  
                # print(updatequestion['questions'])
                questionsid = updatequestion['questions']
                ## Get only questionid from the array
                for question in questionsid:
                    ind = question.index(':')+2 
                    ssub = question[ind:len(question)]
                    #print(ssub)
                    questiondata.append(ssub)
            ##passing all the questionid to display htmlpage
            context= {
                'questionlist': questiondata,    
            }
        return render(request, 'questionid.html', context=context)
    messages.error(request,("Invalid email or password Try again"))
    return render(request, 'authenticate/login.html')

