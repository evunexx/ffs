
const container = document.querySelector(".container-preload");
const topcontainer = document.querySelector(".top-nav");

const infobutton = document.createElement("i");
infobutton.classList.add("fas");
infobutton.classList.add("fa-info");
infobutton.classList.add("fa-2x");

const logoutbutton = document.createElement("i");
logoutbutton.classList.add("fas");
logoutbutton.classList.add("fa-sign-out-alt");
logoutbutton.classList.add("fa-2x");


window.addEventListener("load", () =>{
  container.classList.add("finished");
});
container.addEventListener("transitionend", () =>{
  topcontainer.appendChild(infobutton);
  topcontainer.appendChild(logoutbutton);
})
