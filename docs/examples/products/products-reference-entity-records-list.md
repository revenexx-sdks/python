```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.products import Products

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

products = Products(client)

result = products.products_reference_entity_records_list()
```
