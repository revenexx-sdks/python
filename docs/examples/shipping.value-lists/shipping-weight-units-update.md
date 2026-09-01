```python
from revenexx.client import Client
from revenexx.services.shipping_value_lists import ShippingValueLists
from revenexx.models import Error
from revenexx.enums import Tone

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

shipping_value_lists = ShippingValueLists(client)

result: Error = shipping_value_lists.shipping_weight_units_update(
    id = '',
    description = 'When to pick this weight unit.', # optional
    descriptions = {
        "de": "Wann diese Option zu w\u00e4hlen ist.",
        "en": "When to pick this weight unit."
    }, # optional
    factor = 1000, # optional
    is_default = True, # optional
    labels = {
        "de": "Tonne",
        "en": "Tonne"
    }, # optional
    position = 1, # optional
    title = 'Tonne', # optional
    tone = Tone.NEUTRAL # optional
)

print(result.model_dump())
```
