document.addEventListener("DOMContentLoaded", function () {
  var nombre = document.getElementById("nombre").value;
  var apellidos = document.getElementById("apellidos").value;
  var gmail = document.getElementById("gmail").value;
  var descripcion = document.getElementById("descripcion").value;
  var usuario = document.getElementById("usuario").value;

  setInterval(() => {
    var contrasena = document.getElementById("contrasena").value;
    var confirmarContrasena = document.getElementById(
      "confirmar_contrasena"
    ).value;
    var textverf = document.querySelector(".verfpaswd");
    var btnRegistro = document.querySelector(".btnregistro");

    if (contrasena != "" && confirmarContrasena != "") {
      if (contrasena === confirmarContrasena) {
        textverf.innerHTML = "Contraseña coincide";
        btnRegistro.style.display = "block";
      } else {
        textverf.innerHTML = "Contraseña NO coincide";
        btnRegistro.style.display = "none";
      }
    } else {
      textverf.innerHTML = "";
      btnRegistro.style.display = "block";
    }
  }, 500);
});
