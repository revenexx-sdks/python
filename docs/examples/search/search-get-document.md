```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.search import Search
from revenexx_revenexx.enums import Collection

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

search = Search(client)

result = search.search_get_document(
    collection = Collection.GREETINGS,
    document_id = ''
)
```
