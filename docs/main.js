const test = "test"
var url = "https://raw.githubusercontent.com/goshva/moneyTracker/main/docs/stat.json"
var statistic = document.getElementById('statistic')
async function logMovies() {
    const response = await fetch(url);
    const movies = await response.json();
    console.log(`Fifteen is ${movies.all_count} and not ${url}.`);
    console.log(movies.all_count);
    statistic.innerText=`Всего фотографий в нашем боте: ${movies.all_count}, дубликатов фотографий: ${movies.double}.`
  }
logMovies()