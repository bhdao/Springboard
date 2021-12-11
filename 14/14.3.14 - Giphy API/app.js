console.log("Let's get this party started! 🎊");
const gifOutput = document.getElementById("gifOutput");
const buttons = {
  search: document.getElementById("searchBtn"),
  reset: document.getElementById("resetBtn")
}

const gifSearchTerm = document.querySelector("#gifSearchTerm");
const numGuests = document.querySelector("#numGuests");

let numCurrentGifs = 0;

//If there are gifs, remove the landing message. If none, replace the landing message
const houseKeeping = () => {
  let welcomeMessage = document.querySelector("#welcomeMessage");
  if (numCurrentGifs > 0) {
    welcomeMessage.style.visibility = "hidden";
  } else if (numCurrentGifs <= 0) {
    welcomeMessage.style.visibility = "visible";
  }
  console.log("HouseKeeping function run")
}

//Event delegation on the page's form
gifForm.addEventListener("click", (e) => {
  e.preventDefault();
  if (e.target.id == "searchBtn") {
    if (+numGuests.value == "") {
      window.alert("Please indicate the number of guests you would like to invite!")
      numGuests.focus();
      return
    }
    const key = "NSGtypMfvEuDs3r2iEjnk4DcyWTvd4Z5";
    inviteGIFs(key);
  } else if (e.target.id == "resetBtn") {
    clearGifs();
  }
});


// Adds hover events to the buttons 🛸
// (Start) Fancy button interaction handlers //
const randomEmoji = (type, place) => {
  const emojis = {
    search: ["🎊", "🎉", "🎂", "🎈", "🥳"],
    reset: ["❌", "👋", "💥", "😱", "🚮"],
  };
  const randNum = Math.floor(Math.random() * 5);
  if (place == "header") {
    return emojis[type][randNum];
  } else {
    return (
      emojis[type][randNum] +
      emojis[type][randNum] +
      emojis[type][randNum]
    );
  }
}

buttons.search.addEventListener("mouseenter", () => {
  buttons.search.textContent = randomEmoji("search");
});

buttons.search.addEventListener("mouseleave", () => {
  buttons.search.textContent = "Search"
});

buttons.reset.addEventListener("mouseenter", () => {
  buttons.reset.textContent = randomEmoji("reset");
});

buttons.reset.addEventListener("mouseleave", () => {
  buttons.reset.textContent = "Clear"
});
// (End) Fancy button interaction handlers //


//get request to giphy API, appends returned GIF to DOM
async function searchGif(key) {
  console.log("%csearchGif run", "color: rgb(81, 197, 81)");
  let searchTerm = gifSearchTerm.value.toString();

  try {
    let res = await axios.get("http://api.giphy.com/v1/gifs/random", { params: { api_key: key, tag: searchTerm, rating: "g" } });
    let gifURL = res.data.data.images.fixed_height.url;
    let gif = document.createElement("img");
    gif.src = gifURL;
    gifOutput.appendChild(gif);
    numCurrentGifs++;
    houseKeeping();
  } catch (error) {
    console.log("Something went wrong!");
    console.log(error);
  }

};

//Wipes the gifs from the DOM
const clearGifs = () => {
  console.log("%cclearGifs run", "color: red");
  gifOutput.innerHTML = "";
  numCurrentGifs = 0;
  houseKeeping();
};

//Runs searchGif according to inputted number
const inviteGIFs = (key) => {
  if (+numGuests.value > 4) {
    numGuests.value = 4;
  } else if (+numGuests.value < 0) {
    numGuests.value = 0;
  };
  let numInvites = +numGuests.value;

  for (let i = 0; i < numInvites; i++) {
    searchGif(key);
  }
};

// Randomly changes the emoji in the page header 🎉
const headerEmojiLoop = setInterval(
  function () {
    document.querySelector("#headerEmoji").textContent = randomEmoji("search", "header");
  }
  , 2000)