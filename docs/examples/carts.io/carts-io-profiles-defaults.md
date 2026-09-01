```python
from revenexx.client import Client
from revenexx.services.carts_io import CartsIo

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

carts_io = CartsIo(client)

result = carts_io.carts_io_profiles_defaults()
```
