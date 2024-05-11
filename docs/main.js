const test = "test"
var url = "https://raw.githubusercontent.com/goshva/moneyTracker/main/stat.json"
var statistic = document.getElementById('statistic')
async function logMovies() {
    const response = await fetch(url);
    const movies = await response.json();
    console.log(`Fifteen is ${movies.all_count} and not ${url}.`);
    console.log(movies.all_count);
    statistic.innerText=`Fifteen is ${movies.all_count} and not ${url}.`
  }
logMovies()