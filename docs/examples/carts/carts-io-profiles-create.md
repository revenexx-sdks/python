```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.carts import Carts
from revenexx_revenexx.models import IoProfile
from revenexx_revenexx.enums import CartIoDirection
from revenexx_revenexx.enums import CartIoApplyMode
from revenexx_revenexx.enums import CartIoEntity
from revenexx_revenexx.enums import CartIoFormat

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

carts = Carts(client)

result: IoProfile = carts.carts_io_profiles_create(
    direction = CartIoDirection.IMPORT,
    name = '',
    apply_mode = CartIoApplyMode.INSERT, # optional
    entity = CartIoEntity.CARTS, # optional
    format = CartIoFormat.JSON, # optional
    is_template = None, # optional
    mapping = {}, # optional
    options = {} # optional
)

print(result.model_dump())
```
