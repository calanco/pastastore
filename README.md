# PastaStore
REST API server to rank the most preferred pasta recipes.

## Pasta recipes
You can choose vote for the following pasta recipes:
1. `lasagne`
2. `spaghetti_alla_carbonara`
3. `linguine_al_pesto`
4. `cannelloni`

## Instructions
Use the following endpoints to know what's the most preferred pasta recipe:
- `/store` POST: vote for your pasta recipe! Upload a JSON message containing the `recipe` as a key
- `/get_recipes` GET: retrieve all the added pasta recipes and see their ranks
- `/rank` GET: get the rank of pasta recipes. You'll also get the number of votes for each result
