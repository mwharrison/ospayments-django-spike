# ospayments-django-spike
OpenStax Payments - Django based technical spike

To get started:

`git clone https://github.com/mwharrison/ospayments-django-spike && cd ospayments-django-spike`

`pip install -rU requirements.txt` (preferably from within your virtualenv)

`python manage.py migrate`

`python manage.py createsuperuser`

`python manage.py runserver`



You will also need some braintree credientials to get this running. You'll need to register for a sandbox account at https://www.braintreepayments.com/sandbox.

Then rename `payments/settings/local.py.example` -> `payments/settings/local.py` and fill in the required keys.
