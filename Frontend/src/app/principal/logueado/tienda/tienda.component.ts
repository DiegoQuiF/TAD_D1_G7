import { Component, Input } from '@angular/core';
import { MaterialCompleto } from '../../../models/material-completo';
import { Usuario } from '../../../models/usuario';
import { ConnBackendService } from '../../../services/conn-backend.service';

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
  @Input() user_input!: Usuario;

  constructor(private connBackend: ConnBackendService) {}

  async comprarMaterial(idMat:string){
    if(await this.postFactura(idMat, this.user_input.id_user)){
      alert("Material Comprado");
    }
    else{
      alert("Error de compra");
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
    if(await this.postCarrito(idMat, this.user_input.id_user)){
      alert("Agregado al carrito con exito...");
    }
    else{
      alert("Error al agregar al carrito...");
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
}
