var table;
function initTableData() {
    var data=[
        {
            "TenMonHoc": "Nhập Môn Lập Trình",
            "MaMon": "sasas",
            "Lop": "asasas",
            "NgayHoc": "asasas",
            "HocPhi": "sasasas",
            "TrangThai":"asasas",
        },
        {
            "TenMonHoc": "Nhập Môn Lập Trình",
            "MaMon": "sasas",
            "Lop": "asasas",
            "NgayHoc": "asasas",
            "HocPhi": "sasasas",
            "TrangThai":"asasas",
        }

    ];
    table = $('#HocPhi').DataTable(
        {
            "processing": true,
            data,
            colums:[
                { data: 'TenMonHoc' },
                { data: 'MaMon' },
                { data: 'Lop' },
                { data: 'NgayHoc' },
                { data: 'HocPhi' },
                { data: 'TrangThai' }

            ]
        });
    }
$(document).ready(function (){
    initTableData();
    $("#list-header").on({
    });
});