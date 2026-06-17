```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.locale import Locale
from revenexx_revenexx.models import PhoneList

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

locale = Locale(client)

result: PhoneList = locale.locale_list_countries_phones()

print(result.model_dump())
```
