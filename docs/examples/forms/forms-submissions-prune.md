```python
from revenexx.client import Client
from revenexx.services.forms import Forms
from revenexx.models import Error
from revenexx.enums import FormsSubmissionsPruneStatus

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

forms = Forms(client)

result: Error = forms.forms_submissions_prune(
    dry_run = True, # optional
    form_slug = 'contact', # optional
    older_than_days = 1, # optional
    status = FormsSubmissionsPruneStatus.NEW # optional
)

print(result.model_dump())
```
