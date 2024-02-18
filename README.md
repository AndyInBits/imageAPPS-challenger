# IMAGEAPPS CHALLENGER README

## Introduction

This is a resolution of the challenge proposed by ImageApps. The challenge is about the logistics with a some clients and some carriers and packages. The goal is to find the best carrier for each package and the best package for each client.

## How to run

To run the project, you need to have Python 3.11 or higher installed. Then, you can run the following commands:

```bash
git clone https://github.com/AndyInBits/imageAPPS-challenger

cd imageAPPS-challenger

docker-compose up --build
```

## Libraries

The project uses the following libraries:

- Docker
- Django
- Django Rest Framework
- Django Filter
- Django Cors Headers
- Docker Compose
- Postgres
- Psycopg2

## Libraries installation
```bash
pip install requeriements.txt (this happens automatically when you run the docker-compose up --build command)
```

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository.
2. Install the required dependencies.
3. Run the Django application.

## End Points

The project has the following end points:

- Health check: http://localhost:8000/healthcheck/
- List all packages: http://localhost:8000/logistics/packages/
- List all packages by client: http://localhost:8000/logistics/client/1/packages/
- List all packages by carrier: http://localhost:8000/logistics/carrier/1/packages/
- Create a package: http://localhost:8000/logistics/package/create/
- Update a package: http://localhost:8000/logistics/package/5/edit/
- Delete a package: http://localhost:8000/logistics/package/5/delete/
- Package detail: http://localhost:8000/logistics/package/5/
- Asing a package to a carrier: http://localhost:8000/logistics/api/assign_carrier/
body={
    "package_id": 5
}


## Database

The project uses a Postgres database. The database is created and populated automatically when you run the docker-compose up --build command.

## Arquiteture
This project uses the Django framework, which is a high-level Python web framework that encourages rapid development and clean, pragmatic design. The project is divided into the following apps:
    
- logistics: This app contains the models, views, and serializers for the packages, clients, and carriers.


## Fixtures

The project uses fixtures to populate the database with some initial data. The fixtures are located in the logistics/data_fixture directory.

```bash
[
    {
      "model": "logistics.client",
      "pk": 1,
      "fields": {
        "name": "Cliente1",
        "address": "Dirección Cliente1",
        "phone_number": "123-456-7890",
        "created": "2023-01-01T12:00:00Z",
      "modified": "2023-01-01T12:00:00Z"
      }
    },
    {
      "model": "logistics.client",
      "pk": 2,
      "fields": {
        "name": "Cliente2",
        "address": "Dirección Cliente2",
        "phone_number": "987-654-3210",
        "created": "2023-01-01T12:00:00Z",
      "modified": "2023-01-01T12:00:00Z"
      }
    },
  
    {
      "model": "logistics.carrier",
      "pk": 1,
      "fields": {
        "name": "Transportista1",
        "vehicle_type": "Camión",
        "contact_number": "555-1234",
        "created": "2023-01-01T12:00:00Z",
      "modified": "2023-01-01T12:00:00Z"
      }
    },
    {
      "model": "logistics.carrier",
      "pk": 2,
      "fields": {
        "name": "Transportista2",
        "vehicle_type": "Furgoneta",
        "contact_number": "555-5678",
        "created": "2023-01-01T12:00:00Z",
      "modified": "2023-01-01T12:00:00Z"
      }
    },
  
    {
      "model": "logistics.package",
      "pk": 1,
      "fields": {
        "weight": "2.5",
        "dimensions": "20x30x10",
        "origin_address": "Origen Paquete1",
        "destination_address": "Destino Paquete1",
        "delivery_status": "En tránsito",
        "client": 1,
        "carrier": 1,
        "created": "2023-01-01T12:00:00Z",
      "modified": "2023-01-01T12:00:00Z"
      }
    },
    {
      "model": "logistics.package",
      "pk": 2,
      "fields": {
        "weight": "1.8",
        "dimensions": "15x25x8",
        "origin_address": "Origen Paquete2",
        "destination_address": "Destino Paquete2",
        "delivery_status": "Entregado",
        "client": 2,
        "carrier": 2,
        "created": "2023-01-01T12:00:00Z",
      "modified": "2023-01-01T12:00:00Z"
      }
    }
  ]
```

## Preguntas del reto : 
1. Escribir un ejemplo de una lambda function de python : 
```python
lambda x: x + 10
```
# 2. Un ejemplo y utilización de lookup table: 
```python
lookup_table = {
    "a": 1,
    "b": 2,
    "c": 3
}

print(lookup_table["a"]) # 1
```
Lookup tables are used to store data that is not going to change and that is going to be used frequently. This is useful to avoid making a lot of queries to the database.
# 3. Retornar un n-valor de la secuencia fibonacci con recursividad
```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```
# 4. Un ejemplo de un quick sort
```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
```




## POSTMAN COLLECTION
[POSTMAN COLLECTION](/CHALLENGER%20IMAGEAPPS.postman_collection.json)