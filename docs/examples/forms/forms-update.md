```python
from revenexx.client import Client
from revenexx.services.forms import Forms
from revenexx.models import Error
from revenexx.enums import FormStatus

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

forms = Forms(client)

result: Error = forms.forms_update(
    id = '',
    definition = [{"$formkit":"text","label":"Company","name":"company","validation":"required"},{"$formkit":"email","label":"Email","name":"email","validation":"required|email"},{"$formkit":"textarea","label":"What do you need a price for?","name":"message","rows":4},{"$el":"p","children":"We answer price requests within one working day."}], # optional
    metadata = {}, # optional
    name = 'Price request', # optional
    settings = {}, # optional
    slug = 'price-request', # optional
    status = FormStatus.DRAFT # optional
)

print(result.model_dump())
```
