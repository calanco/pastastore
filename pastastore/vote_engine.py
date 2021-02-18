import os
import json
import heapq
import threading
from .logger import logger
from .recipe_error import RecipeError

lock = threading.Lock()


class VoteEngine():
    # holds the allowed recipes
    __votes = dict()

    # pasta_recipes holds the allowed recipes
    __pasta_recipes = set()

    def __init__(self):
        '''
        Initializing votes and pasta_recipes attributes
        '''
        super().__init__()

        with lock:
            if not os.path.isfile("votes.txt"):
                logger.warning("Creating votes.txt file")
                open("votes.txt", 'a').close()

            with open("votes.txt", 'r') as vote_file:
                try:
                    votes = json.load(vote_file)
                    self.__votes = dict(votes)
                except json.decoder.JSONDecodeError as e:
                    logger.error(e)

        self.__pasta_recipes = {"cacio e pepe", "carbonara",
                                "ragù alla bolognese",
                                "spaghetti pomodoro e basilico",
                                "pasta al pesto", "amatriciana",
                                "pasta fredda"}

    def get_votes(self) -> dict:
        '''
        Returning votes
        '''
        return self.__votes

    def get_vote(self, recipe: str) -> int:
        '''
        Returning vote of recipe
        '''
        if recipe not in self.__votes:
            return 0
        return self.__votes[recipe]

    def get_pasta_recipes(self) -> set:
        '''
        Returning pasta_recipes
        '''
        return self.__pasta_recipes

    def vote_recipe(self, recipe: str):
        '''
        Voting recipe
        '''
        if recipe not in self.__pasta_recipes:
            raise RecipeError(recipe)

        if recipe not in self.__votes:
            self.__votes[recipe] = 0
        self.__votes[recipe] += 1

        with lock:
            with open("votes.txt", 'w') as vote_file:
                try:
                    json.dump(self.__votes, vote_file, indent=4)
                except json.decoder.JSONDecodeError as e:
                    logger.error(e)

    def sort_pasta_recipes(self, recipes: dict) -> tuple:
        '''
        Sorting recipes using heapsort. Getting the decreasing order from it
        '''
        h = []
        for recipe in recipes.items():
            heapq.heappush(h, (-recipe[1], recipe[0],))

        negated_sorted_recipe = [heapq.heappop(h) for i in range(len(h))]

        for recipe in negated_sorted_recipe:
            yield (recipe[1], -recipe[0],)

    def clean_votes(self):
        '''
        Cleaning saved votes
        '''
        self.__votes = dict()

        with lock:
            with open("votes.txt", 'w') as vote_file:
                try:
                    json.dump(self.__votes, vote_file, indent=4)
                except json.decoder.JSONDecodeError as e:
                    logger.error(e)


ve = VoteEngine()
