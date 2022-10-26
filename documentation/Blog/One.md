# Show blog

Used to get specific  blog data

**URL** : `/api/blog/:id`

**Method** : `GET`

**Auth required** : NO

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
  "title": "string",
  "body": "string",
  "user_id": 0,
  "created_at": "2022-10-26T19:20:10.355Z",
  "updated_at": "2022-10-26T19:20:10.355Z",
  "comments": []
}
```

## Error Response

* **Condition** : If blog doesn't exist.

  **Code** : `404 NOT FOUND`

  **Content** :

  ```json
 {
  "detail": "Blog with the id 0 is not exist"
}
  ```

* **Condition** : If user try access blog with invalid data

  **Code** : `422 ERROR`

  **Content** :

  ```json
{
    "detail": [
        {
            "loc": [
                "path",
                "id"
            ],
            "msg": "value is not a valid integer",
            "type": "type_error.integer"
        }
    ]
}
  ```

