```python
from revenexx.client import Client
from revenexx.services.customers_organizations import CustomersOrganizations
from revenexx.models import OrganizationMetricsFreshness

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

customers_organizations = CustomersOrganizations(client)

result: OrganizationMetricsFreshness = customers_organizations.customers_organization_metrics_freshness()

print(result.model_dump())
```
