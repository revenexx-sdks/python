```python
from revenexx.client import Client
from revenexx.services.products_data_model import ProductsDataModel
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

products_data_model = ProductsDataModel(client)

result: Error = products_data_model.products_measurement_families_update(
    id = '',
    code = 'weight', # optional
    labels = {
        "de": "Gewicht",
        "en": "Weight"
    }, # optional
    standard_unit = 'kilogram', # optional
    units = [
        {
            "code": "kilogram",
            "convert_factor": 1,
            "symbol": "kg"
        },
        {
            "code": "gram",
            "convert_factor": 0.001,
            "symbol": "g"
        }
    ] # optional
)

print(result.model_dump())
```
