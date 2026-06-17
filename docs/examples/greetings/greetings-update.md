```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.greetings import Greetings
from revenexx_revenexx.models import Greeting

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

greetings = Greetings(client)

result: Greeting = greetings.greetings_update(
    id = '',
    locale = '', # optional
    message = '', # optional
    metadata = {}, # optional
    name = '' # optional
)

print(result.model_dump())
```
