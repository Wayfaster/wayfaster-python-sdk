# InterviewConfigs
(*interview_configs*)

## Overview

### Available Operations

* [list](#list) - Read Interview Configs
* [get](#get) - Read Interview Config

## list

Read Interview Configs

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

res = s.interview_configs.list()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get

Read Interview Config

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

res = s.interview_configs.get(id="<id>")

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