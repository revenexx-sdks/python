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

result: Error = channels.channels_update(
    id = '',
    code = 'shop', # optional
    is_default = True, # optional
    labels = {
        "de": "Shop",
        "en": "Shop"
    }, # optional
    name = 'Shop', # optional
    position = 1, # optional
    status = ChannelStatus.ACTIVE, # optional
    type = 'storefront', # optional
    unassigned_visibility = ChannelUnassignedVisibility.INHERIT # optional
)

print(result.model_dump())
```
