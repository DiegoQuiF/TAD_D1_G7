import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Coleccion } from '../../../models/coleccion';
import { Usuario } from '../../../models/usuario';
import { ConnBackendService } from '../../../services/conn-backend.service';
import { Material } from '../../../models/material';
import { MaterialCompleto } from '../../../models/material-completo';
import { MaterialCategoria } from '../../../models/material-categoria';
import { Categoria } from '../../../models/categoria';


@Component({
  selector: 'app-colecciones',
  templateUrl: './colecciones.component.html',
  styleUrl: './colecciones.component.css'
})
export class ColeccionesComponent {
  @Input() user_input!: Usuario;
  @Input() user_colecciones_input: Array<Coleccion> = new Array<Coleccion>();
  @Input() user_materiales_input: Array<Material> = new Array<Material>();
  @Input() user_comprados_input:Array<MaterialCompleto> = new Array<MaterialCompleto>();
  @Input() user_material_categorias_input: Array<MaterialCategoria> = new Array<MaterialCategoria>();
  @Input() categorias_input: Array<Categoria> = new Array<Categoria>();
  @Output() mensajeActualizar = new EventEmitter<string>();

  material_filtrado: Array<Material> = new Array<Material>();
  categorias_filtrado: Array<MaterialCategoria> = new Array<MaterialCategoria>();
  material_nuevo: Material = new Material('', '', '', '', '', '', '', '', '', '', '', '');

  titulo_material_selected = '';
  id_material_selected = '';
  categoria_selected = '';
  
  mostrarAddCategoria:boolean = false;
  
  abrirAddCategoria(id:string, titulo:string) {
    this.id_material_selected = id;
    this.titulo_material_selected = titulo;
    this.mostrarAddCategoria = true;
  }

  cerrarAddCategoria() {
    this.mostrarAddCategoria = false;
  }

  abrirPostCategoria() {
    this.mostrarAddCategoria = true;
  }

  async agregarCategoria(idM: string, idC:string){
    this.cerrarAddCategoria();
    this.cargando = true;
    if (await this.addCategoria(idM, idC)) {
      await this.recargarCategorias(this.user_input.id_user);
    }
  }

  async addCategoria(idM:string, idC:string) {
    try {
      const data = await this.connBackend.postCategoria(idM, idC).toPromise();
      console.log(data);
      if (data.success === true) {
        await this.recargarCategorias(this.user_input.id_user);
        this.cargando = false;
        this.alerta('Tag agregado correctamente...');
        return true;
      }
      else {
        this.cargando = false;
        this.alerta('Error al agregar el TAG...');
        return false;
      }
    } catch (error) {
      console.error(error);
      this.cargando = false;
      this.alerta('Error al agregar el TAG...');
      return false;
    }
  }

  async recargarCategorias(idU:string) {
    try {
      const data = await this.connBackend.getMaterialCategoria(idU).toPromise();
      console.log(data);
      if (data.materialCategorias.length > 0 && data.materialCategorias) {
        this.user_material_categorias_input = data.materialCategorias;
        this.categorias_filtrado = this.user_material_categorias_input;
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

  async deleteCategoria(idMC:string){
    this.cargando = true;
    try {
      const data = await this.connBackend.delCategoria(idMC).toPromise();
      console.log(data);
      if (data.success === true) {
        await this.recargarCategorias(this.user_input.id_user);
        this.cargando = false;
        this.alerta('Tag eliminado correctamente...');
      }
      else {
        this.cargando = false;
        this.alerta('Error el intentar eliminar el Tag...');
      }
    } catch (error) {
      console.error(error);
      this.cargando = false;
      this.alerta('Error el intentar eliminar el Tag...');
    }
  }


  constructor(private connBackend: ConnBackendService) { }

  //Se ejecuta cuando se selecciono que no hay disponibilidad Fisica del material 
  bloquearPrecioStockFisico() {
    if (this.material_nuevo.dispFisico === 'No') {
      this.material_nuevo.precioFisico = '0.0';
      this.material_nuevo.stockFisico = '0';
    } else {
      this.material_nuevo.precioFisico  = ''; 
      this.material_nuevo.stockFisico = ''; 
    }
  }
  
  //Se ejecuta cuando se selecciono que no hay disponibilidad Electronica del material 
  bloquearPrecioElectronico() {
    if (this.material_nuevo.dispElec === 'No') {
      this.material_nuevo.precioElec = '0.0';
    } else {
      this.material_nuevo.precioElec  = ''; 
    }
  }

  async obtenerColecciones(){
    try {
      const data = await this.connBackend.getColeccion(this.user_input.id_user).toPromise();
      console.log(data);
      this.user_colecciones_input = data.coleccion;
    } catch (error) {
      console.error(error);
    }
  }

  async abrirLibros(id:string){
    var libros = document.getElementById(id);
    if (libros?.classList.contains('oculto')){
      // Filtrado de libros
      this.material_filtrado = this.user_materiales_input.filter(material => material.idColeccion === id);
      this.categorias_filtrado = this.user_material_categorias_input;
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
      const data = await this.connBackend.getMaterial(id).toPromise();
      console.log(data);
      this.user_materiales_input = data.material;
    } catch (error) {
      console.error(error);
    }
  }

  async crearMaterial(material:Material, id:string){
    this.cargando = true;
    if(await this.postMaterial(material, id)){
      await this.getLibros(this.user_input.id_user);
      this.material_filtrado = this.user_materiales_input.filter(material => material.idColeccion === id);
      this.material_nuevo = new Material('', '', '', '', '', '', '', '', '', '', '', '');
      this.mensajeActualizar.emit('actualizarPerfil');
      this.cargando = false;
      this.alerta('Material creado correctamente...');
    }
    else{
      this.cargando = false;
      this.alerta('Error en el registro de datos, verifique la sintaxis de los campos asociados y seleccione opciones validad...')
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
    this.cargando = true;
    if (await this.deleteLibro(id_libro)) {
      await this.getLibros(this.user_input.id_user);
      this.material_filtrado = this.user_materiales_input.filter(material => material.idColeccion === id_coleccion);
      this.mensajeActualizar.emit('actualizarPerfil');
      this.cargando = false;
      this.alerta("Material eliminado correctamente...");
      await this.getLibros(this.user_input.id_user);
    }
    else {
      this.alerta('No fue posible eliminar el material bibliográfico...');
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

  async abrirColecciones() {
    var hoja = document.getElementById('abrirColecciones');
    hoja?.classList.toggle('inactivo');
  }

  mostrarCrearContenido: boolean = false;
  coleccion_nueva: Coleccion = new Coleccion('', '', 'Privada', '', '');
  
  async iniciarCrearColeccion() {
    this.mostrarCrearContenido = true;
  }
  async crearColeccion(nombre:string, tipo:string){
    this.mostrarCrearContenido = false;
    this.cargando = true;
    if(await this.postColeccion_registro(nombre, tipo)){
      this.user_colecciones_input = await this.getColecciones(this.user_input.id_user);
      this.coleccion_nueva = new Coleccion('', '', 'Privada', '', '');
      this.alerta('Colección registrada satisfactoriamente...');
      this.cargando = false;
    }
    else{
      this.cargando = false;
      this.alerta('Error en el registro de datos, verifique la sintaxis del nombre de la colección...');
    }
  }
  async postColeccion_registro(nombre:string, tipo:string) {
    try {
      const data = await this.connBackend.postColeccion(this.user_input.id_user, nombre, tipo).toPromise();
      console.log(data);
      if(data.coleccion.length > 0 && data.coleccion){
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
  cancelarCrearColeccion() {
    this.mostrarCrearContenido = false;
    this.coleccion_nueva = new Coleccion("", "", "Privada", "", "");
  }


  // ALERTAS
  cargando: boolean = false;
  mostrarAlerta: boolean = false;
  mensajeAlerta: string = '';

  async alerta(mensaje:string) {
    this.mensajeAlerta = mensaje;
    this.mostrarAlerta = true;
  }
  async continuar() {
    this.mostrarAlerta = false;
  }


  // ACTUALIZAR COLECCIONES
  async getColecciones( id:string ) {
    try {
      const data = await this.connBackend.getColeccion(id).toPromise();
      console.log(data);
      var colecciones: Array<Coleccion> = data.coleccion;
      if ( data.success == true ) {
        if ( colecciones.length > 0 && colecciones ) {
          return colecciones;
        }
        else {
          return new Array<Coleccion>();
        }
      }
      else {
        return new Array<Coleccion>();
      }
    } catch (error) {
      console.error(error);
      return new Array<Coleccion>();
    }
  }


  
  // EDITAR ELIMINAR COLECCIÓN
  coleccion1: Coleccion = new Coleccion('', '', '', '', '');
  mostrarEditarColeccion: boolean = false;
  
  iniciarEditarColeccion(coleccion: Coleccion) {
    this.coleccion1 = coleccion;
    this.mostrarEditarColeccion = true;
  }
  cancelarEditarColeccion() {
    this.mostrarEditarColeccion = false;
  }
  async guardarColeccion(coleccion:Coleccion){
    this.mostrarEditarColeccion = false;
    this.cargando = true;
    if (await this.guardarCol(coleccion)) {
      this.user_colecciones_input = await this.getColecciones(this.user_input.id_user);
      this.cargando = false;
      this.alerta("Colección actualizada correctamente...");
      
    }
    else {
      this.cargando = false;
      this.alerta("No fue posible actualizar la colección...");
    }
  }
  async guardarCol(coleccion:Coleccion) {
    const data = await this.connBackend.putColeccion(coleccion).toPromise();
    if(data.coleccion && data.coleccion.length > 0){
      return true;
    }
    else {
      return false;
    }
  }
  async eliminarColeccion(coleccion:Coleccion){
    this.mostrarEditarColeccion = false;
    this.cargando = true;
    if (await this.eliminarCol(coleccion)) {
      this.user_colecciones_input = await this.getColecciones(this.user_input.id_user);
      this.cargando = false;
      this.alerta("Colección eliminada correctamente...");
    }
    else {
      this.cargando = false;
      this.alerta("No fue posible eliminar la colección...");
    }
  }
  async eliminarCol(coleccion:Coleccion) {
    const data = await this.connBackend.deleteColeccion(coleccion).toPromise();
    if(data.coleccion && data.coleccion.length > 0){
      return true;
    }
    else {
      return false;
    }
  }

  async actualizarTodo(){
    try {
      this.cargando = true;
      this.user_comprados_input = await this.refreshUserCompradosInput();
      this.cargando = false;
    } catch (error) {
      console.error(error);
      this.cargando = false;
    }
  }
  async refreshUserCompradosInput() {
    try {
      const data = await this.connBackend.getComprados(this.user_input.id_user).toPromise();
      console.log(data);
      var comprados: Array<MaterialCompleto> = data.comprados;
      if(comprados.length > 0 && comprados){
        return comprados;
      }
      else {
        return new Array<MaterialCompleto>();
      }
    } catch (error) {
      console.error(error);
      return new Array<MaterialCompleto>();
    }
  }
}
