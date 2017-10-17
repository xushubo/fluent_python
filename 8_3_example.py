charles = {'name': 'Charles L. Dodgson', 'born': 1832}
lewis = charles
print(lewis is charles)
print(id(lewis), id(charles))
lewis['balance'] = 950
print(charles)

alex = {'born': 1832, 'name': 'Charles L. Dodgson', 'balance': 950}
print(alex == charles)
print(alex is not charles)