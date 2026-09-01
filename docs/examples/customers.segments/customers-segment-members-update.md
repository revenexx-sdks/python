```python
from revenexx.client import Client
from revenexx.services.customers_segments import CustomersSegments
from revenexx.models import Error
from revenexx.enums import SegmentMemberSource

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

customers_segments = CustomersSegments(client)

result: Error = customers_segments.customers_segment_members_update(
    id = '',
    organization_id = '', # optional
    segment_id = '', # optional
    source = SegmentMemberSource.MANUAL # optional
)

print(result.model_dump())
```
