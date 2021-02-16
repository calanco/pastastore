from pastastore.vote_engine import ve


class TestVoteEngine():
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
