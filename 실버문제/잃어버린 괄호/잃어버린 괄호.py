import sys
import re

string = sys.stdin.readline().rstrip()

first_minus_location = string.find('-')
if first_minus_location != -1:
    positive_number = map(int, string[:first_minus_location].split('+'))
    negative_number = map(int, re.sub('[\-+]', ' ', string[first_minus_location + 1:]).split())
    print(sum(positive_number) - sum(negative_number))
else:
    positive_number = map(int, string.split('+'))
    print(sum(positive_number))