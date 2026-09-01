```python
from revenexx.client import Client
from revenexx.services.io import Io
from revenexx.models import ValidationFailedResponse

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

io = Io(client)

result: ValidationFailedResponse = io.list_io_entities()

print(result.model_dump())
```
