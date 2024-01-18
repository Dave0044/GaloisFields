
$(document).ready(function() {
    $('form').submit(function(event) {
        event.preventDefault();

        // Obtener el formulario y el botón
        var form = $(this);
        var submitButton = form.find('button[type="submit"]');

        // Deshabilitar el botón mientras se procesa la solicitud
        submitButton.prop('disabled', true);

        // Realizar la solicitud AJAX
        $.ajax({
            type: form.attr('method'),
            url: form.attr('action'),
            data: form.serialize(),
            success: function(response) {
                console.log('Success:', response);
                // Actualizar solo la parte de la página que deseas
                $('#resultado').text(response.resultado);
            },
            error: function(error) {
                console.log('Error:', error);
            },
            complete: function() {
                // Habilitar el botón después de que se completa la solicitud
                submitButton.prop('disabled', false);
            }
        });
    });
});
