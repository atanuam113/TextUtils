from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    dict = {'name':'atanu','place':'var me'}
    return render(request,'index.html',dict)

def analyze(request):
    dtext = request.POST.get('text','default')
    rtext = request.POST.get('removepunc','off')
    to_upper = request.POST.get('to_upper','off')
    newlineremove = request.POST.get('newlineremover','off')
    spaceremove = request.POST.get('spaceremover','off')
    charactercount = request.POST.get('charcount','off')
    
    if rtext == 'on':
        a_text = ''
        p_list = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for char in dtext:
            if char not in p_list:
                a_text = a_text + char
        dtext = a_text
    
    if to_upper == 'on':
        u_text =''
        for char in dtext:
            u_text = u_text + char.upper()
        dtext = u_text
    
    if newlineremove == 'on':
        n_text = ''
        for char in dtext:
            if char !='\n' and char !='\r':
                n_text = n_text + char
        dtext = n_text
    
    if spaceremove =='on':
        s_text = ''
        for char in dtext:
            if char !='  ':
                s_text = s_text + char
        dtext = s_text

    c_text = 0
    if charactercount =='on':
        for char in dtext:
            if char !=' ':
                c_text = c_text + 1
    if rtext == 'off' and to_upper == 'off' and newlineremove == 'off' and spaceremove =='off' and charactercount =='off':
        return HttpResponse("Please select any tool to analyze your text !")
    if c_text==0:
        ch_text='You do not on the switch for number of character calculation'
    else:
        ch_text = f"The number of character is:{c_text}"
    params = {'purpose':'Remove Punctuations','analyzed_text':dtext,'character_count':ch_text}
    return render(request,'analyze.html',params)