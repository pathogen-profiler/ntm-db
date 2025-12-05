---
hide:
  - toc
---


# Species

To facilitate species detection a database of sequences has been created for use with NTM-Profiler. The following table summarizes the species and accessions included in the NTM-DB. To make sure your species is detected by NTM-Profiler, please check that your species is listed here.

<table>
  <thead>
    <tr>
    {%- for c in get_species_table_headers() %}
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
    data = {{ get_species_table_rows() }}
    console.log('test')

    $('table').DataTable({
      data: data,
      columnDefs: [
        { targets: [0, 1, 2, 3], visible: true},
        { targets: '_all', visible: false }
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

<script async defer src="https://scripts.simpleanalyticscdn.com/latest.js"></script>
<noscript><img src="https://queue.simpleanalyticscdn.com/noscript.gif" alt="" referrerpolicy="no-referrer-when-downgrade" /></noscript>