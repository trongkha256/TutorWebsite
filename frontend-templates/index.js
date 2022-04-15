$(document).ready(function()
{
    $("#Navlist").on({
        mouseenter: function()
        {
            $(this).css("color","yellow");
        },
        mouseleave: function()
        {
            $(this).css("color","white");
        },
    });
});