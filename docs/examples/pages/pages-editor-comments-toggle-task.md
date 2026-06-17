```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.pages import Pages
from revenexx_revenexx.models import Comment

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

pages = Pages(client)

result: Comment = pages.pages_editor_comments_toggle_task(
    page_id = '',
    uuid = '',
    task_index = None
)

print(result.model_dump())
```
