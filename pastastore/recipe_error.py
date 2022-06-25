class RecipeError(Exception):
    '''
    Exception raised when a recipe is tried to be voted but it's not contained
    in __pasta_recipes
    '''
    def __init__(self, recipe: str):
        super().__init__(f"{recipe} is not allowed")
