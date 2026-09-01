```python
from revenexx.client import Client
from revenexx.services.carts_io import CartsIo
from revenexx.models import Error
from revenexx.enums import CartIoDirection
from revenexx.enums import CartIoEntity
from revenexx.enums import CartIoFormat
from revenexx.enums import CartIoApplyMode

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

carts_io = CartsIo(client)

result: Error = carts_io.carts_io_profiles_list(
    id = '', # optional
    name = 'cart-export-csv', # optional
    direction = CartIoDirection.IMPORT, # optional
    entity = CartIoEntity.CARTS, # optional
    format = CartIoFormat.JSON, # optional
    apply_mode = CartIoApplyMode.INSERT, # optional
    is_template = True, # optional
    created_at = '2026-01-01T12:00:00Z', # optional
    updated_at = '2026-01-01T12:00:00Z', # optional
    limit = 1, # optional
    offset = 1, # optional
    order = 'created_at.desc' # optional
)

print(result.model_dump())
```
