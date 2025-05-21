# Using the Silly Walk Grant Application API

This document provides examples of how to interact with the Silly Walk Grant Application API using curl.

## API Base URL

When running locally, the API is available at:

```
http://localhost:8000/api/v1
```

## API Key Authentication

All data-modifying endpoints (POST, PUT) require an API key to be provided in the `X-API-Key` header.

For testing purposes, use:

```
X-API-Key: SILLY_WALKS_2023_SECRET_KEY
```

## Submitting a New Application

```bash
curl -X POST http://localhost:8000/api/v1/applications \
  -H "Content-Type: application/json" \
  -H "X-API-Key: SILLY_WALKS_2023_SECRET_KEY" \
  -d '{
    "applicant_name": "John Cleese",
    "walk_name": "Ministry Shuffle",
    "description": "A walk involving high knee lifts, occasional hopping, and precisely timed briefcase movements.",
    "has_briefcase": true,
    "involves_hopping": true,
    "number_of_twirls": 5
  }'
```

This will return a response with the application ID, silliness score, and status:

```json
{
  "application_id": "123e4567-e89b-12d3-a456-426614174000",
  "silliness_score": 42,
  "status": "PendingReview"
}
```

## Retrieving an Application

```bash
curl -X GET http://localhost:8000/api/v1/applications/123e4567-e89b-12d3-a456-426614174000
```

This will return the full application details:

```json
{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "applicant_name": "John Cleese",
  "walk_name": "Ministry Shuffle",
  "description": "A walk involving high knee lifts, occasional hopping, and precisely timed briefcase movements.",
  "has_briefcase": true,
  "involves_hopping": true,
  "number_of_twirls": 5,
  "silliness_score": 42,
  "status": "PendingReview",
  "submission_timestamp": "2023-05-21T14:30:00Z"
}
```

## Listing All Applications

```bash
curl -X GET http://localhost:8000/api/v1/applications
```

You can use pagination parameters:

```bash
curl -X GET "http://localhost:8000/api/v1/applications?skip=10&limit=5"
```

This will return a list of applications:

```json
{
  "applications": [
    {
      "id": "123e4567-e89b-12d3-a456-426614174000",
      "applicant_name": "John Cleese",
      "walk_name": "Ministry Shuffle",
      "description": "A walk involving high knee lifts, occasional hopping, and precisely timed briefcase movements.",
      "has_briefcase": true,
      "involves_hopping": true,
      "number_of_twirls": 5,
      "silliness_score": 42,
      "status": "PendingReview",
      "submission_timestamp": "2023-05-21T14:30:00Z"
    },
    ...
  ],
  "total": 25
}
```

## Error Cases

### Invalid API Key

```bash
curl -X POST http://localhost:8000/api/v1/applications \
  -H "Content-Type: application/json" \
  -H "X-API-Key: WRONG_KEY" \
  -d '{...}'
```

Response (403 Forbidden):

```json
{
  "detail": "Invalid API key"
}
```

### Application Not Found

```bash
curl -X GET http://localhost:8000/api/v1/applications/nonexistent-id
```

Response (404 Not Found):

```json
{
  "detail": "Application with ID nonexistent-id not found"
}
```

### Invalid Application Data

```bash
curl -X POST http://localhost:8000/api/v1/applications \
  -H "Content-Type: application/json" \
  -H "X-API-Key: SILLY_WALKS_2023_SECRET_KEY" \
  -d '{
    "applicant_name": "",  # Empty name (invalid)
    "walk_name": "Test Walk"
    # Missing required fields
  }'
```

Response (422 Unprocessable Entity) with detailed validation errors.
