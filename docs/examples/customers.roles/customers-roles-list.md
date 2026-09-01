```python
from revenexx.client import Client
from revenexx.services.customers_roles import CustomersRoles
from revenexx.models import RoleCatalogResponse

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

customers_roles = CustomersRoles(client)

result: RoleCatalogResponse = customers_roles.customers_roles_list()

print(result.model_dump())
```
