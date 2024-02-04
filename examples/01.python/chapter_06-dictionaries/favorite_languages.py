favorite_languages = {
      'ali': ['python', 'rust'],
      'sarah': ['c'],
      'samir': ['rust', 'go'],
      'fatima': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")