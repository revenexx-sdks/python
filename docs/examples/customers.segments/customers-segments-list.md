```python
from revenexx.client import Client
from revenexx.services.customers_segments import CustomersSegments
from revenexx.enums import RuleMatch

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

customers_segments = CustomersSegments(client)

result = customers_segments.customers_segments_list(
    id = '', # optional
    code = 'key_accounts', # optional
    position = 1, # optional
    rule_match = RuleMatch.ALL, # optional
    rules_computed_at = '2026-01-01T12:00:00Z', # optional
    created_at = '2026-01-01T12:00:00Z', # optional
    updated_at = '2026-01-01T12:00:00Z', # optional
    limit = 1, # optional
    offset = 1, # optional
    order = 'created_at.desc' # optional
)
```
