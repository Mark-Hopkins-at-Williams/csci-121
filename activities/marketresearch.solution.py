populations = {('sesamopolis', 'sesame'): 4200000,
               ('sesameville', 'sesame'): 2700,
               ('springfield', 'sesame'): 51000,
               ('silopomases', 'emases'): 2400000,
               ('ellivemases', 'emases'): 4200000,
               ('kermiton', 'muppet empire'): 57000,
               ('kermitberg', 'muppet empire'): 125000,
               ('kermitshire', 'muppet empire'): 1200,
               ('springfield', 'oregon'): 62000}


def focus_on(state, population_dict):
    result = dict()
    for key in population_dict:
        if key[1] == state:
            result[key[0]] = population_dict[key]
    return result

