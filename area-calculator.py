import math

user_dimens = []
shapes = {'Square': ['width'], 'Rectangle':['width', 'length'], 'Triangle': ['base', 'height'], 'Circle': ['radius']}
print(shapes.keys())
shape_choice = input("Choose shape from above: ")

if shape_choice in shapes:

    required_dimen = shapes[shape_choice]

for dimen in required_dimen:
    user_dimen = int(input("Please enter your {}".format(dimen)))
    user_dimens.append(user_dimen)
    print(user_dimens)
    switcher = {
        'Square': user_dimens[0] ** 2,
        'Rectangle': [0] * user_dimens[1],
        'Triangle': (user_dimens[0] * user_dimens[1] // 2),
        'Circle': float(user_dimens[0] * math.pi())
    }
    print(shape_choice)
    print(switcher.get(shape_choice, "That's crazy!!!"))
print(shape_choice)