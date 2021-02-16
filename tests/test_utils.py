from pastastore.api.utils import sort_pasta_recipes


def test_sort_pasta_recipes():
    input_recipes = {"cacio e pepe": 1, "carbonara": 2, "amatriciana": 3}
    expected_output_recipes = [("amatriciana", 3,), ("carbonara", 2,),
                               ("cacio e pepe", 1,)]

    assert sort_pasta_recipes(input_recipes) == expected_output_recipes


def test_sort_pasta_recipes_wrong():
    input_recipes = {"cacio e pepe": 1, "carbonara": 2, "amatriciana": 3}
    expected_output_recipes = [("cacio e pepe", 1,), ("carbonara", 2,),
                               ("amatriciana", 3,)]

    assert sort_pasta_recipes(input_recipes) != expected_output_recipes
