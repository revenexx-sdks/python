```python
from revenexx.client import Client
from revenexx.services.avatars import Avatars
from revenexx.enums import AvatarsGetFlagCode

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

avatars = Avatars(client)

result = avatars.avatars_get_flag(
    code = AvatarsGetFlagCode.AF,
    width = 1, # optional
    height = 1, # optional
    quality = 1 # optional
)
```
