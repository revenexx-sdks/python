```python
from revenexx.client import Client
from revenexx.services.channels import Channels
from revenexx.models import Error
from revenexx.enums import ChannelStatus
from revenexx.enums import ChannelUnassignedVisibility

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

channels = Channels(client)

result: Error = channels.channels_list(
    id = '', # optional
    code = 'shop', # optional
    name = 'Shop', # optional
    labels = '{"en":"Shop","de":"Shop"}', # optional
    type = 'storefront', # optional
    status = ChannelStatus.ACTIVE, # optional
    unassigned_visibility = ChannelUnassignedVisibility.INHERIT, # optional
    is_default = True, # optional
    position = 1, # optional
    created_at = '2026-01-01T12:00:00Z', # optional
    updated_at = '2026-01-01T12:00:00Z', # optional
    limit = 1, # optional
    offset = 1, # optional
    order = 'created_at.desc' # optional
)

print(result.model_dump())
```
