# 7.4.1 Start with a dict
capitals = {'UK':'London', 'Japan':'Tokyo', 'India':'New Delhi', 'Peru':'Lima'}
capitals

# 7.4.2 Add the Capitals Rome, Italy and Prague, Czech Republic:
capitals.update([('Czech Republic','Prague'), ('Italy','Rome')])
capitals

# 7.4.3 Create a dictionary called "new_captials" consisting of Cairo, Egypt and Helsinki, Finland. Then add it to "capitals" and print:
new_capitals = {'Egypt': 'Cairo', 'Finland': 'Helsinki'}
capitals.update(new_capitals)
capitals

# 7.4.4 Remove the UK and print it's capital
ret = capitals.pop('UK')
ret

# 7.4.5 Remove the capital of Cuba, or, if it is not found, print "Not Found":
ret = capitals.pop('Cuba', 'Not Found')
ret

# 7.4.6 return the capital of Finland, but do not remove
capitals.get('Finland')

# 7.4.7 return the capital of Mexico or "Could not find it" if it is not in the dict
capitals.get('Mexico', 'Could not find it')

# 7.4.8 list all the countries (keys) in the capitals dict
capitals.keys()

# 7.4.9 List all the capitals (values) in the capitals dict
capitals.values()

# 7.4.10 list all the countries and capitals (keys and values) in the capitals dict
capitals.items()
