```python
from revenexx.client import Client
from revenexx.services.products_categories import ProductsCategories
from revenexx.models import Error
from revenexx.enums import ProductCategoriesSource

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

products_categories = ProductsCategories(client)

result: Error = products_categories.products_product_categories_create(
    category_id = '',
    product_id = '',
    position = 1, # optional
    source = ProductCategoriesSource.MANUAL # optional
)

print(result.model_dump())
```
