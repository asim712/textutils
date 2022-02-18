from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Gettting the text 
    djtext=request.POST.get('text','default')

    # Getting the checkbox value 
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercount = request.POST.get('charactercount', 'off')

    # Check which checkbox is on 
    if removepunc=='on':
        punctuations = """!@#$%^&*()_+=-:;,./~`{}[]"""
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params ={'purpose':'Removed Punctuation', 'analyzed_text': analyzed}
        djtext= analyzed

    if(fullcaps=='on'):
        analyzed =""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose':'Changed to Upper Case', 'analyzed_text': analyzed}
        djtext=analyzed
    
    if(newlineremover=='on'):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed+char
        params = {'purpose':'Changed to Upper Case','analyzed_text':analyzed}

        djtext=analyzed
    
    if(extraspaceremover=='on'):
        analyzed=''
        for index,char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index + 1]==" "):
                analyzed = analyzed+char

        params={'purpose':'Extra Space Remover','analyzed_text':analyzed}
        djtext = analyzed


    if(charactercount=='on'):
        analyzed=0
        for i in djtext:
            analyzed=analyzed+1
        params={'pupose':'Count the Character','analyzed_text':analyzed}
        djtext=analyzed
    
    return render(request, 'analyze.html', params)


    



