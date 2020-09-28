// Define Variables for Post Request
const signup_form = document.getElementById('register_form');
const successMessage = document.getElementById('success-message');
const errorcontainer = document.querySelector(".error-container");
const fields = {
    csrf_token:{
        input: document.querySelector('#csrf_token'),
    },
    username: {
        input: document.getElementById('sign-up-username'),
    },
    email: {
        input: document.getElementById('sign-up-email'),
    },
    password: {
        input: document.getElementById('sign-up-password'),
    },
    password_confirm: {
        input: document.getElementById('sign-up-password-confirm'),
    }
}
// Variables to turn off/on the Signup-Mode
const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});

//Sends Input to Server for Validation
signup_form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const response = await fetch('/view', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            
            csrf_token: fields.csrf_token.input.value,
            username: fields.username.input.value,
            email: fields.email.input.value,
            password: fields.password.input.value,
            confirmPassword: fields.password_confirm.input.value
        })
    });
    // If Server returns ok deactivate signup-mode and display success message
    if (response.ok) {
        errorcontainer.innerHTML = await response.text();
        container.classList.remove("sign-up-mode");
        errorcontainer.classList.remove("is-invalid")

    // Else display errors
    } else {
        const errors = await response.json();
        Object.keys(errors).forEach((key) => {
            var node = document.createElement("LI");
            var textnode = document.createTextNode(errors[key]);
            node.appendChild(textnode);
            document.getElementById("error-list").appendChild(node);
            
        });
    }
});









