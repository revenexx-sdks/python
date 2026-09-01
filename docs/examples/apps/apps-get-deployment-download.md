```python
from revenexx.client import Client
from revenexx.services.apps import Apps
from revenexx.enums import AppsGetDeploymentDownloadType

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

apps = Apps(client)

result = apps.apps_get_deployment_download(
    function_id = '',
    deployment_id = '',
    type = AppsGetDeploymentDownloadType.SOURCE # optional
)
```
