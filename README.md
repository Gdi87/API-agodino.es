# API-agodino.es

An API made with FLASK to get data from my web.

## Functionalities

* Authentication: Users can authenticate with a username and password.
* Authorization: Users can only access the data they are entitled to.
* Logging: The API tracks the requests that are made to the API.
* Monitoring: The API monitors the performance of the API.
* Availability: The API is available all the time.
* Weather: The API returns the weather in Alicante.
* News: The API returns the latest news in Alicante.
* Concerts: The API returns upcoming concerts in Alicante.
* Sports events: The API returns upcoming sporting events in Alicante.
* Cinema: The API returns upcoming movie releases in Alicante.
* Transport: The API returns information about public transportation in Alicante.

## Usage

To use the API, you will need to first authenticate. You can do this by sending a POST request to the `/login` endpoint with your username and password. Once you are authenticated, you can access the other endpoints.

For example, to get the weather in Alicante, you would send a GET request to the `/weather` endpoint. The response will be a JSON object with the current weather conditions.

Here is a list of all the endpoints and their descriptions:

* `/login`: This endpoint is used to authenticate users.
* `/logout`: This endpoint is used to log out users.
* `/weather`: This endpoint returns the weather in Alicante.
* `/news`: This endpoint returns the latest news in Alicante.
* `/concerts`: This endpoint returns upcoming concerts in Alicante.
* `/sports_events`: This endpoint returns upcoming sporting events in Alicante.
* `/cinema`: This endpoint returns upcoming movie releases in Alicante.
* `/transport`: This endpoint returns information about public transportation in Alicante.

## Documentation

The full documentation for the API is available on the [API website](https://api-agodino.es/docs).

## Contributing

If you would like to contribute to the API, please fork the GitHub repository and submit a pull request.

## License

The API is licensed under the MIT License.
