# Login

Used to collect a Token for a registered User.

**URL** : `/api/login/`

**Method** : `POST`

**Auth required** : NO

**Data constraints**

```json
{
    "username": "[valid username]",
    "password": "[password in plain text]"
}
```

**Data example**

```json
{
    "username": "arabov",
    "password": "arabov@admin"
}
```

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInN1YiI6IjEifQTygXY01S40swH7srY3c",
  "token_type": "bearer"
}
```

## Error Response

* **Condition** : If 'username' and 'password' combination is wrong.

  **Code** : `404 NOT FOUND`

  **Content** :

  ```json
  {
    "detail": "invalid creadentials"
  }
  ```
* **Condition** : If 'password' is wrong.

  **Code** : `404 NOT FOUND`

  **Content** :

  ```json
  {
    "detail": "incorrect password"
  }
  ```
