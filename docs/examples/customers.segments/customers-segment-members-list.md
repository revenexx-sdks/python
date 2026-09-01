```python
from revenexx.client import Client
from revenexx.services.customers_segments import CustomersSegments
from revenexx.enums import Source

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

customers_segments = CustomersSegments(client)

result = customers_segments.customers_segment_members_list(
    id = '', # optional
    segment_id = '', # optional
    organization_id = '', # optional
    source = Source.MANUAL, # optional
    created_at = '2026-01-01T12:00:00Z', # optional
    limit = 1, # optional
    offset = 1, # optional
    order = 'created_at.desc' # optional
)
```
