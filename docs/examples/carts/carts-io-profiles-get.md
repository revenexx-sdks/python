```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.carts import Carts
from revenexx_revenexx.models import IoProfile

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

carts = Carts(client)

result: IoProfile = carts.carts_io_profiles_get(
    id = ''
)

print(result.model_dump())
```
