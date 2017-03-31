import braintree
from django import forms


class CreditCardForm(forms.Form):

    def clean(self):
        #payment_method_nonce = self.cleaned_data['payment_method_nonce']
        result = braintree.Transaction.sale({
            "amount": 1000,
            "payment_method_nonce": "fake-valid-nonce",
            "options": {
                "submit_for_settlement": False
            }
        })

        if result.is_success:
            # Don't charge the customer yet - instead get the transaction
            # id and use that later to complete the sale.
            self.cleaned_data['braintree_transaction_id'] = result.transaction.id
        else:
            errors = ", ".join([e.message for e in result.errors.deep_errors])
            print(errors)
            raise forms.ValidationError(errors)