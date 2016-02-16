$(document).ready(function () {
    $('#datatable-employees').DataTable({
        "data": employeesData,
        "columns": [
            { "data": "first_name"},
            { "data": "last_name"},
            { "data": "email"},
            { "data": "username"},
            { "data": "email"}
        ]

    });

});