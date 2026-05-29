## API Documentation

### Authentication

#### Get JWT Token

POST `/api/token/`
Request:

```json
{
  "username": "admin",
  "password": "password"
}
```

Response:

```json
{
  "refresh": "jwt_refresh_token",
  "access": "jwt_access_token"
}
```

### Customer Requests

#### List Requests

GET `/api/requests/`

Authentication Required.

#### Create Request

POST `/api/requests/`
Request:

```json
{
  "customer_name": "John",
  "customer_email": "john@example.com",
  "message": "Need refund"
}
```

#### Get Request Detail

GET `/api/requests/<id>/`

#### Update Request Status

PATCH `/api/requests/<id>/`
Request:

```json
{
  "status": "resolved"
}
```
