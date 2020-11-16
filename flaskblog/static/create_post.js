$(document).ready(function(){
    $('input[type="file"]').change(function(e){
        var fileName = e.target.files[0].name;
        $("#upload_label").remove();
        $('<div class="upload-label-selected"></div>').insertAfter($(".input-field"));
        $('.upload-label-selected').append("<p>"+fileName+"<p>");
        $('.upload-label-selected').append('<i class="fas fa-check"></i>');
    });
});

const fields = {
    csrf_token: {
        input: $('#csrf_token')
    },
    training_title: {
        input: $('#add-post-title')
    },
    training_image: {
        input: $('training_image')
    }
}

//Sends input to Server to Validate
$(document).ready(function() {

    $('form').on('submit', function(event) {

        var form_data = new FormData( $('.add-post-form')[0]);

        $.ajax({
            url : '/process',
            type : 'POST',
            dataType: 'json',
            cache : false,
            contentType: false,
            processData: false,
            data : form_data,
            success: function (response) {
                swal({
                    icon: "success",
                    title: "Erledigt",
                    text: "Dein Training wurde erfolgreich eingereicht",
                }).then(function() {
                    window.location.assign("/dashboard");
                })
            },
            error: function(response) {
                var result = response.responseJSON;
                //alert(result.responseJSON["datatype"]);
                Swal.fire({
                    icon: 'error',
                    title: 'Üngültiges Foto',
                    text: "Der Datentyp "+ "<b>"+result['datatype']+"</b>"+ " ist nicht zulässig",
                  }).then(function() {
                    window.location.assign("/post/new");
                })
            } 
        })

        event.preventDefault();
    });
});
