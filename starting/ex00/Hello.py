ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
print("/n")

ft_list[1] = "World!"
ft_tuple = ("Hello", "France!")

ft_set.remove("tutu!")
ft_set.add("Paris!")

ft_dict["Hello"] = "42 Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)