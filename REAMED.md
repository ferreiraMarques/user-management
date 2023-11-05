# Users Managment

Users Managment Test

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`JWT_PRIVATE_KEY`: jwt secret for the firm

`DATABASE_PORT`: port of the database

`POSTGRES_PASSWORD`: password of the database

`POSTGRES_USER`: user of the database

`POSTGRES_DB`: db assigned in the database

`POSTGRES_HOSTNAME`: host of the database

`ACCESS_TOKEN_EXPIRES_IN`: time expires access token

`JWT_ALGORITHM`: jwt cypher algorithm

`CLIENT_ORIGIN`: origins allow


## Installation

Install user-management with pip

```bash
  cd users-management
  pip install
  uvicorn app.main:app --host localhost --port 8000
```
    
## API Reference

#### Login
Description: this endpoint is used to authenticate with the system via phone and password, it will return the access token and username.


```http
  POST {{baseUrl}}/api/v1/users/login
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `phone` | `string` | **Required**. phone user |
| `password ` | `string` | **Required**. password user|


### Users


#### Create User
Description: this end point is used to create a new user.


```http
  POST {{baseUrl}}/api/v1/users/
```


| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Required**. name user |
| `email`      | `string` | **Required**. email Authorization |
| `address`      | `string` | **Required**. address Authorization |
| `phone`      | `string` | **Required**. phone user |
| `password`      | `string` | **Required**. user password |

Headers

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Authorization`      | `string` | **Required**. Access Token |

#### Get Users
Description: this endpoint is used to obtain all registered users.


```http
  GET {{baseUrl}}/api/v1/users?limit=2&page=1
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `limit`      | `int` | **optional**. limit registers retrieve |
| `page`      | `int` | **optional**. page view |
| `search`      | `string` | **optional**. search keyword |

Headers

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Authorization`      | `string` | **Required**. Access Token |


#### Get User
Description: this endpoint is used to obtain a single user if it is registered.


```http
  GET {{baseUrl}}/api/v1/users/{{userId}}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `userId` | `integer` | **Required**. id user |

Headers

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Authorization`      | `string` | **Required**. Access Token |



#### Update User
Description: this endpoint is used to update the data of a product.


```http
  PUT {{baseUrl}}/api/v1/users/{{userId}} 
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `userId` | `integer` | **Required**. id user |
| `name`      | `string` | **Required**. name user |
| `email`      | `string` | **Required**. email Authorization |
| `address`      | `string` | **Required**. address Authorization |
| `phone`      | `string` | **Required**. phone user |
| `password`      | `string` | **Required**. user password |

Headers

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Authorization`      | `string` | **Required**. Access Token |


#### Delete User
Description: this end point is used to eliminate a user.


```http
  DELETE {{baseUrl}}/api/v1/users/{{userId}}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `userId` | `integer` | **Required**. id user |


