import csv
with open('data/pokemon.csv', newline='', encoding="utf-8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=']', quotechar='|')
    for row in spamreader:
        abilities = []
        addingAbilities = True
        print('pokemon abilities:')
        for i in row:
            if addingAbilities:
                newAbility = i.split("'")
                print(newAbility)
                # abilities.append(newAbility)
            
            if ']' in i:
                addingAbilities = False

        print(abilities)