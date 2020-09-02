# 7.3.1 Create some sets to work with
lunch = {'sandwich', 'pasta', 'pizza', 'curry'}
dinner = {'pasta', 'stir fry', 'curry', 'pie'}

# 7.3.2 Add 'rice' to dinner
dinner.add('rice')
dinner

# 7.3.3 Add 'wrap' and 'soup' to lunch
lunch.update(['wrap', 'soup'])
lunch

# 7.3.4 Add 2 sets to another
meals = {'eggs'}
meals.update(lunch, dinner)
meals

# 7.3.5 Remove the 'pie' from dinner. You need something more nutritious
dinner.remove('pie')
dinner

# 7.3.6 We cannot decide what's for lunch. Have python pick something at random
todays_lunch = lunch.pop()
todays_lunch

# 7.3.7 What is in lunch, but not dinner?
lunch.difference(dinner)

# 7.3.8 What is in both lunch and dinner?
dinner.intersection(lunch)

# 7.3.9 What is in either lunch or dinner?
dinner.union(lunch)
