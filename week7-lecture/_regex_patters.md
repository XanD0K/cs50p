# Regex

## Regex patterns
It can take a whole bunch of symbols:

- . → any character except a newline
- \* → 0 or more repetitions
- \+ → 1 or more repetitions
- ? → 0 or 1 repetition
- {m} → m repetitions
- {m, n} → m-n repetitions
- ^ → matches the start of the string
- $ → matches the end of the string (just before the newline at the end of the )string
- [ ] → set of characters to specifically look for
- [^] → complementing the set, meaning the set of characters that you cannot match


- \d → decimal digits (e.g. 0-9)
- \D → not decimal digits
- \s → whitespace characters
- \S → not whitespace characters
- \w → word characters (alphanumeric characters and underscore)
- \W → not word characters


- \b → word boundary. It isn't a character! It is used for 2 things:  
    1- makes reference to the boundary between a word character (\w) and a non-word character (\W)  
    2- references the start/end of a string (if positionad ant the start/end of the string)


- A|B → either A or B
- (...) → group → return a value from the re.serach function
- (?:...) → non-capturing version, preventing the return, making it only for group conditionals, and dismissing its count on .group()


# re.search(pattern, string, flags=0)
The re.search() takes 3 parameters, being the last one an opitional parameter
Some of the flags:
- re.IGNORECASE → ignore the case of user's input. In other words, allows uppercase, lowercase or a combination of both
- re.MULTILINE
- re.DOTALL


# re.match(pattern, string, flags=0)
Dismiss the the '^' symbol at the beggining of the regular expression


# re.fullmatch(pattern, string, flags=0)
Dismiss the the '^' symbol at the beggining of the regular expression and the '$' symbol at the end of that expression


# re.sub(pattern, repl, string, count=0, flags=0)
Used to substitute a pattern a spaecific number of times (count)
So you define a pattern, what you want to replace it with (repl), and where it will be replaced (string)


# re.split(pattern, string, maxsplit=0, flags=0)
Split a string by using multiple characters


# re.findall(pattern, string, flags=0)
Allow to search for multiple copies of the same pattern in different places in a string, so that you can, for example, manipulate more than jsut one