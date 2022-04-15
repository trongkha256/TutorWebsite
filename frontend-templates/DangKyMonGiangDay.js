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
                { data: 'PhiGiangDay' },
                { data: 'DangKy' }

            ]
        });
    }
$(document).ready(function (){
    initTableData();
    $("#list-header").on({
    });
});