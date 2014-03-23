from django.shortcuts import render_to_response
from django.template import RequestContext
from profiles.models import User



# Create your views here.
 
def base(request):
	template_var = {}
	if request.user.is_authenticated():
		username=request.user.username 
		password=request.user.password
		email = request.user.email
		
		template_var["is_authenticated"]= True
	return render_to_response('home/base.html',template_var, context_instance=RequestContext(request))
