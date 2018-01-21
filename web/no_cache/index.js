
function obtenerNoticias(){
    $.get( '/api/noticias_top/no_cache', function( data ) {
        
        var divArticulos = $('#articulos');

        $.each(data, function( index, articulo ) {
        var divAr = $('<div/>').addClass('col s6').appendTo(divArticulos);
        var title = $('<h5/>').addClass('center').text(articulo.titulo).attr('id', 'titulo').appendTo(divAr);
        var descr = $('<p/>').addClass('light').text(articulo.subtitulo).attr('id', 'descripcion').appendTo(divAr);
        var butt  = $('<a/>').addClass('center waves-effect waves-light light-blue btn modal-trigger ').text("Read More...").attr('onClick','abrirModal(this)').attr('href','#modal1').appendTo(divAr);
        var arti = $('<p/>').addClass('light').text(articulo.articulo).attr('id', 'articulo').hide().appendTo(divAr);
        var space = $('<br/>').appendTo(divAr);
        //$('<br/>').appendTo(divArticulos);
        });

      });

}

function abrirModal(data){
    var parent= $(data).parent();
    var modal= $('.modal-content');
    var title = $('<h5/>').addClass('center').text(parent.find("#titulo").text()).appendTo(modal);
    var descr = $('<p/>').addClass('light').text(parent.find("#descripcion").text()).appendTo(modal);
    var arti = $('<p/>').addClass('light').text(parent.find("#articulo").text()).appendTo(modal);

}

$(document).ready(function(){
    // the "href" attribute of the modal trigger must specify the modal ID that wants to be triggered
    $('.modal').modal({
        complete: function() { $('.modal-content').empty(); }
    });
    obtenerNoticias();
  });

