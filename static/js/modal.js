$(document).ready(function () {
window.setTimeout(function() {
    $(".alert").fadeTo(700, 0).slideUp(350, function(){
        $(this).remove();
    });
}, 5000);

});

function abrir_modal(url, id){
    $(id).load(url, function(){
        $(this).modal('show');
    });

}
function ocultar(id, valores){
$('#mostrar' + id).on('click', function(){
    if ($(this).hasClass('active')){
        $(this).removeClass('active');
        $('tr.' + valores).hide();
    }
    else{
        $(this).addClass('active');
        $('tr.' + valores).show();
    }
});
}

