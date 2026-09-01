```python
from revenexx.client import Client
from revenexx.services.io import Io
from revenexx.models import ValidationFailedResponse
from revenexx.enums import Direction
from revenexx.enums import ApplyMode

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

io = Io(client)

result: ValidationFailedResponse = io.create_profile(
    app = '',
    direction = Direction.IMPORT,
    entity = '',
    format = '',
    name = '',
    vendor = '',
    apply_mode = ApplyMode.UPSERT, # optional
    mapping = {}, # optional
    markets = [], # optional
    options = {} # optional
)

print(result.model_dump())
```
