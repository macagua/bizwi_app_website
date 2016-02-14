$(document).ready(function () {

    var urlLang = "//cdn.datatables.net/plug-ins/1.10.6/i18n/English.json";
    if (lang == 'es') {
        urlLang = "//cdn.datatables.net/plug-ins/1.10.6/i18n/Spanish.json";
    }

    $('#data-table-simple').DataTable({
        "data": storesData,
        "oLanguage": {
            "sUrl": urlLang
        },
        "aoColumnDefs": [

            {"aTargets": [0],
                "mData": function (source, type, full) {
                    return source.store_name
                }
            },

            {"aTargets": [1],
                "mData": function (source, type, full) {
                    return source.country
                }
            },

            {"aTargets": [2],
                "mData": function (source, type, full) {
                    return source.city
                }
            },

            {"aTargets": [3],
                "mData": function (source, type, full) {
                    return source.address
                }
            },
            {"aTargets": [4],
                "mData": function (source, type, full) {
                    return source.categories
                }
            },
            {"aTargets": [5],
                "mData": function (source, type, full) {
                    return source.categories
                }
            }

        ],

        "fnRowCallback": function (nRow, aData, iDisplayIndex, iDisplayIndexFull) {
            $(nRow).click(function () {
                var id = aData.id;
                window.location.href = url_local + id;
            });
        }

    });

});