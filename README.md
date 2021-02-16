# PastaStore
REST API server to rank your most preferred pasta recipes.

## Pasta recipes
You can vote for the following pasta recipes:
1. `cacio e pepe`
2. `carbonara`
3. `ragù alla bolognese`
4. `spaghetti pomodoro e basilico`
5. `pasta al pesto`
6. `amatriciana`
7. `pasta fredda`

## Instructions
Use the following endpoints to know what are the most voted pasta recipes:
- `/store` POST: vote for your pasta recipe! Upload a JSON message containing the `recipe` as a key
- `/get_recipe/<recipe>` GET: retrieve the votes of pasta `recipe`
- `/get_recipes` GET: retrieve all the voted pasta recipes and see their votes
- `/rank` GET: get the rank of all pasta recipes!
- `/clean` GET: delete all votes
