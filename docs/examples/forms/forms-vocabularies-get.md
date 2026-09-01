```python
from revenexx.client import Client
from revenexx.services.forms import Forms
from revenexx.models import Error
from revenexx.enums import FormsVocabulariesGetName

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

forms = Forms(client)

result: Error = forms.forms_vocabularies_get(
    name = FormsVocabulariesGetName.FORM_STATUSES
)

print(result.model_dump())
```
