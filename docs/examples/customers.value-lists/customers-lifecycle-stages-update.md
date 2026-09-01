```python
from revenexx.client import Client
from revenexx.services.customers_value_lists import CustomersValueLists
from revenexx.models import Error
from revenexx.enums import Tone

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

customers_value_lists = CustomersValueLists(client)

result: Error = customers_value_lists.customers_lifecycle_stages_update(
    id = '',
    description = 'Has ordered at least once and is being served.', # optional
    descriptions = {
        "de": "Hat mindestens einmal bestellt und wird betreut.",
        "en": "Has ordered at least once and is being served."
    }, # optional
    is_default = True, # optional
    labels = {
        "de": "Kunde",
        "en": "Customer"
    }, # optional
    position = 1, # optional
    title = 'Customer', # optional
    tone = Tone.NEUTRAL # optional
)

print(result.model_dump())
```
