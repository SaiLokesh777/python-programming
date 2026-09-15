num=input("enter some scentence :")
num=num.lower()
count_words=0
count_vowels=0
count_consonants=0

for ch in num:
    if ch in "aeiou":
        count_vowels +=1
    elif ch in "bcdfghjklmnpqrstvwxyz":
        count_consonants +=1
count_words=len(num)

print(f"Number of words: {count_words}")
print(f"Number of vowels: {count_vowels}")
print(f"Number of consonants: {count_consonants}")
print(f"Number of unique characters: {len(set(num))}")

# store in list
list=[]
for i in num:
    list.append(i)
print(list)

# set to store unique characters

unique_chars=set(num)
print(unique_chars)

# store in dictionary
dict={
    "total words":count_words,
    "total vowels":count_vowels,
    "total consonants":count_consonants,
    "total unique characters":len(set(num))
}
for key, value in dict.items():
    print(key, value)
