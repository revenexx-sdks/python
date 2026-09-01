```python
from revenexx.client import Client
from revenexx.services.orderlists import Orderlists
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

orderlists = Orderlists(client)

result: Error = orderlists.orderlists_items_create(
    list_id = '',
    name = 'Copy paper A4, 80 g/m², white',
    category_slug = 'office-supplies', # optional
    cost_center_id = 'CC-100', # optional
    custom_sku = 'CUST-4711', # optional
    image = 'https://cdn.example.com/catalog/acme-4711-blk.jpg', # optional
    metadata = {
        "erp_line_ref": "4711-01"
    }, # optional
    position = 0, # optional
    position_texts = ["Deliver to bay 3","Engraving: Team A"], # optional
    price = 3.49, # optional
    product_id = '', # optional
    quantity = 12, # optional
    sku = 'ACME-4711-BLK', # optional
    subcategory_slug = 'paper', # optional
    tax_rate = 19, # optional
    unit = 'piece' # optional
)

print(result.model_dump())
```
