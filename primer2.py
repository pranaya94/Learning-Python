
long_string = "hello world"

print(long_string[-2])
print(long_string[-2:])
print(long_string[2:-2])
print(long_string[3:])

print("%c is the number %.5f in the lang of %s" %('x', 1.2, "Pran"))
print("abc".capitalize())
print("hellow world".find("wor"))
print("hellow".isalpha())
print("hell 1 2".isalnum())
print(len("asdf"))
print("hellow world".replace("hellow", "hello"))
print("     hellow world    ".strip() + "end") #leading and trailing
split_list = "hello my name is TBone".split(" ")
print(split_list)

a = [1,2,3]
for i,a in enumerate(a):
	print(i," ",a)
