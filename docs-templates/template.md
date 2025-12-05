---
hide:
    toc: true
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
{{ row.Gene }} | {{ row.drug }} | [{{ row.literature }}](https://doi.org/{{ row.literature }})
{%- endfor %}


{% if data['resistance_detection'] == "Yes" %}

## Resistance mechanisms


<table id="resistance-table">
<thead>
    <tr>
    {%- for c in get_resistance_table_headers('SPECIES') %}
    <th>{{ c }}</th>
    {%- endfor %}
    </tr>
</thead>
<tbody></tbody>
</table>

<link href="https://cdn.datatables.net/v/dt/jq-3.7.0/jszip-3.10.1/dt-2.1.7/b-3.1.2/b-colvis-3.1.2/b-html5-3.1.2/date-1.5.4/sb-1.8.0/datatables.min.css" rel="stylesheet">

<script src="https://cdn.datatables.net/v/dt/jq-3.7.0/jszip-3.10.1/dt-2.1.7/b-3.1.2/b-colvis-3.1.2/b-html5-3.1.2/date-1.5.4/sb-1.8.0/datatables.min.js"></script>  

<script>
$(document).ready(function() {
    data = {{ get_resistance_table_rows('SPECIES') }}
    console.log('test')

    $('#resistance-table').DataTable({
    data: data,
    columnDefs: [
        // { targets: [0, 1, 2, 3], visible: true},
        { targets: '_all', visible: true }
    ],
    layout: {
        //   top1: 'searchBuilder',
        topStart: {
            buttons: [
                {
                    extend: 'colvis',
                    postfixButtons: ['colvisRestore']
                },
                {
                    extend: 'excelHtml5',
                    autoFilter: true,
                    sheetName: 'Exported data'
                }
            ]
        }
    }
    });
});

</script>
{% endif %}


<!-- 100% privacy friendly analytics to report back to funding agency -->
<!-- Learn more at https://docs.simpleanalytics.com/what-we-collect -->
<script async defer src="https://scripts.simpleanalyticscdn.com/latest.js"></script>
<noscript><img src="https://queue.simpleanalyticscdn.com/noscript.gif" alt="" referrerpolicy="no-referrer-when-downgrade" /></noscript>
