<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import os
import wayfaster
from wayfaster import Wayfaster

s = Wayfaster(
    security=wayfaster.Security(
        username=os.getenv("WAYFASTER_USERNAME", ""),
        password=os.getenv("WAYFASTER_PASSWORD", ""),
    ),
)

res = s.interview_configs.list()

if res is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import os
import wayfaster
from wayfaster import Wayfaster

async def main():
    s = Wayfaster(
        security=wayfaster.Security(
            username=os.getenv("WAYFASTER_USERNAME", ""),
            password=os.getenv("WAYFASTER_PASSWORD", ""),
        ),
    )
    res = await s.interview_configs.list_async()
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->