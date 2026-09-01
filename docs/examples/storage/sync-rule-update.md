```python
from revenexx.client import Client
from revenexx.services.storage import Storage

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

storage = Storage(client)

result = storage.sync_rule_update(
    id = '',
    enabled = True, # optional
    options = [], # optional
    schedule = '0 3 * * *', # optional
    sftp_account_id = '', # optional
    source_path = '/uploads', # optional
    target_folder_id = '' # optional
)
```
