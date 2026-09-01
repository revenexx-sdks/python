```python
from revenexx.client import Client
from revenexx.services.io import Io
from revenexx.models import ValidationFailedResponse

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

io = Io(client)

result: ValidationFailedResponse = io.list_bulk_jobs(
    type = None, # optional
    status = None, # optional
    vendor = '', # optional
    app = '', # optional
    entity = '', # optional
    limit = 1 # optional
)

print(result.model_dump())
```
