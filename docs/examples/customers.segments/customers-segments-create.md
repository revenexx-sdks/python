```python
from revenexx.client import Client
from revenexx.services.customers_segments import CustomersSegments
from revenexx.models import Error
from revenexx.enums import SegmentRuleMatch

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

customers_segments = CustomersSegments(client)

result: Error = customers_segments.customers_segments_create(
    code = 'key_accounts',
    labels = {
        "de": "Gro\u00dfkunden",
        "en": "Key accounts"
    }, # optional
    position = 1, # optional
    rule_match = SegmentRuleMatch.ALL, # optional
    rules = {} # optional
)

print(result.model_dump())
```
