```python
from revenexx.client import Client
from revenexx.services.markets import Markets
from revenexx.models import MarketsVocabularyIndex

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

markets = Markets(client)

result: MarketsVocabularyIndex = markets.markets_vocabularies()

print(result.model_dump())
```
