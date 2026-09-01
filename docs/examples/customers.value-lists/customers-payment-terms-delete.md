```python
from revenexx.client import Client
from revenexx.services.customers_value_lists import CustomersValueLists
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

customers_value_lists = CustomersValueLists(client)

result: Error = customers_value_lists.customers_payment_terms_delete(
    id = ''
)

print(result.model_dump())
```
