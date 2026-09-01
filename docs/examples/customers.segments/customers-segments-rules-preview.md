```python
from revenexx.client import Client
from revenexx.services.customers_segments import CustomersSegments
from revenexx.models import Error
from revenexx.models import SegmentRuleCondition
from revenexx.enums import RuleMatch
from revenexx.enums import Target

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

customers_segments = CustomersSegments(client)

result: Error = customers_segments.customers_segments_rules_preview(
    segment_id = '',
    conditions = [SegmentRuleCondition()],
    rule_match = RuleMatch.ALL, # optional
    target = Target.ORGANIZATIONS # optional
)

print(result.model_dump())
```
