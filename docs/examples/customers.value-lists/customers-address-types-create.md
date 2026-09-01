```python
from revenexx.client import Client
from revenexx.services.customers_value_lists import CustomersValueLists
from revenexx.models import Error
from revenexx.enums import Tone

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

customers_value_lists = CustomersValueLists(client)

result: Error = customers_value_lists.customers_address_types_create(
    code = '',
    title = 'Shipping address',
    description = 'Where the goods go.', # optional
    descriptions = {
        "de": "Wohin die Ware geliefert wird.",
        "en": "Where the goods go."
    }, # optional
    is_default = True, # optional
    labels = {
        "de": "Lieferadresse",
        "en": "Shipping address"
    }, # optional
    position = 1, # optional
    tone = Tone.NEUTRAL # optional
)

print(result.model_dump())
```
