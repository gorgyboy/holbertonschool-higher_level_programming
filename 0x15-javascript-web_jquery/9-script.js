// Fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays
// the value of hello from that fetch in the HTML’s tag DIV#hello.

const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

$.getJSON(url, function (data) {
  $('#hello').text(data.hello);
});
