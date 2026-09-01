```python
from revenexx.client import Client
from revenexx.services.channels import Channels
from revenexx.models import ChannelContext

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

channels = Channels(client)

result: ChannelContext = channels.channels_context(
    channel = 'shop' # optional
)

print(result.model_dump())
```
