// Mobile Menu Toggle
const menuBtn = document.getElementById("menu-btn");
const mobileMenu = document.getElementById("mobile-menu");

menuBtn.addEventListener("click", () => {
  mobileMenu.classList.toggle("hidden");
});


function openModal(id) {
  document.getElementById(id).classList.remove("hidden");
  document.getElementById(id).classList.add("flex");
}

function closeModal(id) {
  document.getElementById(id).classList.add("hidden");
  document.getElementById(id).classList.remove("flex");
}



