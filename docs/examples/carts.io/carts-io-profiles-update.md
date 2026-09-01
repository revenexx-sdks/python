```python
from revenexx.client import Client
from revenexx.services.carts_io import CartsIo
from revenexx.models import Error
from revenexx.enums import CartIoApplyMode
from revenexx.enums import CartIoDirection
from revenexx.enums import CartIoEntity
from revenexx.enums import CartIoFormat

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

carts_io = CartsIo(client)

result: Error = carts_io.carts_io_profiles_update(
    id = '',
    apply_mode = CartIoApplyMode.INSERT, # optional
    direction = CartIoDirection.IMPORT, # optional
    entity = CartIoEntity.CARTS, # optional
    format = CartIoFormat.JSON, # optional
    is_template = True, # optional
    mapping = {}, # optional
    name = 'cart-export-csv', # optional
    options = {} # optional
)

print(result.model_dump())
```
