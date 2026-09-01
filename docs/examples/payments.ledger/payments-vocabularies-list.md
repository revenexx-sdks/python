```python
from revenexx.client import Client
from revenexx.services.payments_ledger import PaymentsLedger

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

payments_ledger = PaymentsLedger(client)

result = payments_ledger.payments_vocabularies_list()
```
