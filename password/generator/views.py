from django.shortcuts import render
import random
def home(request):
    return render( request,'generator/home.html')

def password(request):
    character = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('Uppercase'):
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        character.extend(list('0123456789'))
    if request.GET.get('special'):
        character.extend(list('!@#$%^&*()'))
    length = int(request.GET.get('length',8))
    thepass=''
    for i in range(length):
        thepass+=random.choice(character)
    return render(request,'generator/password.html',{'password':thepass})
    
    
    


