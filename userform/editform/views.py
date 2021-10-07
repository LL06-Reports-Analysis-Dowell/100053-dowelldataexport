import requests
import logging
import json

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# updateformpage views.
def updateform(request):

    ## Debugging Requests

    # logging.basicConfig()
    # logging.getLogger().setLevel(logging.DEBUG)
    # requests_log = logging.getLogger("requests.packages.urllib3")
    # requests_log.setLevel(logging.DEBUG)
    # print(request.POST.get('question'))

    ##QuestionId getting from questionid page
    quesid = request.GET.get("quesid")
    context ={
                'questionid': quesid,
                    
                } 
    if  request.POST.get('question'):
        questionid = request.POST.get("hid-question-id")##Get the value from hidden questionid field
        token = 'your-token'
        hed = {'Authorization': 'Bearer ' + token,'Content-Type':'application/json'}
        url="https://api.videoask.com/questions/"+questionid
        updatequestion = request.POST.get('question')

        ##update the question 

        payload = {
                "metadata": {
                "text": updatequestion}}


        print(requests.patch(url, data=json.dumps(payload), headers=hed))

    return render(request, "updateform.html", context=context)
    
# logotpage views.
def logout(request):
        return redirect('authenticate/login')


