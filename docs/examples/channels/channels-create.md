```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.channels import Channels
from revenexx_revenexx.models import Channel
from revenexx_revenexx.enums import ChannelStatus
from revenexx_revenexx.enums import ChannelType

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

channels = Channels(client)

result: Channel = channels.channels_create(
    code = '',
    name = '',
    is_default = None, # optional
    labels = {}, # optional
    position = None, # optional
    status = ChannelStatus.ACTIVE, # optional
    type = ChannelType.STOREFRONT # optional
)

print(result.model_dump())
```
