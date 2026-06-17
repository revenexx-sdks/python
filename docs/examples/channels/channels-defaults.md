```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.channels import Channels
from revenexx_revenexx.models import ChannelDefaults

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

channels = Channels(client)

result: ChannelDefaults = channels.channels_defaults()

print(result.model_dump())
```
