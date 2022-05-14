from modulefinder import Module
from django.http import HttpResponse



def hello(request):
    return HttpResponse("""
   <h1> Welcome To My World <h1/>
  <h2> sir Aun <h2/>
    """)
    
    
    
