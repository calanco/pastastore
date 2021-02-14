# PastaStore
REST API server to rank the most preferred pasta recipes.

## Instructions
You can choose among the following pasta recipes:
1. `lasagne`
2. `spaghetti_alla_carbonara`
3. `linguine_al_pesto`
4. `cannelloni`

Use the following endpoints:
- `/store` POST: upload a JSON message containing the `recipe` as a key
- `/get_recipes` GET: retrieve the ranked pasta recipes
