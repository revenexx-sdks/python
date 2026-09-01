```python
from revenexx.client import Client
from revenexx.services.orderlists import Orderlists
from revenexx.models import Error
from revenexx.models import OrderListItemInput

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

orderlists = Orderlists(client)

result: Error = orderlists.orderlists_create(
    name = 'Weekly office supplies',
    owner_id = '',
    owner_name = 'Jamie Rivera',
    items = [OrderListItemInput()], # optional
    kind = 'shopping', # optional
    metadata = {
        "department": "facility",
        "erp_reference": "REQ-2026-0042"
    }, # optional
    organization_id = '', # optional
    shared = True # optional
)

print(result.model_dump())
```
