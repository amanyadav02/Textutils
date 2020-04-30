from django.shortcuts import render
from django.http import HttpResponse
from collections import Counter

def index(request):
    return render(request, 'index.html')


def analize(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcounter=request.POST.get('charcounter','off')
    c=""
    d = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    e=0
    if(removepunc=="on"):
        c=""
        for i in djtext:
            if i not in d:
                c+=i
        params = {'purpose': 'remove punctuation', 'rashi': c}
        djtext=c
        e+1
        #return render(request,'analyze.html',params)
    if(fullcaps=='on'):
        c=""
        for i in djtext:
            if(i not in d):
                c+=i.upper()
        params = {'purpose': 'capatilized', 'rashi': c}
        djtext=c
        e+=1
        #return render(request, 'analyze.html', params)
    if(newlineremover=='on'):
        c=""
        for i in djtext:
            if( i!="\n") and i!="\r":
                c+=i
        params = {'purpose': 'newline remover', 'rashi': c}
        djtext=c
        e+=1
        #return render(request, 'analyze.html', params)
    if (spaceremover == 'on'):
        c =""
        for i in djtext:
            c+=i
        a=c.strip()
        params = {'purpose': 'newline remover', 'rashi': a}
        djtext=c
        e+=1
        #return render(request, 'analyze.html', params)
    if (charcounter == 'on'):
        c=""
        for i in djtext:
            c+=i
        a=Counter(c)
        params = {'purpose': 'count', 'rashi': a}
        djtext=c
        e+=1
        #return render(request, 'analyze.html', params)
    if(e==0):
        return HttpResponse("chutiya ho ka be")
    else:
        return render(request, 'analyze.html', params)
def e(request):
    s='''<h2>navigation bar<br></h2>
    <h1>aman <br></h1>
    <h2>yadav<br></h2>'''
    return HttpResponse(s)



