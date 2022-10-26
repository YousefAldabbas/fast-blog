# Show

Used to show user data ***only for testing purpose***

**URL** : `/api/user/:id`

**Method** : `GET`

**Auth required** : NO

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
  "id": 0,
  "email": "user@example.com",
  "full_name": "string",
  "username": "string",
  "hashed_password": "string",
  "is_active": true,
  "created_at": "2022-10-26T19:10:17.273Z",
  "updated_at": "2022-10-26T19:10:17.273Z"
}
```

## Error Response

* **Condition** : If user doesn't exist.

  **Code** : `404 NOT FOUND`

  **Content** :

  ```json
  {
  "detail": "User with the id 5 is not exist"
  }
  ```

* **Condition** : If user miss or enter invalid data.

  **Code** : `422 ERROR`

  **Content** :

  ```json
  {
    "detail": [
      {
        "loc": [
          "string",
          0
        ],
        "msg": "string",
        "type": "string"
      }
    ]
  }
  ```


## Notes

* For know there is no MAX or MIN length for any field :D
* Error response are not customized **yet**