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

### votes.txt
All votes will be stored in a `votes.txt` JSON file in the root directory.

The access to the file is handled by a `threading.Lock()` resource:
```
{
    "cacio e pepe": 4,
    "carbonara": 2
}
```

### file.log
A `file.log` log file will be created in the root directory:
```
2021-02-17 20:01:28,609 - pastastore.logger - INFO - /store {'recipe': 'carbonara'}
2021-02-17 20:01:28,609 - pastastore.logger - INFO - carbonara has been added 200
2021-02-17 20:01:30,730 - pastastore.logger - INFO - /store {'recipe': 'cacio e pepe'}
2021-02-17 20:01:30,731 - pastastore.logger - INFO - cacio e pepe has been added 200
2021-02-17 20:01:32,720 - pastastore.logger - INFO - /get_recipes
2021-02-17 20:01:32,720 - pastastore.logger - INFO - {'carbonara': 1, 'cacio e pepe': 1} 200
2021-02-17 20:01:35,111 - pastastore.logger - INFO - /rank
2021-02-17 20:01:35,111 - pastastore.logger - INFO - {1: {'recipe': 'cacio e pepe', 'votes': 1}, 2: {'recipe': 'carbonara', 'votes': 1}} 200
2021-02-17 20:01:37,532 - pastastore.logger - INFO - /get_recipe cacio e pepe
2021-02-17 20:01:37,532 - pastastore.logger - INFO - 1 200
2021-02-17 20:01:39,438 - pastastore.logger - INFO - /clean
2021-02-17 20:01:39,439 - pastastore.logger - INFO - Cleaned 200
```
