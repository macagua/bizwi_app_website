$(document).ready(function(){
    $('#datatable-brands').DataTable();

/*
    var urlLang = "https://cdn.datatables.net/plug-ins/1.10.6/i18n/English.json";
    if (lang == 'es') {
        urlLang = "https://cdn.datatables.net/plug-ins/1.10.6/i18n/Spanish.json";
    }

    $('#datatable-brands').DataTable({
        "data": bransData,
        "oLanguage": {
            "sUrl": urlLang
        },
        "aoColumnDefs": [

            {"aTargets": [0],
                "mData": function (source, type, full) {
                    return source.first_name
                }
            },

            {"aTargets": [1],
                "mData": function (source, type, full) {
                    return source.last_name
                }
            },

            {"aTargets": [2],
                "mData": function (source, type, full) {
                    return source.location['name']
                }
            },

            {"aTargets": [3],
                "mData": function (source, type, full) {
                    return source.username
                }
            },

            {"aTargets": [4],
                "mData": function (source, type, full) {
                    return source.email
                }
            },

        ],

        "fnRowCallback": function (nRow, aData, iDisplayIndex, iDisplayIndexFull) {
            $(nRow).click(function () {
                var id = aData.id;
                window.location.href = url_employee + id;
            });
        }

    });
*/
});