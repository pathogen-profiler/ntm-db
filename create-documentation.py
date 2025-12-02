import os

species = [s for s in os.listdir('db') if s.startswith('Myco')]
print(species)

def check_for_hain_info(s):
    filename = f'db/{s}/variants.csv'
    if os.path.isfile(filename):
        if "hain" in open(filename).read():
            return True
    return False

template = open('docs-templates/template.md').read()
template_hain = open('docs-templates/template_hain.md').read()
for s in species:
    with open(f'docs/{s}.md',"w") as O:
        if check_for_hain_info(s):
            O.write(template_hain.replace("SPECIES",s))
        else:
            O.write(template.replace("SPECIES",s))
