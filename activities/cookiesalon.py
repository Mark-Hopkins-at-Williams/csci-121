def cookie_salon(guests):
    for guest in guests:
        print("C.M. gives a cookie to " + guest + "!")


def cookie_salon_too(guests):
    guest_index = 0
    while guest_index < len(guests):
        print("C.M. gives a cookie to " + guests[guest_index] + "!")
        guest_index = guest_index + 1
