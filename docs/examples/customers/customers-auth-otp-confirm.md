```python
from revenexx.client import Client
from revenexx.services.customers import Customers
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

customers = Customers(client)

result: Error = customers.customers_auth_otp_confirm(
    secret = '',
    user_id = ''
)

print(result.model_dump())
```
