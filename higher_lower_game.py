# string
print("hello")
print('hello'[0])
print("123" + "345")
print(len("hello"))

#integer

12345
print(123+345)

#float

3.12132

# boolean

True / False


# bug exe
num_char = len(input("what is your name"))
print("your name has" + num_char + "chars") # this line has a bug

#solution  :
num_char = len(input("what is your name"))
str(num_char)
print(f"your name has {num_char} chars")

