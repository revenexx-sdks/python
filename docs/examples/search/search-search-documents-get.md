```python
from revenexx.client import Client
from revenexx.services.search import Search
from revenexx.models import Error
from revenexx.enums import Collection

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

search = Search(client)

result: Error = search.search_search_documents_get(
    collection = Collection.PRODUCTS,
    q = '', # optional
    query_by = '', # optional
    filter_by = '', # optional
    sort_by = '', # optional
    facet_by = '', # optional
    max_facet_values = 1, # optional
    group_by = '', # optional
    include_fields = '', # optional
    exclude_fields = '', # optional
    highlight_full_fields = '', # optional
    num_typos = 1, # optional
    prefix = '', # optional
    page = 1, # optional
    per_page = 1 # optional
)

print(result.model_dump())
```
