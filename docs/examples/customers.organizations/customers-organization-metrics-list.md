```python
from revenexx.client import Client
from revenexx.services.customers_organizations import CustomersOrganizations

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

customers_organizations = CustomersOrganizations(client)

result = customers_organizations.customers_organization_metrics_list(
    id = '', # optional
    organization_id = '', # optional
    order_count = 1, # optional
    order_count_30d = 1, # optional
    order_count_90d = 1, # optional
    order_count_365d = 1, # optional
    revenue_total = 9.99, # optional
    revenue_30d = 9.99, # optional
    revenue_90d = 9.99, # optional
    revenue_365d = 9.99, # optional
    avg_order_value = 9.99, # optional
    avg_order_value_365d = 9.99, # optional
    first_order_at = '2026-01-01T12:00:00Z', # optional
    last_order_at = '2026-01-01T12:00:00Z', # optional
    currency = 'EUR', # optional
    currency_mixed = True, # optional
    orders_as_of = '2026-01-01T12:00:00Z', # optional
    computed_at = '2026-01-01T12:00:00Z', # optional
    created_at = '2026-01-01T12:00:00Z', # optional
    updated_at = '2026-01-01T12:00:00Z', # optional
    limit = 1, # optional
    offset = 1, # optional
    order = 'created_at.desc' # optional
)
```
