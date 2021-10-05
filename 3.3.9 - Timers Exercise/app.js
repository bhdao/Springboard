noDecimalsAllowed = (input) => {
  let num = input.toString();
  console.log(`🔪💥🐱‍👤\nOops, you dropped this.\n${num.slice(num.indexOf("."))} \n🐱Keep the change.`)
  return parseInt(num.slice(0, num.indexOf(".")));
}

function countDown(seconds) {
  let time = seconds;
  if (typeof(time) !== "number"){console.log("That's no number..."); return};
  if (time < 0){console.log("Oh, so you're a wise guy, eh? Going up! ⬆")};
  if(time%1 !== 0) {time = noDecimalsAllowed(time);}
  const cd = setInterval(() => {
      if (time > 0) {
        console.log(time);
        time -= 1;
      } else if (time < 0) {
        console.log(time);
        time += 1;
      } else {
        clearInterval(cd);
        console.log("Done! 🎉")
      }
    }, 1000  
  );
  
};

function randomGame() {
  let count = 0;
  const game = setInterval(()=>{
    const num = Math.random();
    console.log(num)
    count += 1;
    if (num > 0.75) {
      console.log(`It took ${count} ${count > 1 ? "tries" : "try"} to get a number greater than 0.75!`)
      clearInterval(game);
    }
  }, 1000)
};