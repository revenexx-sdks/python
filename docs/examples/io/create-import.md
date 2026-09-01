```python
from revenexx.client import Client
from revenexx.services.io import Io
from revenexx.models import ValidationFailedResponse
from revenexx.enums import Format
from revenexx.enums import Mode
from revenexx.enums import CreateImportTarget

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

io = Io(client)

result: ValidationFailedResponse = io.create_import(
    app = '',
    entity = '',
    object_key = '',
    vendor = '',
    format = Format.CSV, # optional
    keys = [], # optional
    max_rejects = 1, # optional
    mode = Mode.UPSERT, # optional
    profile_id = '', # optional
    target = CreateImportTarget.LIVE # optional
)

print(result.model_dump())
```
