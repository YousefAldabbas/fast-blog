# fast-blog API
## Welcome! 👋

Thanks for checking out this project!

this project was build during my internship at fintech ahli bank ,i build this project to learn FastAPI on my prefered way learn by building project,

*this projects doesn't done yet*

## Open Endpoints

Open endpoints require no Authentication.
### Login
* [Login](./documentation/Auth/Login.md) : `POST /api/login/`

### User
* [Register](./documentation/User/Register.md) : `POST /api/user/`
* [Show info](./documentation/User/Show.md) : `GET /api/user/:id` **for testing purpose*

### Blog
* [Show All](All.md) : `GET /api/blog/`
* [Show one](One.md) : `GET /api/blog/:id`


## Endpoints that require Authentication

Closed endpoints require a valid Token to be included in the header of the
request. A Token can be acquired from the Login view above.

### Current User related

Each endpoint manipulates or displays information related to the User whose
Token is provided with the request:

### Blog
* [Publish a blog](./documentation/Blog/Publish.md) : `POST /api/blog/`
* [Update a blog]() : `UPDATE /api/blog/:id`
* [Delete a blog]() : `DELETE /api/blog/:id`

### Account related

Endpoints for viewing and manipulating the Accounts that the Authenticated User
has permissions to access.

* [Show An Account]() : `GET /api/user/me/` 
* [Update An Account](): `PATCH /api/user/` 
* [Delete An Account](): `DELETE /api/user/`
* [Refresh Token](): /api/refresh
