```python
from revenexx.client import Client
from revenexx.services.search import Search
from revenexx.models import Error
from revenexx.enums import Collection

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

search = Search(client)

result: Error = search.search_get_document(
    collection = Collection.PRODUCTS,
    document_id = ''
)

print(result.model_dump())
```
