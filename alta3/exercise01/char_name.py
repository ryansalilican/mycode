#!/usr/bin/env python3

print("Welcome to Marvel Heroes of the Day!")
char_name= input("Which character do you want to know aboout? Starlord, Mystique, or Hulk?\n>")
char_stat= input("What statistic do you want to know about? Their real name, powers, or archenemy?\n>")
marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }
print("Here is the info! " + char_name + "'s" + char_stat + " is " + marvelchars([char_name][char_stat]))

