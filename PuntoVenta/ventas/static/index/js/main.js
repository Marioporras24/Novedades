/*$( document ).ready(function() {
    // Handler for .ready() called.
    alert('Todo bien');
  });*/



function eliminarPersonal(id) {
  document.getElementById("id_personal_eliminar").value = id;
}

function editarNovedadEmpleado(idnovedadpersonal, descripcion, fecha_inicio, fechafin, codigo_empleado, idtiponovedad_personal) {
  document.getElementById("id_novedad_editar").value = idnovedadpersonal;
  document.getElementById("descripcion_editar").value = descripcion;
  document.getElementById("fecha_inicio_editar").value = fecha_inicio;
  document.getElementById("fechafin_editar").value = fechafin;
  document.getElementById("codigo_empleado_editar").value = codigo_empleado;
  document.getElementById("idtiponovedad_personal_editar").value = idtiponovedad_personal;

}

function editarEmpleado(cod_empleado, documentoidentidad, primer_nombre) {
  document.getElementById("id_empleado_editar").value = cod_empleado;
  document.getElementById("documentoidentidad_editar").value = documentoidentidad;
  document.getElementById("primer_nombre_editar").value = primer_nombre;
}



function borrarContent(){
  document.getElementById("search").value = "";
}



$(document).ready(function () {

  $('#myTable').DataTable({
    "language": {
      "url": "../static/index/js/idiom.json"},
    "lengthMenu": [[10, 25, 50], [10, 25, 50]],
    dom: 'Bfrtip',
    buttons: [
      { extend: 'csv' },
      { extend: 'print'},
    ]
  });
  $('#table2').DataTable({
    "language": {
      "url": "../static/index/js/idiom.json"},
    "lengthMenu": [[10, 25, 50], [10, 25, 50]],
    dom: 'Bfrtip',
    buttons: [
      { extend: 'csv' },
      { extend: 'print'},
    ]
  });
  $('#table3').DataTable({
    "language": {
      "url": "../static/index/js/idiom.json"},
    "lengthMenu": [[10, 25, 50], [10, 25, 50]],
    dom: 'Bfrtip',
    buttons: [
      { extend: 'csv' },
      { extend: 'print'},
    ]
  });
});
 