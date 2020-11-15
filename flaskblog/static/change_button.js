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
