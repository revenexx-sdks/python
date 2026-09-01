```python
from revenexx.client import Client
from revenexx.services.payments_ledger import PaymentsLedger
from revenexx.models import Error
from revenexx.enums import PaymentsVocabulariesGetName

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

payments_ledger = PaymentsLedger(client)

result: Error = payments_ledger.payments_vocabularies_get(
    name = PaymentsVocabulariesGetName.DUNNING_STAGES
)

print(result.model_dump())
```
