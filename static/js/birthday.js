$(function()
{
  var flame = $('#flame');
  var txt = $('h1');

  flame.on(
  {
    click: function()
    {
      flame.removeClass('burn').addClass('puff');
      $('.smoke').each(function()
      {
        $(this).addClass('puff-bubble');
      });
      $('#glow').remove();
      txt.html("Felices <b>21 años</b> Mi nalgona hermosa, la amoooo").delay(10000).fadeOut(300);
      $('#candle').animate(
      {
        //'opacity': '.5'
      }, 10000);
    }
  })   
});