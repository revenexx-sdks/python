```python
from revenexx.client import Client
from revenexx.services.customers import Customers
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

customers = Customers(client)

result: Error = customers.customers_auth_register(
    email = 'einkauf@example.com',
    password = '',
    first_name = 'Anna', # optional
    last_name = 'Berger', # optional
    locale = 'de-DE', # optional
    organization_id = '', # optional
    organization_name = 'Beispiel Industrietechnik GmbH', # optional
    url = 'https://shop.example.com/account', # optional
    vat_id = 'DE123456789', # optional
    verification_url = 'https://shop.example.com/bestaetigen' # optional
)

print(result.model_dump())
```
