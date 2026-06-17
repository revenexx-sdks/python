```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.avatars import Avatars
from revenexx_revenexx.enums import Theme
from revenexx_revenexx.enums import Timezone
from revenexx_revenexx.enums import Permissions
from revenexx_revenexx.enums import Output

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

avatars = Avatars(client)

result = avatars.avatars_get_screenshot(
    url = '',
    headers = {}, # optional
    viewport_width = None, # optional
    viewport_height = None, # optional
    scale = None, # optional
    theme = Theme.LIGHT, # optional
    user_agent = '', # optional
    fullpage = None, # optional
    locale = '', # optional
    timezone = Timezone.AFRICA_ABIDJAN, # optional
    latitude = None, # optional
    longitude = None, # optional
    accuracy = None, # optional
    touch = None, # optional
    permissions = [Permissions.GEOLOCATION], # optional
    sleep = None, # optional
    width = None, # optional
    height = None, # optional
    quality = None, # optional
    output = Output.JPG # optional
)
```
