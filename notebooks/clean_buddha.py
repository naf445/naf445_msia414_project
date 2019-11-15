# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.2.4
#   kernelspec:
#     display_name: text-analytics
#     language: python
#     name: text-analytics
# ---

import re

with open('../data/buddha.txt', 'r') as file:
    x = file.readlines()

x[:5]

x = [line for line in x if line!='\n' ]

test = x[:5]
test

regex = re.compile(r" +\d\n$", re.IGNORECASE)
x = [regex.sub('\n', line) for line in x]

test = x[:5]
test

with open("../data/buddha_clean.txt", "w") as output:
    output.writelines(x)


