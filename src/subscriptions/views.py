from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import SubscriptionForm

def subscribe(request):
    form = SubscriptionForm()
    context = RequestContext(request, {'form': form})
    return render_to_response('subscriptions/new.html', context)
