$(document).ready(function () {
    $('#datatable-employees').DataTable({
        "data": employeesData,
        "aoColumnDefs": [

            {
                "aTargets": [0],
                "mData": function (source, type, full) {
                    return source.first_name
                }
            },

            {
                "aTargets": [1],
                "mData": function (source, type, full) {
                    return source.last_name
                }
            },

            {
                "aTargets": [2],
                "mData": function (source, type, full) {
                    return source.last_name
                }
            },

            {
                "aTargets": [3],
                "mData": function (source, type, full) {
                    return source.username
                }
            },

            {
                "aTargets": [4],
                "mData": function (source, type, full) {
                    return source.email
                }
            }

        ]

    });

});