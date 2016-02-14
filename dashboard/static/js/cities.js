$(document).ready(function () {

    var urlLang = "//cdn.datatables.net/plug-ins/1.10.6/i18n/English.json";
    if (lang == 'es') {
        urlLang = "//cdn.datatables.net/plug-ins/1.10.6/i18n/Spanish.json";
    }

    $('#cities_tb').DataTable({
        "data": bransData,
        "oLanguage": {
            "sUrl": urlLang
        },
        "aoColumnDefs": [

            {"aTargets": [0],
                "mData": function (source, type, full) {
                    return source.city_name
                }
            },

            {"aTargets": [1],
                "mData": function (source, type, full) {
                    return source.country
                }
            },

        ],

        "fnRowCallback": function (nRow, aData, iDisplayIndex, iDisplayIndexFull) {
            $(nRow).click(function () {
                var id = aData.id;
                window.location.href = url_cities + id;
            });
        }

    });

});