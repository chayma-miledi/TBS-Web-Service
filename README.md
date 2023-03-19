# Store and Inventory Management RESTful API

This project is a RESTful API developed using Python Flask for organizing stores and managing inventory items. The API contains all CRUD operations and is secured with JWT token authentication.

## Installation
1. Clone this repository
2. Install the required packages by running pip install -r requirements.txt
3. Run the app with python app.py
4. The API will be running at http://localhost:5000

## API Endpoints
* /register (POST): Registers a new user.
* /login (POST): Logs in an existing user and returns a JWT token.
* /logout (POST): Logs out the user by revoking their JWT token.
* /stores (GET): Retrieves a list of all stores.
* /store/<string:name> (GET): Retrieves a store by its name.
* /store/<string:name> (POST): Adds a new store with a given name.
* /store/<string:name> (PUT): Updates the details of a store with a given name.
* /store/<string:name> (DELETE): Deletes a store with a given name.
* /items (GET): Retrieves a list of all items.
* /item/<string:name> (GET): Retrieves an item by its name.
* /item/<string:name> (POST): Adds a new item with a given name and price to a store.
* /item/<string:name> (PUT): Updates the details of an item with a given name.
* /item/<string:name> (DELETE): Deletes an item with a given name.

## Testing
Multiple Insomnia snippets have been provided in the insomnia directory to test the API endpoints. Simply import the desired snippet into Insomnia and execute the requests.

## Security
The API endpoints are secured with JWT token authentication. The authenticate function in user.py checks the user credentials and returns a JWT token upon successful authentication. The identity function in security.py takes the JWT token and returns the user information if the token is valid.

## Docker
This project includes a Dockerfile for easy deployment. To build a Docker image, run the following command:

```
docker build -t store-inventory-api .
```
Then, to run the Docker container:
```
docker run -p 5000:5000 store-inventory-api
```
The API will be accessible at http://localhost:5000.

## Acknowledgements
This project was developed as part of the IT325 course at Tunis Business School. Special thanks to Mr Montassar Ben Messaoud for providing guidance and support throughout the project.
