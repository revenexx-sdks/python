```python
from revenexx.client import Client
from revenexx.services.customers_value_lists import CustomersValueLists
from revenexx.models import Error
from revenexx.enums import Tone

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

customers_value_lists = CustomersValueLists(client)

result: Error = customers_value_lists.customers_payment_terms_create(
    code = '',
    title = 'Net 30 days',
    description = 'Invoice due 30 days after the delivery note.', # optional
    descriptions = {
        "de": "Rechnung 30 Tage nach Lieferschein f\u00e4llig.",
        "en": "Invoice due 30 days after the delivery note."
    }, # optional
    is_default = True, # optional
    labels = {
        "de": "Zahlbar in 30 Tagen",
        "en": "Net 30 days"
    }, # optional
    position = 1, # optional
    tone = Tone.NEUTRAL # optional
)

print(result.model_dump())
```
