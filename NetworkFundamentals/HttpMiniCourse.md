# Http Methods Mini Course
* What is http?
  * http(hyper text protocol)
  * foundation of data communication data
  * request - response
  * stateless : request is independent
* Components
  * method, get post
    * get : retrive 
    * post : submit
    * put : replace 
    * patch : update
    * delete : remove
  * url
  * header 
    * authentication most used
  * body - optional
* idempotent : on the server of multiple identical requests 

## Get
body : not allowed
idempotent : yes
safe : yes

```http request
GET /users/1 hHTTP/1.1
```

```python
@app.route(/users/, methods=['GET'])
def get_user(id):
    pass
```

## Post
body : required
idempotent : yes
safe : no

```http request
POST /users
{
    'name':'Alice'
}
```

## Patch

body : required
idempotent : yes
safe : no

```http request
PATCH /users
{c
    'name':'hello'
}
```

## Put
safe : no

body : required
idempotent : yes

```http request
put /users
{
    'name':'hello'
}
```

- rest client extension
-  