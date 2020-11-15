$(document).ready(function(){
    $('input[type="file"]').change(function(e){
        var fileName = e.target.files[0].name;
        $("#upload_label").remove();
        $('<div class="upload-label-selected"></div>').insertAfter($(".input-field"));
        $('.upload-label-selected').append("<p>"+fileName+"<p>");
        $('.upload-label-selected').append('<i class="fas fa-check"></i>');
        swal("Good job!", "You clicked the button!", "success");
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

        $.ajax({
            data : {
                csrf_token: $('#csrf_token').val(),
                training_title: $('#add-post-title').val(),
                training_image: $('#training_image').val()
            },
            type : 'POST',
            url : '/process'
        })
        .done(function(data) {

            if (data.ok) {
                swal("OK", "Success");
            }

            else {
                swal(data[0]);
            }
        });

        event.preventDefault();
    });
});
