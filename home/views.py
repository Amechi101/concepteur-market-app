from django.shortcuts import render_to_response
from django.template import RequestContext


# Create your views here.
 
def base(request):
    return render_to_response('home/base.html', context_instance=RequestContext(request))
