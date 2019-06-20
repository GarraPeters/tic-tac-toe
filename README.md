# tic-tac-toe

> "A strange game. The only winning move is not to play."

Run "docker-compose up" to start.
Runs on 0.0.0.0:8000 by default

Human player is "X" and always goes first.

to play, make a GET request with the gameboard in the query sting as shown:

YOUR_URL?board=+xxo++o++

The API will return a similar game board string with it's move included.