```python
from revenexx.client import Client
from revenexx.services.shipping_value_lists import ShippingValueLists
from revenexx.models import Error
from revenexx.enums import Tone

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

shipping_value_lists = ShippingValueLists(client)

result: Error = shipping_value_lists.shipping_service_levels_create(
    code = 'night_courier',
    title = 'Night courier',
    description = 'When to pick this service level.', # optional
    descriptions = {
        "de": "Wann diese Option zu w\u00e4hlen ist.",
        "en": "When to pick this service level."
    }, # optional
    is_default = True, # optional
    labels = {
        "de": "Night courier",
        "en": "Night courier"
    }, # optional
    position = 1, # optional
    tone = Tone.NEUTRAL # optional
)

print(result.model_dump())
```
