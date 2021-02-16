import os
import json
import heapq


class VoteEngine():
    # holds the allowed recipes
    counts = dict()

    # pasta_recipes holds the allowed recipes
    pasta_recipes = set()

    def __init__(self):
        '''
        Initializing counts and pasta_recipes attributes
        '''
        super().__init__()
        if not os.path.isfile("votes.txt"):
            open("votes.txt", 'a').close()

        with open("votes.txt", 'r') as vote_file:
            try:
                votes = json.load(vote_file)
                self.counts = dict(votes)
            except json.decoder.JSONDecodeError as e:
                print(e)

        self.pasta_recipes = {"cacio e pepe", "carbonara",
                              "ragù alla bolognese",
                              "spaghetti pomodoro e basilico",
                              "pasta al pesto", "amatriciana",
                              "pasta fredda"}

    def vote_recipe(self, recipe: str):
        '''
        Voting recipe
        '''
        if recipe not in self.counts:
            self.counts[recipe] = 0
        self.counts[recipe] += 1

        with open("votes.txt", 'w') as vote_file:
            try:
                json.dump(self.counts, vote_file)
            except json.decoder.JSONDecodeError as e:
                print(e)

    def sort_pasta_recipes(self, recipes: dict) -> list:
        '''
        Sorting recipes using heapsort. Getting the decreasing order from it
        '''
        h = []
        for recipe in recipes.items():
            heapq.heappush(h, (-recipe[1], recipe[0],))

        negated_sorted_recipe = [heapq.heappop(h) for i in range(len(h))]

        sorted_recipe = []
        for recipe in negated_sorted_recipe:
            sorted_recipe.append((recipe[1], -recipe[0],))

        return sorted_recipe

    def clean_votes(self):
        '''
        Cleaning saved votes
        '''
        self.counts = dict()
        with open("votes.txt", 'w') as vote_file:
            try:
                json.dump(self.counts, vote_file)
            except json.decoder.JSONDecodeError as e:
                print(e)


ve = VoteEngine()
