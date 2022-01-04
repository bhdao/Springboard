def print_upper_words(words):
  for word in words:
    print(word.upper())

def print_xy_upper(words):
  for word in words:
    if word[0].lower() in "xy":
      print (word.upper())

print_upper_words(["alllowercase", "CapitalCase", "thisIsHumpCase", "lower_snake_case"])

print_xy_upper(["xylophone (lowercase x)", "jello", "yellow (lowercase y)", "Xyz (capital X)", "Yippee! (Capital Y)"])