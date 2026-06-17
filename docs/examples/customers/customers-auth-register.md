```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.customers import Customers
from revenexx_revenexx.models import AuthRegisterResponse

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

customers = Customers(client)

result: AuthRegisterResponse = customers.customers_auth_register(
    email = '',
    password = '',
    first_name = '', # optional
    last_name = '', # optional
    locale = '', # optional
    organization_id = '', # optional
    organization_name = '' # optional
)

print(result.model_dump())
```
