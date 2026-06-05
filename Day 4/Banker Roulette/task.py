
import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_friend = friends[random.randint(0,len(friends)-1)]
print(random_friend)
print(random.choice(friends))