
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

const fields = {
    csrf_token: {
        input: $('#csrf_token')
    },
    username: {
        input: $('#sign-up-username')
    },
    email: {
        input: $('#sign-up-email')
    },
    password: {
        input: $('#sign-up-password')
    },
    confirmpassword: {
        input: $('#sign-up-password-confirm')
    }
}

//Sends input to Server to Validate registration
$(document).ready(function() {

    $('#register_form').on('submit', function(event) {

        var form_data = new FormData( $('#register_form')[0]);

        $.ajax({
            url : '/view/register',
            type : 'POST',
            dataType: 'json',
            cache : false,
            contentType: false,
            processData: false,
            data : form_data,
            success: function (response) {
                Swal.fire({
                    icon: "success",
                    title: "Erledigt!",
                    text: "Bitte logge dich ein"
                }).then(function() {
                    container.classList.remove("sign-up-mode");
                })
            },
            error: function(response) {
                var result = response.responseJSON;
                var html = $("<ul />");
                if (typeof result['username'] !== 'undefined'){
                    html.append("<li>"+result['username']+"</li>");
                }
                if (typeof result['email'] !== 'undefined'){
                    html.append("<li>"+result['email']+"</li>");
                }
                if (typeof result['password'] !== 'undefined'){
                    html.append("<li>"+result['password']+"</li>");
                }
                if (typeof result['confirmPassword'] !== 'undefined'){
                    html.append("<li>"+result['confirmPassword']+"</li>");
                }
                Swal.fire({
                    icon: 'error',
                    html: html
                  })
            } 
        })

        event.preventDefault();
    });
});

//Sends input to Server to Validate login
$(document).ready(function() {

    $('.sign-in-form').on('submit', function(event) {

        var form_data = new FormData( $('.sign-in-form')[0]);

        $.ajax({
            url : '/view/login',
            type : 'POST',
            dataType: 'json',
            cache : false,
            contentType: false,
            processData: false,
            data : form_data,
            success: function (response) {
                window.location.assign("/dashboard");
            },
            error: function(response) {
                Swal.fire({
                    icon: 'error',
                    title: "Ungültig!",
                    text: 'Bitte Überprüfe deine Eingabe'
                  })
            } 
        })

        event.preventDefault();
    });
});


