class car:
    pass #return null gibi

car1 = car()
car1.name = "audi"
car1.model = "A8"
print(car1.model)
print(car1.name)


# Constructor Class
class _car:

    def __init__(self,name,model,seats):
        self.name = name
        self.model =model
        self.seats = seats

    def seatschange(self,seats):
        self.seats = seats



get_car = _car("bmw","m3",4)
print(get_car.name)
print(get_car.seats)
get_car.seats = 12
print(get_car.seats)


class User:
    def __init__(self,username,followers,following):
        self.username = username
        self.followers = followers
        self.following = following

    def Follow(self,user):
        user.followers +=1
        self.following +=1



user1 = User("Emircan",0,0)
user2 = User("Mehmet",0,0)

user2.Follow(user1)
print(user2.followers)
