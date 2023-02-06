from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def List(r):
   ''' 
   :param r: 
   :return: 
   '''''' print(type(r))
    print(r.Get)
    return HttpResponse('Catagory List')
    '''
   context={}
   context['username']='Asd@yahoo.com'
   return render(r,'index.html',context)

def Add(req):
    return HttpResponse('Catagory Add')
def Update(req,catgid):
    print(req.method)
    print(req.GET)
    print(req.POST)
    return HttpResponse('Catagory Update'+str(catgid))