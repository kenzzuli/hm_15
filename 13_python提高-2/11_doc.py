class Test(object):
    """这是类的描述"""
    pass


# 查看类的描述
# 1.help
print(help(Test))

# Help on class Test in module __main__:
# Help on class Test in module __main__:
#
# class Test(builtins.object)
#  |  这是类的描述
#  |
#  |  Data descriptors defined here:
#  |
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |
#  |  __weakref__
#  |      list of weak references to the object (if defined)
#
# None

# 2.__doc__
print(Test.__doc__)
# 这是类的描述
