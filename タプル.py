travel = ('passport','wallet','phone')
print(travel)
print(travel[2])

travel_A = ('phone')
travel_B = tuple(travel_A)
print(travel_B)

travel = ('passport','wallet','phone','camera','map')
print(travel[3:])

travel = ('passport','wallet','phone','camera','map')
print(travel[::2])

travel = (('passport','wallet'),('phone','camera'))
print(travel[1][0])

travel = ('passport','wallet','phone')
bag = travel + ('camera','map')
print(bag)

travel = ('passport','wallet','phone')*2
print(travel)

travel = ('passport','wallet','phone')
print('phone' in travel)

travel = ('passport','wallet','phone')
print(len(travel))

travel = ('passport','wallet','phone')
print(max(travel))
print(min(travel))

test = (55,60,65,70,75,80)
print(sum(test))
print(sum(test)/len(test))

travel = ('passport','wallet','phone')
print(travel.index('phone'))

travel = ('passport','wallet','phone')
print(travel.count('wallet'))

number = (1,6,4,5,3,2)
print(sorted(number))

restaurant_A = ('Italian','Japanese','Mexican')
print(restaurant_A)

restaurant_A = ('Italian','Japanese','Mexican')
restaurant_B = restaurant_A+ ('Indian','French')
print(restaurant_B)

print(restaurant_B[:-3])

restaurant_C = (('Italian','Japanese'),('Mexican','Indian'))
print(restaurant_C[1][1])

m = ("menu")
restaurant_D = (m in m)
print(restaurant_D)

#模範解答
m = "menu"
restaurant_D = tuple(m)
print('m' in restaurant_D)