```python
from revenexx.client import Client
from revenexx.services.products_categories import ProductsCategories
from revenexx.models import Error
from revenexx.models import CategoryRuleCondition
from revenexx.enums import CategoryRuleMatch

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

products_categories = ProductsCategories(client)

result: Error = products_categories.products_categories_rules_preview(
    category_id = '',
    conditions = [CategoryRuleCondition()],
    rule_match = CategoryRuleMatch.ALL # optional
)

print(result.model_dump())
```
