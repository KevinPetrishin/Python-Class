# do not use this code in python 3 !!
age = 17
print("My age is %d years" % age)

# %d = integer
# %s = string
# %f = float
major = "years"
minor = "months"
print("My age is %d %s, %d %s" % (age, major, 6, minor))
print("Pi is approximately %f" % (22 / 7))
print("Pi is approximately %60.50f" % (22 / 7))

# These two are the thing
print("My age is %d %s, %d %s" %
      (age, major, 6, minor))            # Used for python 2
print("My age is {0} {1}, {2} {3}".format(
    age, major, 6, minor))    # Used for python 3
