```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.orders import Orders
from revenexx_revenexx.models import NumberRange

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

orders = Orders(client)

result: NumberRange = orders.orders_number_ranges_create(
    code = '',
    channel_id = '', # optional
    counter = None, # optional
    metadata = {}, # optional
    padding = None, # optional
    position_step = None, # optional
    prefix = '', # optional
    step = None, # optional
    suffix = '' # optional
)

print(result.model_dump())
```
