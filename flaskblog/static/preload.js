
const container = document.querySelector(".container-preload");
const topcontainer = document.querySelector(".top-container");

const infobutton = document.createElement("i");
infobutton.classList.add("fas");
infobutton.classList.add("fa-info");
infobutton.classList.add("fa-2x");


window.addEventListener("load", () =>{
  container.classList.add("finished");
});
container.addEventListener("transitionend", () =>{
  topcontainer.appendChild(infobutton);
})
