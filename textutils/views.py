from django.http import HttpResponse
from django.shortcuts import render

def index(request):
     return render(request,'index.html')

def analyze(request):
    # Get the text
    djtext=request.POST.get('text','default')

    # Check checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcps = request.POST.get('fullcps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')

    # Punctuations remover if else conditions
    if removepunc == 'on':
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ''
        # This is for loop to check punctions and add in char to analyzed variable
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        #This is params arguments which will take this dicnaory into analyze.html variables
        params = {'purpose':'Removed punctions','analyzed_text':analyzed}
        djtext = analyzed
        #Analyize the text
        # return render(request,'analyze.html',params)

    # UPPERCASE if else conditions
    if  (fullcps == "on"):
        analyzed =""
        for char in djtext:
            analyzed = analyzed +char.upper()
        # This is params arguments which will take assign values of variables in analyze.html
        params = {'purpose': 'Upper Case', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyize the text
        #return render(request, 'analyze.html', params)

    # New line remover if else conditions
    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != '\n' and char !='\r':
                analyzed = analyzed + char
        # This is params arguments which will take assign values of variables in analyze.html
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyize the text
        # return render(request, 'analyze.html', params)

    # Extra Space Remover if else condition
    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):

            if not(djtext[index]==" " and djtext[index+1] ==" "):
                analyzed = analyzed + char
        # This is params arguments which will take assign values of variables in analyze.html
        params = {'purpose': 'Extra Line Remover', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyize the text
        #return render(request, 'analyze.html', params)

    # Character count conditions
    if (charcounter == "on"):
        analyzed = 0
        for i in djtext:
            analyzed = analyzed + 1
        # This is params arguments which will take assign values of variables in analyze.html
        params = {'purpose': 'Your Total Characters is : ', 'analyzed_text': analyzed}
        djtext = analyzed

    if (removepunc != 'on' and fullcps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcounter != "on"):
        return HttpResponse("Error")


    return render(request, 'analyze.html', params)
