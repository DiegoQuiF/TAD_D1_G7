import { Component, Input } from '@angular/core';
import { Coleccion } from '../../../models/coleccion';
import { Usuario } from '../../../models/usuario';
import { ConnBackendService } from '../../../services/conn-backend.service';
import { Material } from '../../../models/material';


@Component({
  selector: 'app-colecciones',
  templateUrl: './colecciones.component.html',
  styleUrl: './colecciones.component.css'
})
export class ColeccionesComponent {
  @Input() coleccion_array: Array<Coleccion> = new Array<Coleccion>();
  @Input() user_input!: Usuario;
  
  coleccion_selected: Coleccion = new Coleccion("-", "-", "Privada", "-", "-");
  material_nuevo: Material = new Material('', '', '', '', '', '', '', '', '', '', '', '');
  mensajeCrear: string = 'Crear Coleccion';
  libros_array!: Array<Material>;
  


  constructor(private connBackend: ConnBackendService) { }

  abrirCrearColeccion() {
    var formularioCrear = document.getElementById('formularioCrear');
    formularioCrear?.classList.toggle('cerrado');
    if(this.mensajeCrear === 'Crear Coleccion') {
      this.mensajeCrear = 'Cancelar';
    }
    else {
      this.mensajeCrear = 'Crear Coleccion';
    }
  }

  editarEliminarColeccion(coleccion: Coleccion){
    this.coleccion_selected = coleccion;
    var formularioEditarEliminar = document.getElementById('formularioEditarEliminar');

    const botones = document.getElementsByClassName('botones') as HTMLCollectionOf<HTMLButtonElement>;
    for (let i = 0; i < botones.length; i++) {
      const boton = botones[i];
      boton.disabled = true;
      boton.style.background = '#3a3a3a';
      boton.style.cursor = 'default';
    }

    formularioEditarEliminar?.classList.toggle('cerrado');
  }

  bloquearPrecioStockFisico() {
    if (this.material_nuevo.fisico === 'No') {
      this.material_nuevo.precioF = '0.0';
      this.material_nuevo.stockF = '0';
    } else {
      this.material_nuevo.precioF  = ''; 
      this.material_nuevo.stockF = ''; 
    }
  }
  
  bloquearPrecioElectronico() {
    if (this.material_nuevo.electronico === 'No') {
      this.material_nuevo.precioE = '0.0';
    } else {
      this.material_nuevo.precioE  = ''; 
    }
  }

  async recibirMensaje(mensaje:string){
    if(mensaje === 'Salir') {
      this.abrirCrearColeccion();
    }
    else if(mensaje === 'Salir1') {
      var formularioEditarEliminar = document.getElementById('formularioEditarEliminar');
      formularioEditarEliminar?.classList.toggle('cerrado');
      this.coleccion_selected = new Coleccion("-", "-", "Privada", "-", "-");
    }
    await this.obtenerColecciones();
  }

  async obtenerColecciones(){
    try {
      const data = await this.connBackend.getColeccion(this.user_input.id_user).toPromise();
      console.log(data);
      this.coleccion_array = data.coleccion;
    } catch (error) {
      console.error(error);
    }
  }

  async abrirLibros(id:string){
    var libros = document.getElementById(id);
    if (libros?.classList.contains('oculto')){
      await this.getLibros(id);
      this.cerrarTodosLibros();
      libros?.classList.toggle('oculto');
    }
    else {
      this.cerrarTodosLibros();
    }
  }

  cerrarTodosLibros(){
    var libros = document.getElementsByClassName('libros');
    for (var i = 0; i < libros.length; i++) {
      var libro = libros[i];
      if (libro.classList.contains('oculto')) {
        //Listo
      }
      else {
        libro.classList.toggle('oculto');
      }
    }
  }

  async getLibros(id:string){
    try {
      const data = await this.connBackend.getLibros(id).toPromise();
      console.log(data);
      this.libros_array = data.material;
    } catch (error) {
      console.error(error);
    }
  }

  async crearMaterial(material:Material, id:string){
    if(await this.postMaterial(material, id)){
      await this.getLibros(id);
      alert("Material creado correctamente");
      this.material_nuevo = new Material('', '', '', '', '', '', '', '', '', '', '', '');
    }
    else{
      alert('Error en el registro de datos:\n- Verifique la sintaxis de los campos asociados.\n- Seleccione opciones válidas.');
    }
  }

  async postMaterial(material:Material, id:string) {
    try {
      const data = await this.connBackend.postMaterial(material, id).toPromise();
      console.log(data);
      if(data.libro.length > 0 && data.libro){
        return true;
      }
      else {
        return false;
      }
    } catch (error) {
      console.error(error);
      return false;
    }
  }

  async eliminarLibro(id_libro:string, id_coleccion:string){
    if (await this.deleteLibro(id_libro)) {
      alert("MATERIAL ELIMINADO CORRECTAMENTE");
      await this.getLibros(id_coleccion);
    }
    else {
      alert("ERROR");
    }
  }

  async deleteLibro(id:string) {
    const data = await this.connBackend.deleteLibro(id).toPromise();
    if(data.libro && data.libro.length > 0){
      return true;
    }
    else {
      return false;
    }
  }
}
