```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.search import Search
from revenexx_revenexx.enums import Collection

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

search = Search(client)

result = search.search_search_documents(
    collection = Collection.GREETINGS,
    facet_by = '', # optional
    filter_by = '', # optional
    page = None, # optional
    per_page = None, # optional
    q = '', # optional
    query_by = '', # optional
    sort_by = '' # optional
)
```
