# voting eligibility
# pass 2 args into function -> name, age
# name : "amal" age>=18 -> amal 18 is eligible

def vote(name, age):
    if age >= 18:
        return '%s %d is eligible' % (name, age)
    else:
        return '%s %d is not eligible' % (name, age)


print(vote('Amal', 18))
print(vote('Raju', 16))
