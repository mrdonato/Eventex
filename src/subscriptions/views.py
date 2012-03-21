from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.conf import settings
from models import Subscription
from forms import SubscriptionForm

def subscribe(request, template_name='subscriptions/new.html'):
    form = SubscriptionForm(request.POST or None)
    if form.is_valid():
        subscription = form.save()
        send_mail(subject=u'Cadastrado com sucesso',
                  message=u'Obrigado pela sua inscricao',
                  from_email=settings.DEFAULT_FROM_EMAIL,
                  recipient_list=[subscription.email]
        )
        return HttpResponseRedirect(
        reverse('subscriptions:success', args=[ subscription.pk ]))
 
    
    return render(request, template_name, {'form':form})

def success(request, id, template_name='subscriptions/success.html'):
    subscription = get_object_or_404(Subscription, pk=id)
    return render(request, template_name, {'subscription':subscription})

