var table;
function initTableData() {
    var data=[


    ];
    table = $('#MakeTable').DataTable(
        {
            "processing": true,
            data,
            colums:[
                { data: 'TenMonHoc' },
                { data: 'MaMon' },
                { data: 'Lop' },
                { data: 'NgayHoc' },
                { data: 'ThoiGian' },
                { data: 'HocPhi' },
                { data: 'DangKy' }

            ]
        });
    }
$(document).ready(function (){
    initTableData();
    $("#list-header").on({
    });
});