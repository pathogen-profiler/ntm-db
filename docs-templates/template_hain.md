---

---
{% set data = get_data('SPECIES') %}

# {{ data['variables']['species'] }}


## General information

Key | value
------- | --------
Species | {{ data['variables']['species'] }}
Reference sequence accession | {{ data['reference_accession'] }}
Subspecies detection  | {{ data['subspecies_detection'] }}
Resistance detection  | {{ data['resistance_detection'] }}

## Subspecies detection

The following subspecies are detected:

{% for s in data['subspecies'] %}
* {{ s }}
{% endfor %}

## Drug resistance

Drug resistance is detected for: 
{% for d in data['variables']['drugs'] %}
* {{ d }}
{% endfor %}

## Genes of interest
Gene | Drug | Literature
------------ | ------------- | ------------- 
{%- for row in data['gene_watchlist'] %}
{{ row.Gene }} | {{ row.drug }} | {{ row.literature }}
{%- endfor %}



## Resistance mechanisms
Gene | Mutation | Type | Drug  | Literature | E.coli numbering | In Hain LPA | Comment
------------ | ------------- | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ 
{%- for row in data['mutations'] %}
{{ row.Gene }} | {{ row.Mutation }} | {{ row.type }} | {{ row.drug }} | {{ row.literature }} | {{ row.hain }} | {{ row['E.coli-nomenclature'] }} | {{ row.comment }} |

{%- endfor %}


<!-- 100% privacy friendly analytics to report back to funding agency -->
<!-- Learn more at https://docs.simpleanalytics.com/what-we-collect -->
<script async defer src="https://scripts.simpleanalyticscdn.com/latest.js"></script>
<noscript><img src="https://queue.simpleanalyticscdn.com/noscript.gif" alt="" referrerpolicy="no-referrer-when-downgrade" /></noscript>
