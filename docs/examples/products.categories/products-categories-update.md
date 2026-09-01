```python
from revenexx.client import Client
from revenexx.services.products_categories import ProductsCategories
from revenexx.models import Error
from revenexx.enums import CategoriesRuleMatch

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

products_categories = ProductsCategories(client)

result: Error = products_categories.products_categories_update(
    id = '',
    code = 'cordless_drills', # optional
    labels = {
        "de": "Akku-Bohrschrauber",
        "en": "Cordless drills"
    }, # optional
    parent_id = '', # optional
    path = 'tools/power_tools/cordless_drills', # optional
    position = 1, # optional
    rule_match = CategoriesRuleMatch.ALL, # optional
    rules = {
        "conditions": [
            {
                "field": "attribute:brand",
                "operator": "in",
                "value": [
                    "acme",
                    "globex"
                ]
            },
            {
                "field": "enabled",
                "operator": "eq",
                "value": True
            }
        ]
    }, # optional
    rules_computed_at = '2026-01-01T12:00:00Z', # optional
    values = {
        "hero_asset": "packshots\/cordless_drills_hero",
        "seo_title": "Cordless drills"
    } # optional
)

print(result.model_dump())
```
