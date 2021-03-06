w= input("Enter word : ")
vowels = "aeiouAEIOU"
vowels_list = [each for each in w if each in vowels]
print(vowels_list)