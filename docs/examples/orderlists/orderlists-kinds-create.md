```python
from revenexx.client import Client
from revenexx.services.orderlists import Orderlists
from revenexx.models import Error
from revenexx.enums import OrderListKindTone

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

orderlists = Orderlists(client)

result: Error = orderlists.orderlists_kinds_create(
    code = 'reagents',
    title = 'Reagent list',
    description = 'Chemicals ordered against a standing lab protocol.', # optional
    descriptions = {
        "de": "Chemikalien, die nach einem festen Laborprotokoll bestellt werden.",
        "en": "Chemicals ordered against a standing lab protocol."
    }, # optional
    is_default = True, # optional
    labels = {
        "de": "Reagenzienliste",
        "en": "Reagent list"
    }, # optional
    position = 2, # optional
    tone = OrderListKindTone.NEUTRAL # optional
)

print(result.model_dump())
```
