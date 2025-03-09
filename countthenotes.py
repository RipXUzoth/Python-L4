Amount =int(input("Please Enter Amount for Withdraw :"))
note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10
print("note of hunded rupees" , note_1)
print("note of fifty rupees" , note_2)
print("note of ten rupees" , note_3)