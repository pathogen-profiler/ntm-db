import os

species = [s for s in os.listdir('db') if s.startswith('Myco')]
print(species)

template = open('docs-templates/template.md').read()
for s in species:
    with open(f'docs/{s}.md',"w") as O:
        O.write(template.replace("SPECIES",s))
