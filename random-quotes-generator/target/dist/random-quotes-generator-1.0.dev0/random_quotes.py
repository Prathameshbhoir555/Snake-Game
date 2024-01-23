
# This is a program that generates random quotes

import random


# list of random quotes

# Final Data Structure
Quotes = [
    "In three words I can sum up everything I've learned about life: it goes on. ― Robert Frost",

    "To live is the rarest thing in the world. Most people exist, that is all. ― Oscar Wilde",

    "Live as if you were to die tomorrow. Learn as if you were to live forever. ― Mahatma Gandhi",
    
    "You may say I'm a dreamer, but I'm not the only one. I hope someday you'll join us. And the world will live as one. -John Lennon",
   
    "The only thing we have to fear is fear itself. -Franklin D. Roosevelt"
]


     #(Mostly) Side Effect free Functions

def random_quote():
#Get a random quote from the list
    return random.choice(Quotes)



#Find quotes based on the author's name

def find_quotes_by_author(author):         #--------> Functions as Parameters and Return Values
    
    return list(filter(lambda quote: author.lower() in quote.lower(), Quotes)) #----> lambda function is anonymous function


     #Use OF Higher Order Function

def quote_formatter(formatter_func):             #-------> Functions as Parameters and Return Values
    #Generating a quote formatter function.
    def format_quote(quote):
        return formatter_func(quote)
    return format_quote   #---------------> closure Function

# quote formatter function
def add_line_breaks(quote):
    return "\n".join(quote.split(" - "))


# Use of higher-order function to create a formatted quote function
formatted_quote = quote_formatter(add_line_breaks)


random_quote = random_quote()
filtered_quotes = find_quotes_by_author("Mahatma Gandhi")
formatted_random_quote = formatted_quote(random_quote)


print("Random Quote:")
print(formatted_random_quote)

print("\nFiltered Quotes by Author (mahatma Gandhi):")
for quote in filtered_quotes:
    print(formatted_quote(quote))
