school = {'1a' : 33,'3a' : 29,
'4г' : 31, '5в' : 28,
'9б' : 29, '10в' : 21 , '11a' : 20,  }
print(school)
print()
school['5в'] = 26
school['9а'] = 25
print(school)
del school['4г']
print(school)
print(int(sum(school)))
