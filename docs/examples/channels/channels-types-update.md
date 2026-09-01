```python
from revenexx.client import Client
from revenexx.services.channels import Channels
from revenexx.models import Error
from revenexx.enums import ChannelTypeTone

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

channels = Channels(client)

result: Error = channels.channels_types_update(
    id = '',
    description = 'A web shop a human browses.', # optional
    descriptions = {
        "de": "Shop",
        "en": "Shop"
    }, # optional
    is_default = True, # optional
    labels = {
        "de": "Shop",
        "en": "Shop"
    }, # optional
    position = 1, # optional
    title = 'Product feed', # optional
    tone = ChannelTypeTone.NEUTRAL # optional
)

print(result.model_dump())
```
