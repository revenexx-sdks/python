```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.payments import Payments
from revenexx_revenexx.models import Payment

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

payments = Payments(client)

result: Payment = payments.payments_get(
    id = ''
)

print(result.model_dump())
```
