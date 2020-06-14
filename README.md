# Setup

1. Run the migrations using `python manage.py migrate` and create a superuser using `python manage.py createsuperuser`. As using the superuser one can add Articles and Magazines. After this just run the server using `python manage.py runserver` 

2. I have setup JWT Authentication for security purposes, so a user can register an account and login which would provide them with a token. The token should be used in the request header through tools like `Postman` or some chrome extension like `modheader`. This is needed as all the APIs are permission protected.

3. There are five APIs related to articles which are documented below.

4. I have deployed the project on `Heroku` and the route is :~ https://edison101.herokuapp.com/

5. I have also created a superuser for the deployed project with credentials :~ `email` :- testing@gmail.com and `password` :- testing123


## API Documentation.

### 1. UserRegister API

#### URL:

```
/account/register/
```

### Parameters:

- Method: POST
- headers:

```
{
    Content-type: application/json
}
```

### Sample payload:

```
{
	"first_name": "Tester"
	"email": "testing@gmail.com",
	"password":"testing123"
}
```

### Sample response:

- Status code: 201

Data:

```
{
    "id": 3,
    "u_id": "a5c2cd46-919a-4f1c-977d-57bb422b99f4",
    "first_name": "Tester",
    "last_name": null,
    "email": "testing@gmail.com",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MywiZXhwIjoxNTk3MzI1NTY0fQ.-H1RKu9TCjD5-Nfm9CFxP7kw5nKpk-VaTweZ-4Nv6VM"
}
```

### 2. UserLogin API

#### URL:

```
/account/login/
```

### Parameters:

- Method: POST
- headers:

```
{
    Content-type: application/json
}
```

### Sample payload:

```
{
	"email": "testing@gmail.com",
	"password":"testing123"
}
```

### Sample response:

- Status code: 200

Data:

```
{
    "id_": 3,
    "u_id": "a5c2cd46-919a-4f1c-977d-57bb422b99f4",
    "first_name": "Tester",
    "last_name": null,
    "email": "testing2@gmail.com",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MywiZXhwIjoxNTk3MzI1ODcyfQ.X_rAyqa9IOBwRbRxpmBKoji1_II8b7T1OjU4MMzHaIA"
}
```

### 3. ArticlesList API

API to list all the articles.

#### URL:

```
/articles/
```

### Parameters:

- Method: GET
- headers:

```
{
    Content-type: application/json,
    Authorization: Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNTk2Njg4MTMxfQ.zzArFwDSZAeHa0PQ_fNYqYEMe3MMDAMmVVZDjaqagPQ
}
```

### Sample response:

- Status code: 200

Data:

```
[
    {
        "id": 1,
        "author": {
            "id": 2,
            "first_name": "Tester",
            "last_name": null,
            "email": "testing@gmail.com"
        },
        "magazine": [
            1
        ],
        "title": "Test Article 1",
        "content": "lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum",
        "date_posted": "2020-06-14T11:25:27Z"
    }
]
```

### 4. MagazinesList API

API to list all the magazines.

#### URL:

```
/magazines/
```

### Parameters:

- Method: GET
- headers:

```
{
    Content-type: application/json,
    Authorization: Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNTk2Njg4MTMxfQ.zzArFwDSZAeHa0PQ_fNYqYEMe3MMDAMmVVZDjaqagPQ
}
```

### Sample response:

- Status code: 200

Data:

```
[
    {
        "id": 1,
        "owner": {
            "id": 2,
            "first_name": "Tester",
            "last_name": null,
            "email": "testing@gmail.com"
        },
        "name": "Magazine 1"
    },
    {
        "id": 2,
        "owner": {
            "id": 1,
            "first_name": "Edison Admin",
            "last_name": null,
            "email": "test@gmail.com"
        },
        "name": "Edison"
    }
]
```

### 5. UserArticles API

API to list all articles by a specific User/Author.

#### URL:

```
/authors/<int:user_id>/articles/
```

### Parameters:

- Method: GET
- headers:

```
{
    Content-type: application/json,
    Authorization: Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNTk2Njg4MTMxfQ.zzArFwDSZAeHa0PQ_fNYqYEMe3MMDAMmVVZDjaqagPQ
}
```

### Sample response:

- Status code: 200

Data:

```
[
    {
        "id": 1,
        "author": {
            "id": 2,
            "first_name": "Tester",
            "last_name": null,
            "email": "testing@gmail.com"
        },
        "magazine": [
            1
        ],
        "title": "Test Article 1",
        "content": "lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum",
        "date_posted": "2020-06-14T11:25:27Z"
    }
]
```

### 6. MagazineArticles API

API to list all articles of a specific magazine.

#### URL:

```
/magazines/<int:magazine_id>/articles/
```

### Parameters:

- Method: GET
- headers:

```
{
    Content-type: application/json,
    Authorization: Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNTk2Njg4MTMxfQ.zzArFwDSZAeHa0PQ_fNYqYEMe3MMDAMmVVZDjaqagPQ
}
```

### Sample response:

- Status code: 200

Data:

```
[
    {
        "id": 1,
        "author": {
            "id": 2,
            "first_name": "Tester",
            "last_name": null,
            "email": "testing@gmail.com"
        },
        "magazine": [
            1
        ],
        "title": "Test Article 1",
        "content": "lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum",
        "date_posted": "2020-06-14T11:25:27Z"
    }
]
```

### 7. ArticleView API

API to fetch,update or delete a specific article.

#### URL:

```
/articles/<int:article_id>/
```

### Parameters:

- Method: GET
- headers:

```
{
    Content-type: application/json,
    Authorization: Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNTk2Njg4MTMxfQ.zzArFwDSZAeHa0PQ_fNYqYEMe3MMDAMmVVZDjaqagPQ
}
```

### Sample response:

- Status code: 200

Data:

```
{
    "id": 1,
    "author": {
        "id": 2,
        "first_name": "Tester",
        "last_name": null,
        "email": "testing@gmail.com"
    },
    "magazine": [
        1
    ],
    "title": "Test Article 1",
    "content": "lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum",
    "date_posted": "2020-06-14T11:25:27Z"
}
```

### Parameters:

- Method: PUT

### Sample payload:

```
{
	"title" : "Updated Article 1"
}
```

### Sample response:

- Status code: 200

Data:

```
{
    "id": 1,
    "author": {
        "id": 2,
        "first_name": "Tester",
        "last_name": null,
        "email": "testing@gmail.com"
    },
    "magazine": [
        1
    ],
    "title": "Updated Article 1",
    "content": "lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum",
    "date_posted": "2020-06-14T11:25:27Z"
}
```

### Parameters:

- Method: DELETE

### Sample response:

- Status code: 204

Data:

```
[
    "Article Deleted"
]
```