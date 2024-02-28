$('document').ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  $('input#btn_translate').click(function () {
    $.get(url + $.param({ lang: $('input#language_code').val() }), function (data) {
      $('DIV#hello').html(data.hello);
    });
  });
});
