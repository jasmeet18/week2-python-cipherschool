#Datastructures

#string operations

#string formatting or string interpolation
a=5
print("value of a is %d" %(a))
print("value of a is {}".format(a))

a,b,c = 1,2,3
print("a={2},b={1}.c={0}".format(c,b,a))

name="Samiksha"
college="LPU"

print("name={name} college={college}".format(name=name,college=college))
print(f"name={name}")

name="Samiskha"
college="LPU"
print("Hello {name}, welcome to {college}".format(name=name,college=college))

print(len(r"a\nb"))

print("         samiksha            ".strip())

print("1,2,3,4,5".split(","))

print("Samiksha".replace("i","ee"))

print("Samiksha".count("a"))