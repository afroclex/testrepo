user_0 = {
		'username': 'acaffrey',
		'first': 'alex',
		'last': 'caffrey',
		}

for key, value in user_0.items():
	print(f"\nKey:{key}")
	print(f"Value: {value}")

favorite_languages = {
	'jen': 'python',
	'joe': 'c#',
	'jane': 'java',
	'john': 'c',
	}

friends = ['jane', 'john']
for name in favorite_languages.keys():
	print(f"\nHi, {name.title()}.")

	if name in friends:
		language = favorite_languages[name].title()
		print(f"\t{name.title()}, I see that you love {language}")

if 'erin' not in favorite_languages.keys():
	print("\nErin, please take the poll.")

	# .items pulls the keys and values and associates them with the variable "name" and "language"
	for name, language in favorite_languages.items():
		print(f"\nName: {name.title()}")
		print(f"Favorite language: {language.title()}\n")
	# .keys pulls all keys from dict and add them to variable "name"
	for name in favorite_languages.keys():
		print(name.title())
