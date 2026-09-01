```python
from revenexx.client import Client
from revenexx.services.storage import Storage
from revenexx.input_file import InputFile
from revenexx.enums import Visibility

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

storage = Storage(client)

result = storage.asset_store(
    file = InputFile.from_path('file.png'),
    alt_text = '', # optional
    description = '', # optional
    display_name = '', # optional
    folder_id = '', # optional
    keep_archive = True, # optional
    tags = [], # optional
    unpack = True, # optional
    visibility = Visibility.PUBLIC # optional
)
```
