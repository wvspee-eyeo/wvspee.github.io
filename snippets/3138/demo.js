document.getElementById('load_iframe_working').addEventListener("click", event =>
{
  document.getElementById('iframe_working').src = "iframe.html";
  
});

document.getElementById('load_iframe_broken').addEventListener("click", event =>
{
  var doc = document.getElementById('iframe_broken').contentWindow.document;
  doc.addEventListener('contextmenu', (event) => {console.log('4', event);});
  doc.open();
  doc.write("<html><head><title>foo</title></head><body><p>Now broken</p><img src='abp.png' /></body></html>");
  doc.close();
});

document.addEventListener("load", event => { console.log('load'); });
document.getElementById('iframe_working').addEventListener("load", event => { console.log('load'); });
document.getElementById('iframe_broken').addEventListener("load", event => { console.log('load'); });
