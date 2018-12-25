from random import randint

x = randint(1, 100)

cloud_str = '''
 _(  )_( )_
(_   _    _)
  (_) (__)
  '''

print(x)
if x < 30:
    print("Rain")
elif 30 < x < 60:
    print(cloud_str)
else:
    print("Sunny")
    # pass