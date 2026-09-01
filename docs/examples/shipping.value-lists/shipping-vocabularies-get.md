```python
from revenexx.client import Client
from revenexx.services.shipping_value_lists import ShippingValueLists
from revenexx.models import Error
from revenexx.enums import ShippingVocabulariesGetName

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

shipping_value_lists = ShippingValueLists(client)

result: Error = shipping_value_lists.shipping_vocabularies_get(
    name = ShippingVocabulariesGetName.CARRIER_STATUSES
)

print(result.model_dump())
```
