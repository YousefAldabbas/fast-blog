# Register

Used to register new user

**URL** : `/api/user/`

**Method** : `POST`

**Auth required** : NO

**Data constraints**

```json
{
    "email": "[valid email]",
    "username": "[valid username]",
    "full_name": "[valid string]",
    "password": "[password in plain text]"
}
```

**Data example**

```json
{
  "email": "user@example.com",
  "full_name": "string",
  "username": "string",
  "password": "string"
}
```

## Success Response

**Code** : `201 OK`

**Content example**

```json
{
  "email": "user@example.com",
  "full_name": "string",
  "username": "string",
  "id": 0,
  "is_active": true,
  "is_superuser": false
}
```

## Error Response

**Condition** : If user miss or enter invalid data.

**Code** : `422 ERROR`

**Content** :

  ```json
{
    "detail": [
        {
            "loc": [
                "path",
                "X"
            ],
            "msg": "value is not a valid X",
            "type": "type_error.X"
        }
    ]
}
  ```


## Notes

* For know there is no MAX or MIN length for any field :D
* Error response are not customized