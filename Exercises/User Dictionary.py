#user dictionary
#1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'

#2 iterate and print all the keys in the above user.

#3 Add a new weapon to your user

#4 Add a new key to include 'is_banned'. Set it to false

#5 Ban the user by setting the previous key to True

#6 create a new user2 my copying the previous user and update the age value and username value.

user_profile = {
    'age' : 25,
    'username' : 'ballsdeep69',
    'weapons' : ['Scimitar', 'Long Sword', 'Two HUGE FUCKING SHARKS'],
    'is_active' : True,
    'clan' : 'Midnight Black Cats'
}
#print(user_profile)
#print(user_profile.keys())
#user_profile.update({'weapons': ["An extra HUGE FUCKING SHARK"]}) #doesnt add, but changes the function
#user_profile.update({'is_banned': False})
#user_profile.update({'is_banned' : True}) #technically does it, but not the solution hes looking for
#new_user2 = user_profile.copy()
#print(user_profile)

#actual solution

user = {
    'age' : 22,
    'username' : 'Craig',
    'weapons' : ['a gun', 'also a gun'],
    'is_active': True,
    'clan' : 'Machinima'
}
print(user.keys())
user['weapons'].append('another gun') #you can grab
print(user['weapons'])
user.update({'is_banned' : False})
user['is_banned'] = True
print(user)
user2 = user.copy()
user2.update({'age' : 100,
              'username' :'Timbo'
              })
print(user2)