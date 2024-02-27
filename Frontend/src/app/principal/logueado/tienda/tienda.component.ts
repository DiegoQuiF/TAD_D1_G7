import { Component, EventEmitter, Input, Output } from '@angular/core';
import { MaterialCompleto } from '../../../models/material-completo';
import { Usuario } from '../../../models/usuario';
import { ConnBackendService } from '../../../services/conn-backend.service';
import { MaterialCategoria } from '../../../models/material-categoria';
import { Coleccion } from '../../../models/coleccion';
import { Categoria } from '../../../models/categoria';

@Component({
  selector: 'app-tienda',
  templateUrl: './tienda.component.html',
  styleUrl: './tienda.component.css'
})
export class TiendaComponent {
  @Input() materiales_array: Array<MaterialCompleto> = new Array<MaterialCompleto>();
  @Input() materiales_fisicos: Array<MaterialCompleto> = new Array<MaterialCompleto>();
  @Input() materiales_digitales: Array<MaterialCompleto> = new Array<MaterialCompleto>();
  @Input() carrito_array: Array<MaterialCompleto> = new Array<MaterialCompleto>();
  @Input() categorias_tienda: Array<MaterialCategoria> = new Array<MaterialCategoria>();
  @Input() tienda_fisica_filtrada: Array<MaterialCompleto> = new Array<MaterialCompleto>();
  @Input() filtro_coleccion: Array<Coleccion> = new Array<Coleccion>();
  @Input() filtro_categorias: Array<Categoria> = new Array<Categoria>();
  @Input() user_input!: Usuario;
  @Output() mensajeActualizar = new EventEmitter<string>();

  constructor(private connBackend: ConnBackendService) {}

  async comprarMaterial(idMat:string){
    this.cargando = true;
    if(await this.postFactura(idMat, this.user_input.id_user)){
      this.mensajeActualizar.emit('actualizarPerfil');
      await this.getCarrito(this.user_input.id_user);
      this.cargando = false;
      this.alerta('Material comprado correctamente...');
    }
    else{
      this.cargando = false;
      this.alerta('Hubo un error en la compra...');
    }
  }

  async postFactura(idMat:string, idUser:string) {
    try {
      const data = await this.connBackend.postFactura(idMat, idUser).toPromise();
      console.log(data);
      if(data.factura.length > 0 && data.factura){
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

  async agregarAlCarrito(idMat: string) {
    this.cargando = true;
    if(await this.postCarrito(idMat, this.user_input.id_user)){
      this.cargando = false;
      this.alerta("Agregado al carrito con exito...");
    }
    else{
      this.cargando = false;
      this.alerta("Error al agregar al carrito...");
    }
  }

  async postCarrito(idMat:string, idUser:string) {
    try {
      const data = await this.connBackend.postCarrito(idMat, idUser).toPromise();
      console.log(data);
      if(data.carrito.length > 0 && data.carrito){
        await this.getCarrito(idUser);
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

  async getCarrito(idUser:string) {
    try {
      const data = await this.connBackend.getCarrito(idUser).toPromise();
      console.log(data);
      if(data.carrito.length > 0 && data.carrito){
        this.carrito_array = data.carrito;
        return true;
      }
      else {
        this.carrito_array = new Array<MaterialCompleto>();
        return false;
      }
    } catch (error) {
      console.error(error);
      return false;
    }
  }

  async abrirOpciones(id:string){
    var opciones = document.getElementById(id);
    opciones?.classList.toggle('oculto');
  }

  async abrirOpciones1(id:string){
    var opciones = document.getElementById(id+"C");
    opciones?.classList.toggle('oculto');
  }

  async recargarMaterialesFisicos() {
    this.cargando = true;
    this.obtenerMaterialesCompletos();
    this.materiales_fisicos = this.materiales_array.filter(
      (material: MaterialCompleto) => material.fisicoMat === 'Si'
    );
    this.materiales_digitales = this.materiales_array.filter(
      (material: MaterialCompleto) => material.electronicoMat === 'Si'
    );
    this.cargando = false;
    this.alerta('Materiales bibliográficos (fisicos) actualizados...');
  }
  async obtenerMaterialesCompletos(){
    try {
      const data = await this.connBackend.getMaterialesCompletos(this.user_input.id_user).toPromise();
      console.log(data);
      this.materiales_array = data.materiales;
    } catch (error) {
      console.error(error);
    }
  }


  // CARGA DE LA PÁGINA
  cargando: boolean = false;


  // ALERTA DE LA PÁGINA
  mostrarAlerta: boolean = false;
  mensajeAlerta: string = '';

  async alerta( mensaje:string ) {
    this.mensajeAlerta = mensaje;
    this.mostrarAlerta = true;
  }
  async continuar() {
    this.mensajeAlerta = '';
    this.mostrarAlerta = false;
  }





  filtroPrecio:string = '1';
  filtroIdioma:string = 'Espanol';
  filtro3:string = '';
  filtroAnio:string = '6';
  filtroCol:string = '';

  Filtrar() {
    if(this.filtroPrecio === '1'){
      this.tienda_fisica_filtrada = this.materiales_fisicos.filter(
        (material: MaterialCompleto) => ((parseFloat(material.precioFMat) >= 0.0) && (parseFloat(material.precioFMat) < 10.0))
      );
    }
    if(this.filtroPrecio === '2'){
      this.tienda_fisica_filtrada = this.materiales_fisicos.filter(
        (material: MaterialCompleto) => ((parseFloat(material.precioFMat) >= 10.0) && (parseFloat(material.precioFMat) < 20.0))
      );
    }
    if(this.filtroPrecio === '3'){
      this.tienda_fisica_filtrada = this.materiales_fisicos.filter(
        (material: MaterialCompleto) => ((parseFloat(material.precioFMat) >= 20.0) && (parseFloat(material.precioFMat) < 40.0))
      );
    }
    if(this.filtroPrecio === '4'){
      this.tienda_fisica_filtrada = this.materiales_fisicos.filter(
        (material: MaterialCompleto) => ((parseFloat(material.precioFMat) >= 40.0) && (parseFloat(material.precioFMat) < 60.0))
      );
    }
    if(this.filtroPrecio === '5'){
      this.tienda_fisica_filtrada = this.materiales_fisicos.filter(
        (material: MaterialCompleto) => ((parseFloat(material.precioFMat) >= 60.0) && (parseFloat(material.precioFMat) < 100.0))
      );
    }
    if(this.filtroPrecio === '6'){
      this.tienda_fisica_filtrada = this.materiales_fisicos.filter(
        (material: MaterialCompleto) => (parseFloat(material.precioFMat) >= 100.0)
      );
    }
    this.tienda_fisica_filtrada = this.tienda_fisica_filtrada.filter(
      (material: MaterialCompleto) => material.idiomaMat === this.filtroIdioma
    );
    if(this.filtro3.toString() !== '') {
      this.tienda_fisica_filtrada = this.tienda_fisica_filtrada.filter(material =>
        this.categorias_tienda.some(categoria =>
          categoria.idM === material.idMat && categoria.nombreC === this.filtro3
        )
      );
    }
    if(this.filtroAnio === '1'){
      this.tienda_fisica_filtrada = this.tienda_fisica_filtrada.filter(
        (material: MaterialCompleto) => ((parseInt(material.originalMat.substring(material.originalMat.length-4)) < 1900))
      );
    }
    if(this.filtroAnio === '2'){
      this.tienda_fisica_filtrada = this.tienda_fisica_filtrada.filter(
        (material: MaterialCompleto) => ((parseInt(material.originalMat.substring(material.originalMat.length-4)) >= 1900) && (parseInt(material.originalMat.substring(material.originalMat.length-4)) < 1925))
      );
    }
    if(this.filtroAnio === '3'){
      this.tienda_fisica_filtrada = this.tienda_fisica_filtrada.filter(
        (material: MaterialCompleto) => ((parseInt(material.originalMat.substring(material.originalMat.length-4)) >= 1925) && (parseInt(material.originalMat.substring(material.originalMat.length-4)) < 1950))
      );
    }
    if(this.filtroAnio === '4'){
      this.tienda_fisica_filtrada = this.tienda_fisica_filtrada.filter(
        (material: MaterialCompleto) => ((parseInt(material.originalMat.substring(material.originalMat.length-4)) >= 1950) && (parseInt(material.originalMat.substring(material.originalMat.length-4)) < 1975))
      );
    }
    if(this.filtroAnio === '5'){
      this.tienda_fisica_filtrada = this.tienda_fisica_filtrada.filter(
        (material: MaterialCompleto) => ((parseInt(material.originalMat.substring(material.originalMat.length-4)) >= 1975) && (parseInt(material.originalMat.substring(material.originalMat.length-4)) < 2000))
      );
    }
    if(this.filtroAnio === '6'){
      this.tienda_fisica_filtrada = this.tienda_fisica_filtrada.filter(
        (material: MaterialCompleto) => ((parseInt(material.originalMat.substring(material.originalMat.length-4)) >= 2000) && (parseInt(material.originalMat.substring(material.originalMat.length-4)) < 2025))
      );
    }
    if(this.filtroCol.toString() !== '') {
      this.tienda_fisica_filtrada = this.tienda_fisica_filtrada.filter(
        (material: MaterialCompleto) => material.idCol.toString() === this.filtroCol.toString()
      );
    }
  }

  RefreshFiltrar () {
    this.filtroPrecio = '1';
    this.filtroIdioma = 'Espanol';
    this.filtro3 = '';
    this.filtroAnio = '6';
    this.filtroCol = '';
    this.tienda_fisica_filtrada = this.materiales_fisicos;
  }
}

