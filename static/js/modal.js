function abrir_modal(url){
    var $ = jQuery.noConflict();
    $('#ventana_modal').load(url, function(){
        $(this).modal('show');
    });
}