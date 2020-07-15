# By reading the python documentation, add 3 more magic/dunder methods of your choice to this Toy class.
class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False,
        }

    def __str__(self):
        return f"{self.color}"

    def __len__(self):
        return 5

    def __del__(self):
        return "deleted"

    def __call__(self):
        return ('yes??')

    def __getitem__(self, i):
        return self.my_dict[i]

    def __hash__(self):
        return hash((self.color, self.age))

    def __bool__(self):
        return False

    def __dir__(self):
        return print('whatcha looking for')


action_figure = Toy('red', 10)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure['name'])
print(action_figure.__hash__())
print(action_figure.__bool__())
print(bool(action_figure))
action_figure.__dir__()
