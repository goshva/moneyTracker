const test = "test"
var url = "https://raw.githubusercontent.com/goshva/moneyTracker/main/docs/stat.json"
var all_count = document.getElementById('all_count')
var double = document.getElementById('double')
var tracker = document.getElementById('tracker')
var recognize = document.getElementById('recognize')
var no_recognize = document.getElementById('no_recognize')
async function logMovies() {
    const response = await fetch(url);
    const movies = await response.json();
    all_count.innerText=`Общее количество фото: ${movies.all_count}`;
    double.innerText=`Количество дубликатов: ${movies.double}`;
    tracker.innerText=`Отслеживаемые траектории перемещения: ${movies.tracker}`;
    recognize.innerText=`Переименованные фото: ${movies.recognize}`;
    no_recognize.innerText=`Не переименованные фото: ${movies.not_recognize}`;





  }
/*

    //
function feedback(action, status) {
  let token = "6622721325:AAHEIdpX7ebarUybQOP-Vkjzt_fWHFhrpo8"; 
  //use this for testing
  //let chat_id = "190404167";
  //let chat_id = "1329475336";//Aram ID
  //use this for production
  let chat_id = "-915348868";
  let user_phone = prompt('Введите телефон для контакта с вами');
  var msg = `${action} от ${user_phone}`;// from ${getCookie("@")}`;
  var url = `https://api.telegram.org/bot${token}/sendMessage?chat_id=${chat_id}&text=${msg}&parse_mode=html`;

  if (user_phone !== "" && user_phone !== null) {
    fetch(url)
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        alert(`Благодарим за  заказ «${action}».\nСейчас ответственный свяжется с вами`)
        window.location.href = "/#menu";
      });
  }
  else { console.log(' no null')}

  }
  document.querySelector('.lead').click(
    function () { this.addEventListener("click", feedback(this.innerHTML)) }
  );
*/
logMovies() 
