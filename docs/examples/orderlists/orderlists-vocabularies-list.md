```python
from revenexx.client import Client
from revenexx.services.orderlists import Orderlists
from revenexx.models import OrderListVocabularyIndex

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

orderlists = Orderlists(client)

result: OrderListVocabularyIndex = orderlists.orderlists_vocabularies_list()

print(result.model_dump())
```
