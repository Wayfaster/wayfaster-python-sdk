# Sessions
(*sessions*)

## Overview

### Available Operations

* [create_session](#create_session) - Create Session
* [create](#create) - Read Sessions
* [get](#get) - Read Session

## create_session

Create a new interview session.

Parameters:
- interview_config_id: str (required)
- first_name: str (required)
- last_name: str (required)
- email: str (optional)
- phone_number: str (optional, must be in format +1XXXXXXXXXX)

Returns:
- {
  'id': unique_session_id
}

### Example Usage

```python
import os
import wayfaster
from wayfaster import Wayfaster

s = Wayfaster(
    security=wayfaster.Security(
        username=os.getenv("WAYFASTER_USERNAME", ""),
        password=os.getenv("WAYFASTER_PASSWORD", ""),
    ),
)

res = s.sessions.create_session(request={
    "interview_config_id": "<id>",
    "first_name": "Kaylee",
    "last_name": "Wyman",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `request`                                                                     | [models.CreateSessionsRequestBody](../../models/createsessionsrequestbody.md) | :heavy_check_mark:                                                            | The request object to use for the request.                                    |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.CreateSessionsResponse](../../models/createsessionsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## create

Read Sessions

### Example Usage

```python
import os
import wayfaster
from wayfaster import Wayfaster

s = Wayfaster(
    security=wayfaster.Security(
        username=os.getenv("WAYFASTER_USERNAME", ""),
        password=os.getenv("WAYFASTER_PASSWORD", ""),
    ),
)

res = s.sessions.create(request={
    "interview_config_id": "<id>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.ReadSessionsRequestBody](../../models/readsessionsrequestbody.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get

Read Session

### Example Usage

```python
import os
import wayfaster
from wayfaster import Wayfaster

s = Wayfaster(
    security=wayfaster.Security(
        username=os.getenv("WAYFASTER_USERNAME", ""),
        password=os.getenv("WAYFASTER_PASSWORD", ""),
    ),
)

res = s.sessions.get(id="<id>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |