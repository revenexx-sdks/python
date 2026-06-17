```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.payments import Payments
from revenexx_revenexx.models import PaymentMethod
from revenexx_revenexx.enums import PaymentFeeType
from revenexx_revenexx.enums import PaymentMethodKind

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

payments = Payments(client)

result: PaymentMethod = payments.payments_methods_create(
    code = '',
    name = '',
    countries = [], # optional
    description = '', # optional
    enabled = None, # optional
    fee_amount = None, # optional
    fee_currency = '', # optional
    fee_type = PaymentFeeType.NONE, # optional
    kind = PaymentMethodKind.SELF_MANAGED, # optional
    labels = {}, # optional
    max_order_value = None, # optional
    metadata = {}, # optional
    min_order_value = None, # optional
    position = None, # optional
    provider = '', # optional
    provider_method = '' # optional
)

print(result.model_dump())
```
