def cookie_giveaway(host, friends):
    for friend in friends:
        print(host + ' and ' + friend + " swap cookies!")


def cookie_swap(friends):
    for friend in friends:
        cookie_giveaway(friend, friends)


def cookie_swap_too(friends):
    for friend in friends:
        for friend2 in friends:
            print(friend + ' and ' + friend2 + " swap cookies!")
