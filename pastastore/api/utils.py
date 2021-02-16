import heapq


def sort_pasta_recipes(recipes: dict) -> list:
    '''
    Sorting recipes using the heapsort. Getting the decreasing order from it
    '''
    h = []
    for recipe in recipes.items():
        heapq.heappush(h, (-recipe[1], recipe[0],))

    negated_sorted_recipe = [heapq.heappop(h) for i in range(len(h))]

    sorted_recipe = []
    for recipe in negated_sorted_recipe:
        sorted_recipe.append((recipe[1], -recipe[0],))

    return sorted_recipe
