```python
from revenexx.client import Client
from revenexx.services.carts import Carts
from revenexx.models import CartVocabularyIndex

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

carts = Carts(client)

result: CartVocabularyIndex = carts.carts_vocabularies_list()

print(result.model_dump())
```
