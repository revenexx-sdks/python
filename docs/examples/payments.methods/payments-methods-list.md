```python
from revenexx.client import Client
from revenexx.services.payments_methods import PaymentsMethods
from revenexx.enums import PaymentMethodKind

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

payments_methods = PaymentsMethods(client)

result = payments_methods.payments_methods_list(
    limit = 1, # optional
    offset = 1, # optional
    order = 'created_at.desc', # optional
    code = 'invoice', # optional
    kind = PaymentMethodKind.SELF_MANAGED, # optional
    enabled = True, # optional
    provider = 'stripe' # optional
)
```
