const test = "test"
var url = "https://raw.githubusercontent.com/goshva/moneyTracker/main/docs/stat.json"
var all_count = document.getElementById('all_count')
var double = document.getElementById('double')
var tracker = document.getElementById('tracker')
async function logMovies() {
    const response = await fetch(url);
    const movies = await response.json();
    all_count.innerText=`Общее количество фото: ${movies.all_count}`;
    double.innerText=`Количество дубликатов: ${movies.double}`;
    tracker.innerText=`Отслеживаемые траектории перемещения: ${movies.tracker}`;



  }
logMovies()