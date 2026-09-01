```python
from revenexx.client import Client
from revenexx.services.carts_io import CartsIo
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

carts_io = CartsIo(client)

result: Error = carts_io.carts_import(
    contact_id = '', # optional
    csv = 'sku,name,quantity,unit_price
BOLT-M8-30,Hex bolt M8,100,0.12
NUT-M8,Hex nut M8,100,0.04
', # optional
    name = 'Weekly order', # optional
    payload = {
        "cart": {
            "currency": "EUR",
            "name": "Weekly order"
        },
        "items": [
            {
                "name": "Hex bolt M8",
                "quantity": 100,
                "sku": "BOLT-M8-30",
                "unit_price": 0.12
            }
        ]
    }, # optional
    profile_id = '', # optional
    session_key = 'a1b2c3d4e5f6', # optional
    target_cart_id = '' # optional
)

print(result.model_dump())
```
