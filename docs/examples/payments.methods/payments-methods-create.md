```python
from revenexx.client import Client
from revenexx.services.payments_methods import PaymentsMethods
from revenexx.models import Error
from revenexx.enums import PaymentFeeType
from revenexx.enums import PaymentMethodKind

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

payments_methods = PaymentsMethods(client)

result: Error = payments_methods.payments_methods_create(
    code = 'invoice',
    name = 'Invoice',
    countries = ["DE","AT"], # optional
    description = 'Pay within 14 days of the invoice date.', # optional
    enabled = True, # optional
    fee_amount = 2.5, # optional
    fee_currency = 'EUR', # optional
    fee_type = PaymentFeeType.NONE, # optional
    kind = PaymentMethodKind.SELF_MANAGED, # optional
    labels = {
        "de": "Rechnung",
        "en": "Invoice"
    }, # optional
    max_order_value = 2500, # optional
    metadata = {
        "erp_payment_key": "ZTRM01"
    }, # optional
    min_order_value = 10, # optional
    position = 0, # optional
    provider = 'stripe', # optional
    provider_method = 'card' # optional
)

print(result.model_dump())
```
