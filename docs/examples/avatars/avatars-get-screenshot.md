```python
from revenexx.client import Client
from revenexx.services.avatars import Avatars
from revenexx.enums import Theme
from revenexx.enums import Timezone
from revenexx.enums import Permissions
from revenexx.enums import Output

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

avatars = Avatars(client)

result = avatars.avatars_get_screenshot(
    url = 'https://example.com',
    headers = {}, # optional
    viewport_width = 1, # optional
    viewport_height = 1, # optional
    scale = 1, # optional
    theme = Theme.LIGHT, # optional
    user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15', # optional
    fullpage = True, # optional
    locale = 'en-US', # optional
    timezone = Timezone.AFRICA_ABIDJAN, # optional
    latitude = 9.99, # optional
    longitude = 9.99, # optional
    accuracy = 9.99, # optional
    touch = True, # optional
    permissions = [Permissions.GEOLOCATION], # optional
    sleep = 1, # optional
    width = 1, # optional
    height = 1, # optional
    quality = 1, # optional
    output = Output.JPG # optional
)
```
