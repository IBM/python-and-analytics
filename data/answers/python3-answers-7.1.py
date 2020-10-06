# 7.1.1 Assign a string to a variable
a_string = 'tHis is a sTriNg'

# 7.1.2 Return a capitalized version of the string
a_string.capitalize()

# 7.1.3 Return an uppercase version of the string
a_string.upper()

# 7.1.4 Return a lowercase version of the string
a_string.lower()

# 7.1.5 Notice that the methods called have not actually modified the string
a_string

# 7.1.6 Count number of occurences of the substring 'i' in the string
a_string.count('i')

# 7.1.7 Count number of occurences of the substring 'i' in the string after a certain position
a_string.count('i', 7)

# 7.1.8 Count number of occurences of the substring 'is' in the string
a_string.count('is')

# 7.1.9 Does the string start with 'this'?
a_string.startswith('this')

# 7.1.10 Does the lowercase string start with 'this'?
a_string.lower().startswith('this')

# 7.1.11 Does the string end with 'Ng'?
a_string.endswith('Ng')

# 7.1.12 Return a version of the string with a substring replaced with something else
a_string.replace('is', 'XYZ')

# 7.1.13 Return a version of the string with a substring replaced with something else
a_string.replace('i', '!')

# 7.1.14 Return a version of the string with the first 2 occurences a substring replaced with something else
a_string.replace('i', '!', 2)
