
const container = document.querySelector(".container-preload");
const testbtn = document.querySelector("#testbtn");

window.addEventListener("load", () =>{
  container.classList.add("finished");
});

testbtn.addEventListener("click", () =>{
  container.classList.remove("preload-finished");
});