```python
from revenexx.client import Client
from revenexx.services.channels import Channels
from revenexx.models import Error
from revenexx.models import ChannelVisibilityItem

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

channels = Channels(client)

result: Error = channels.channels_visibility(
    items = [ChannelVisibilityItem()],
    channel = 'shop', # optional
    channel_body = 'shop' # optional
)

print(result.model_dump())
```
