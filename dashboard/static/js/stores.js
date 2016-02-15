$(document).ready(function () {

    $('#datatable-stores').DataTable({
        "data": storesData,
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