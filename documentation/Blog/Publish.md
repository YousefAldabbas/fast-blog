# Publish

Used to publish new blog

**URL** : `/api/blog/`

**Method** : `POST`

**Auth required** : YES

**Data constraints**

```json
{
  "title": "[string]",
  "body": "[string]"
}
```

**Data example**

```json
{
  "title": "how awesome FastAPI is",
  "body": "lorem"
}
```

## Success Response

**Code** : `201 CREATED`

**Content example**

```json
{
  "title": "string",
  "created_at": "2022-10-26T22:25:11.401723+03:00",
  "user_id": 1,
  "id": 6,
  "body": "string",
  "updated_at": null
}
```

## Error Response

**Condition** : Invalid data

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
            "msg": "value is not a valid X",
            "type": "type_error.X"
        }
    ]
}
```

