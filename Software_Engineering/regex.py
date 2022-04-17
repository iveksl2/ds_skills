import re

regex=r"\[(\d+)\]"
re.search(regex, log)
print(result[1])

# Simple matching
result = re.search(r"aza", "plaza") # good idea to use raw strings
print(result)
result = re.search(r"aza", "bazaar") 
print(result)

result = re.search(r"aza", "ma") 
print(result)

print(re.search(r"^x", "xenon"))
print(re.search(r"p.ng", "penguin"))
print(re.search(r"p.ng", "sponge"))

print(re.search(r"p.ng", "Pangea", re.IGNORECASE))

# Wilwcard and character classes
print(re.search(r"[Pp]ython", "Python"))
print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search(r"[a-z]way", "What a way to go")) #None
print(re.search(r"cloud[a-zA-Z0-9]", "cloudy"))
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces")) # matches first space
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))  # final dot
print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I like dogs."))
print(re.search(r"cat|dog", "I like both dogs and cats.")) # greedy
print(re.findall(r"cat|dog", "I like both dogs and cats.")) 

# repeated matches
print(re.search(r"Py.*n", "Pygamillion"))
print(re.search(r"Py.*n", "Python Programming")) # Greedy, takes as much as possible
print(re.search(r"Py[a-z]*n", "Python Programming")) 
print(re.search(r"Py[a-z]*n", "Pyn")) 
print(re.search(r"o+l+", "goldfish")) 
print(re.search(r"o+l+", "woolly")) 
print(re.search(r"o+l+", "boil")) 
print(re.search(r"p?each", "To each their own")) 
print(re.search(r"p?each", "I like peaches")) 

# Escaping Characters
print(re.search(r"\.com", "google.com")) 

print(re.search(r"\w*", "This si an example")) 
print(re.search(r"\w*", "and_this_is_another")) 

print(re.search(r"A.*a", "Argentina")) 
print(re.search(r"A.*a", "Azrbaijan")) 
print(re.search(r"^A.*a$", "Azrbaijan")) 
print(re.search(r"^A.*a$", "Australia")) 

print(re.search(r"^[a-zA-Z_][a-z-A-Z0-9_]*$", "this_is_a_valid_variable_name")) 
print(re.search(r"^[a-zA-Z_][a-z-A-Z0-9_]*$", "this isn't a valid variable name")) 
print(re.search(r"^[a-zA-Z_][a-z-A-Z0-9_]*$", "my_variable1")) 
print(re.search(r"^[a-zA-Z_][a-z-A-Z0-9_]*$", "2my_variable1")) 

# https://docs.python.org/3/howto/regex.html
# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#greedy-versus-non-greedy
# https://regex101.com/


#capturing Groups
result = re.search(r"^(\w*), (\w*)$", "lovelace, Ada")
print(result.groups())
print(result[0])
print(result[1])
print(result[2])

def rearrange_name(name):
    result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
    if result is None:
        return name
    return f"{result[2]} {result[1]}"

rearrange_name("Lovelace, Ada")
rearrange_name("Ritchie, Dennis")
rearrange_name("Hopper, Grace M.")

# numeric repitation qualifiers
print(re.search(r"[a-zA-z]{5}", "a ghost"))
print(re.search(r"[a-zA-z]{5}", "a scary ghost appeared"))
print(re.findall(r"[a-zA-z]{5}", "a scary ghost appeared"))
print(re.findall(r"\b[a-zA-Z]{5}\b", "a scary ghost appeared"))
print(re.findall(r"\w{5,10}", "i really like strawberries"))
print(re.search(r"s\w{,20}", "i really like strawberries"))

regex = r"\[(\d+)\]"
result = re.search(regex, "A completely different string that also has numbers [34567]")
print(result[1])

result = re.search(regex, "99 elephants in a [cage]")
print(result[1])

def extract_pid(log_line): 
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]

print(extract_pid("99 elephants in a [cage]"))

#splitting and replacing
re.split(r"[.?!]", "One stenance. Another one? And the last one!")
re.split(r"([.?!])", "One stenance. Another one? And the last one!")

re.sub(r"[\w.%+-]+@[\w.-]+", "REDACTED", "Received an email for go_nuts95@my.examples.com")

re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada") # capture groups are backrefences

# https://regexcrossword.com/
