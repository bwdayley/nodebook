var hitCount=0;
function timerHit(){
  hitCount += 1;
  console.log("Timer Tick " + hitCount);
  setTimeout(timerHit, 100);
}
function factorHit(factor){
  hitCount = factor*hitCount;
  console.log("Factor Tick " + hitCount);
  setTimeout(factorHit, 500, factor);
}
function intervalHit(){
  hitCount = 1;
  console.log("Interval Tick " + hitCount);
}
setTimeout(timerHit, 100);
setTimeout(factorHit, 500, 5);
setInterval(intervalHit, 2000);

