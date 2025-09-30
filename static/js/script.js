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

// (function () {
//   emailjs.init("UEwG4jSXgJOjd14un"); // replace with your public key from EmailJS
// })();

// document.addEventListener("DOMContentLoaded", function () {
//   const form = document.getElementById("contact-form");

//   if (form) {
//     form.addEventListener("submit", function (event) {
//       event.preventDefault();

//       emailjs.sendForm("service_af1uun8", "template_ghrcm5n", form).then(
//         () => {
//           alert("Message sent successfully ✅");
//         },
//         (error) => {
//           console.error("Failed to send message ❌", error);
//           alert("Oops! Something went wrong.");
//         }
//       );
//     });
//   }
// });

// function sendMail() {
//   let parms = {
//     name : document.getElementById("name").value,
//     email : document.getElementById("email").value,
//     subject: document.getElementById("subject").value,
//     message : document.getElementById("message").value
//   }

//   emailjs.sendForm("service_1tcv6fj", "service_1tcv6fj", parms).then(alert("Message sent successfully ✅"));
// }

// (function () {
//   emailjs.init("UEwG4jSXgJOjd14un"); // replace with your public key from EmailJS
// })();
// document.addEventListener("DOMContentLoaded", function () {
//   const form = document.getElementById("contact-form");

//   if (form) {
//     form.addEventListener("submit", function (event) {
//       event.preventDefault();

//       emailjs.sendForm("service_1tcv6fj", "template_ghrcm5n", form).then(
//         () => {
//           alert("Message sent successfully ✅");
//         },
//         (error) => {
//           console.error("Failed to send message ❌", error);
//           alert("Oops! Something went wrong.");
//         }
//       );
//     });
//   }
// });
