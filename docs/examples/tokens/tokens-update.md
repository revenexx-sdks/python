```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.tokens import Tokens
from revenexx_revenexx.models import ResourceToken

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

tokens = Tokens(client)

result: ResourceToken = tokens.tokens_update(
    token_id = '',
    expire = '' # optional
)

print(result.model_dump())
```
