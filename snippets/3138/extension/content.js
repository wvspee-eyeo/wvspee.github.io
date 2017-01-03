let clickHandler = function(event)
{
   console.log('click');
};

window.setInterval(event => {
  console.log('reconnecting');
  document.removeEventListener('click', clickHandler);
  document.addEventListener('click', clickHandler);
}, 10000);

document.addEventListener('click', clickHandler);
