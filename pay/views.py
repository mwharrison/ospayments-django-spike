import braintree

from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect

from .forms import CreditCardForm

braintree.Configuration.configure(braintree.Environment.Sandbox,
                                  merchant_id=settings.BRAINTREE_MERCHANT_ID,
                                  public_key=settings.BRAINTREE_PUBLIC_KEY,
                                  private_key=settings.BRAINTREE_PRIVATE_KEY)

def payment_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreditCardForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        request.session['braintree_client_token'] = braintree.ClientToken.generate()
        form = CreditCardForm()

    return render(request, 'payment_template.html', {'form': form})

def thanks_view(request):
    return render(request, 'thanks.html', {})