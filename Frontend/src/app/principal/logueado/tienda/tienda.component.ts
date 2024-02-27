import { Component, EventEmitter, Input, Output } from '@angular/core';
import { MaterialCompleto } from '../../../models/material-completo';
import { Usuario } from '../../../models/usuario';
import { ConnBackendService } from '../../../services/conn-backend.service';
import { MaterialCategoria } from '../../../models/material-categoria';

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
}
