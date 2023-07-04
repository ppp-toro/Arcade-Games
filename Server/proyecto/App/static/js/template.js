
 
document.addEventListener('DOMContentLoaded', function() {
    var campoUsuario = document.querySelector('.user');
  
    function obtenerNombreUsuario() {
      fetch(window.location.origin + "/enviar-usuario/")
        .then((res) => res.json())
        .then((data) => {
          var nombreUsuario = data.nombre_usuario;
          campoUsuario.innerHTML = nombreUsuario;
        });
    }
    
    obtenerNombreUsuario();


})
