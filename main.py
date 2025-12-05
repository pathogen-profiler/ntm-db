"""
Basic example of a Mkdocs-macros module
"""


from fileinput import filename
import yaml
import json
import csv
import os

def get_genome_sequence_id(filename):
    for l in open(filename):
        if l.startswith(">"):
            return l[1:].split()[0]


def load_specific_csv(filename):
    rows = []
    columns = set(['comment'])
    if os.path.isfile(filename)==False:
        return rows
    for row in csv.DictReader(open(filename)):

        columns.update(list(row))
        rows.append(row)

    for row in rows:
        for c in columns:
            if c not in row:
                row[c] = ''
    return rows

def get_subspecies_from_barcode(filename):
    subspecies = set()
    if os.path.isfile(filename):
        for l in open(filename):
            row = l.strip().split('\t')
            if row[3].startswith('subsp.'):
                subspecies.add(row[3])
    
    return sorted(list(subspecies))

def define_env(env):
    """
    This is the hook for defining variables, macros and filters

    - variables: the dictionary that contains the environment variables
    - macro: a decorator function, to declare a macro.
    - filter: a function with one of more arguments,
        used to perform a transformation
    """

    @env.macro
    def get_data(species):
        base_dir = env.project_dir+f"/db/{species}/"
        data = {}
        data['reference_accession'] = get_genome_sequence_id(base_dir + "genome.fasta")
        data['variables'] = json.load(open(base_dir + 'variables.json'))
        data['gene_watchlist'] = load_specific_csv(base_dir + 'gene_watchlist.csv')
        data['mutations'] = load_specific_csv(base_dir + 'variants.csv')
        data['subspecies'] = get_subspecies_from_barcode(base_dir + 'barcode.bed')
        data['subspecies_detection'] = 'Yes' if len(data['subspecies'])>0 else 'No'
        data['resistance_detection'] = 'Yes' if ('drugs' in data['variables'] and len(data['variables']['drugs'])>0) else 'No'
        return data

    @env.macro
    def get_species_db_data(species):
        data = {}
        data['variables'] = json.load(open(env.project_dir+f"/db/species/variables.json"))
        return data

    @env.macro
    def get_front_matter(f):
        page_text = [x for x in open(f).readlines()]
        bounds = [i for i in range(len(page_text)) if page_text[i].strip()=="---"]
        data = yaml.safe_load("\n".join(page_text[bounds[0]+1:bounds[1]]))
        return data
    
    @env.macro
    def get_species_table_headers():
        filename1 = env.project_dir + '/db/species/accessions.csv'
        filename2 = env.project_dir + '/db/species/taxonomy.csv'
        reader1 = csv.DictReader(open(filename1))
        headers = reader1.fieldnames
        reader2 = csv.DictReader(open(filename2))
        for h in reader2.fieldnames:
            if h not in headers:
                if h=='gtdb_species':
                    continue
                headers.append(h)
        return headers
    
    @env.macro
    def get_species_table_rows():
        headers = get_species_table_headers()
        filename1 = env.project_dir + '/db/species/accessions.csv'
        filename2 = env.project_dir + '/db/species/taxonomy.csv'
        taxonomy_data = {}
        for row in csv.DictReader(open(filename2)):
            taxonomy_data[row['gtdb_species']] = {k: v for k, v in row.items() if k != 'gtdb_species'}
        data = []
        for row in csv.DictReader(open(filename1)):
            row.update(taxonomy_data.get(row['species'],{}))
            for c in headers:
                if c not in row:
                    row[c] = ''
            data.append(list(row.values()))


        return json.dumps(data)
    
    @env.macro
    def get_resistance_table_headers(species):
        filename1 = env.project_dir + f'/db/{species}/variants.csv'
        reader1 = csv.DictReader(open(filename1))
        headers = reader1.fieldnames
        return headers
    
    @env.macro
    def get_resistance_table_rows(species):
        filename1 = env.project_dir + f'/db/{species}/variants.csv'
        data = []
        for row in csv.DictReader(open(filename1)):
            data.append(list(row.values()))
            print(row)

        print(data)
        return json.dumps(data)