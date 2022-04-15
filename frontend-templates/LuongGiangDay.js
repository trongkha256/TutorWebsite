var table;
function initTableData() {
    var data=[


    ];
    table = $('#luong').DataTable(
        {
            "processing": true,
            data,
            colums:[
                { data: 'TenMonHoc' },
                { data: 'MaMon' },
                { data: 'Lop' },
                { data: 'NgayHoc' },
                { data: 'SoTien' },
                { data: 'TrangThai' }

            ]
        });
    }
$(document).ready(function (){
    initTableData();
    $("#list-header").on({
    });
});