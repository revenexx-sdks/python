```python
from revenexx.client import Client
from revenexx.services.health import Health

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

health = Health(client)

result = health.health_ready()
```
