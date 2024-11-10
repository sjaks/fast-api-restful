## FastAPI RESTful API template

### Usage

Clone the repo and install FastAPI to your host. Run:

```
fastapi dev
```

### Structure

```
api
  car
    controller
        carController
    service
        carService
    model
        carModel
  train
    controller
        trainController
    service
        trainService
    model
        trainModel
util
  common
```

### Features

Implements a RESTful API with all basic functionalities such as support for multiple JSON-based
endpoints, support for all request types (verbs: GET, POST, PUT, DELETE), input validation and
according-to-spec responses.

### TODO

- [ ] OpenAPI yaml documentation
- [ ] GET/PUT/DELETE methods
- [ ] Basic bearer authentication
- [ ] Repository layer and saving data to a dummy database
