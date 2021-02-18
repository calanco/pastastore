import pytest
from pastastore.vote_engine import ve
from pastastore.recipe_error import RecipeError


class TestVoteEngine():
    def test_vote_recipe(self):
        ve.clean_votes()

        recipe = "amatriciana"
        ve.vote_recipe(recipe)

        assert ve.get_vote(recipe) == 1

    def test_vote_recipe_wrong(self):
        ve.clean_votes()

        recipe = "amatriciana"
        ve.vote_recipe(recipe)

        assert ve.get_vote(recipe) != 0

    def test_vote_recipe_unexisting_recipe(self):
        ve.clean_votes()

        recipe = "unexisting_recipe"
        with pytest.raises(RecipeError,
                           match="{} is not allowed".format(recipe)):
            ve.vote_recipe(recipe)

    def test_sort_pasta_recipes(self):
        input_recipes = {"cacio e pepe": 1, "carbonara": 2, "amatriciana": 3}
        expected_output_recipes = (("amatriciana", 3,), ("carbonara", 2,),
                                   ("cacio e pepe", 1,),)
        output = tuple(ve.sort_pasta_recipes(input_recipes))
        assert output == expected_output_recipes

    def test_sort_pasta_recipes_wrong(self):
        input_recipes = {"cacio e pepe": 1, "carbonara": 2, "amatriciana": 3}
        expected_output_recipes = (("cacio e pepe", 1,), ("carbonara", 2,),
                                   ("amatriciana", 3,),)
        output = tuple(ve.sort_pasta_recipes(input_recipes))
        assert output != expected_output_recipes
