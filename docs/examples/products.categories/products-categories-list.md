```python
from revenexx.client import Client
from revenexx.services.products_categories import ProductsCategories
from revenexx.enums import RuleMatch

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

products_categories = ProductsCategories(client)

result = products_categories.products_categories_list(
    limit = 1, # optional
    offset = 1, # optional
    order = 'created_at.desc', # optional
    id = '', # optional
    code = 'cordless_drills', # optional
    parent_id = '', # optional
    path = 'tools/power_tools/cordless_drills', # optional
    position = 1, # optional
    labels = '{}', # optional
    values = '{}', # optional
    rules = '{}', # optional
    rule_match = RuleMatch.ALL, # optional
    rules_computed_at = '2026-01-01T12:00:00Z', # optional
    created_at = '2026-01-01T12:00:00Z', # optional
    updated_at = '2026-01-01T12:00:00Z' # optional
)
```
