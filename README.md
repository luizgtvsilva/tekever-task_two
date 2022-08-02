
# Current Account - A TEKEVER CHALLENGE

Some assumptions was taked about this challenge:

1) I assume that when you said "The assessment consists of an API to open a new 'current account' of already existing customers" it's necessary have an initial customers informations. For that, I created an initial data that will be loaded when you run the project.

2) About the "Once the endpoint is called, a new account will be opened and connected to the user whose ID is customerID" I assume that an current account can only be created if we already have the user into our database

3) When you said "Also, if initialCredit is not 0, a transaction will be sent to the new account" I assume that is necessary create an API that allow two users transact money between two current accounts

Due that, I created an app using DRF (Django Rest Framework) which contains Customers, Current Account and Transaction. Each one of this modules has a CRUD implemented.






## Install and run

Clone the project using git:
```bash
  git clone https://github.com/luizgtvsilva/tekever-task_two.git
```

Navigate to the project:
```bash
  cd tekever-task_two
```

Then run:
```bash
  docker-compose up --build
```

Everything you need will be installed and you can run through :8000 PORT


## API Documentation



#### Swagger
Once the project is running, you can found the API Documentation in:

```http
  http://127.0.0.1:8000/swagger/
```

But for the POSTs:


```http
  POST /api/customers/
```

 Type       | Example                                 |
 :--------- | :------------------------------------------ |
 `json` | {	"first_name":"Luiz", "last_name":"da Silva" } |

```http
  POST /api/current_accounts/
```

 Type       | Example                                 |
 :--------- | :------------------------------------------ |
 `json` | {	"customer_account": 3, 	"balance": 10.0 } |

 ```http
  POST /api/transactions/
```

 Type       | Example                                 |
 :--------- | :------------------------------------------ |
 `json` | {	"from_customer": 2,	"to_customer": 1,"amount": 5.0,	"description": "About that drink"} |


## To improve

For now we have some things that could be improved, as:

0) OAuth to all services
1) Implementation of Unit Test
2) An better data-integrity about Foreign Keys
3) Comments in the code

