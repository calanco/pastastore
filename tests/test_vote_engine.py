from pastastore.vote_engine import ve


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

    def test_sort_pasta_recipes(self):
        input_recipes = {"cacio e pepe": 1, "carbonara": 2, "amatriciana": 3}
        expected_output_recipes = [("amatriciana", 3,), ("carbonara", 2,),
                                   ("cacio e pepe", 1,)]

        assert ve.sort_pasta_recipes(input_recipes) == expected_output_recipes

    def test_sort_pasta_recipes_wrong(self):
        input_recipes = {"cacio e pepe": 1, "carbonara": 2, "amatriciana": 3}
        expected_output_recipes = [("cacio e pepe", 1,), ("carbonara", 2,),
                                   ("amatriciana", 3,)]

        assert ve.sort_pasta_recipes(input_recipes) != expected_output_recipes
