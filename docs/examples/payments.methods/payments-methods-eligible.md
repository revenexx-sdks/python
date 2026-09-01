```python
from revenexx.client import Client
from revenexx.services.payments_methods import PaymentsMethods

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

payments_methods = PaymentsMethods(client)

result = payments_methods.payments_methods_eligible(
    amount = 49.9, # optional
    country = 'DE', # optional
    currency = 'EUR' # optional
)
```
