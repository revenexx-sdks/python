```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.customers import Customers
from revenexx_revenexx.models import AuthLoginResponse

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

customers = Customers(client)

result: AuthLoginResponse = customers.customers_auth_login(
    email = '',
    password = ''
)

print(result.model_dump())
```
