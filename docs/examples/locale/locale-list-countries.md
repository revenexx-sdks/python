```python
from revenexx.client import Client
from revenexx.services.locale import Locale
from revenexx.models import CountryList

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

locale = Locale(client)

result: CountryList = locale.locale_list_countries()

print(result.model_dump())
```
