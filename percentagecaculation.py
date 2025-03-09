print("Enter marks Obtained in 4 subjects: ")
math = int(input("Maths :"))
english = int(input("English :"))
science = int(input("Science :"))
hindi = int(input("Hindi :"))
sum = math+english+science+hindi
print("sum of maths,english,science, and hindi" , sum)
perc = (sum/400)*100
print(end="Percenatge Mark = ")
print(perc)