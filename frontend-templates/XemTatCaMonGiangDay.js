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
                { data: 'SiSo' },
                { data: 'LichThi' }

            ]
        });
    }
$(document).ready(function (){
    initTableData();
    $("#list-header").on({
    });
});