#user input 

adjective= input('Give me an adjective:') 
animal = input ('What is the name of the animal:')
verb1 = input ('Give me a verb:')
exclamation1 = input ('Give me an exclamation:')
verb2 = input ('Give me a verb:')
verb3 = input ('Give me a verb:')
phrase = input ('Give me a phrase:')
verb4 = input ('Give me a verb:')
exclamation2 = input ('Give me an exclamation:')
verb5 = input ('Give me a verb:')
word1 = ('miraculously')
new_word1= word1.capitalize()
word2 = ('it')
new_word2= word2.capitalize()


madlib= f'The other day, I was really in trouble. It all started when I saw a very {adjective} {animal} {verb1} down the hallway. {exclamation1} I yelled.\
But all I could think to do was to {verb2} over and over. {new_word1} that caused it to stop, but not before it tried to {verb3} right in front of my family. \
{phrase} suggested we let it be, and also {verb4} a cool place for the snail to rest and regain strength. {exclamation2} {new_word2} {verb5} into the garden'

print(madlib)
