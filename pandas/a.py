import pandas as pd
from tabulate import tabulate

def pp(df):
    print(tabulate(df, headers='keys', tablefmt='psql'))

age = pd.DataFrame([{'person': 'Joel', 'age': 42}, {'person': 'Ann', 'age': 41}, {'person': 'Bob', 'age': 20}])

pp(age)
age = age.set_index('person')
age['age'] /= 100
# age.name = 'AGE'
pp(age)

house = pd.DataFrame([{'person': 'Joel', 'house': 620}, {'person': 'Ann', 'house': 103}])

house = house.set_index('person')
#house.name = 'HOUSE'

all = pd.concat([age, house], axis=1)
all = all.fillna(0)

new_index = [f"new {f}" for f in all.index]
all.index = new_index

all = all.sort_index()

pp(all)

o = all.iloc[1].to_dict()  # selects row
# o.pop('age')  # remove key
o = pd.DataFrame(o, index=[''])
pp(o)


all = pd.concat([o, all])
pp(all)

sub = all.iloc[0] - all
sub.iloc[0] = all.iloc[0]
pp(sub)
