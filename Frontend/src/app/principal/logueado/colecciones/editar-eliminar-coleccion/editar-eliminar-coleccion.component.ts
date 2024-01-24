import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Coleccion } from '../../../../models/coleccion';
import { ConnBackendService } from '../../../../services/conn-backend.service';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-editar-eliminar-coleccion',
  templateUrl: './editar-eliminar-coleccion.component.html',
  styleUrl: './editar-eliminar-coleccion.component.css'
})
export class EditarEliminarColeccionComponent {
  @Output() mensaje = new EventEmitter<string>();
  @Input() coleccion1!:Coleccion;

  constructor (private connBackend: ConnBackendService) {}

  salir(){
    this.mensaje.emit('Salir1');
  }

  async guardar(coleccion:Coleccion){
    if (await this.guardarColeccion(coleccion)) {
      alert("COLECCIÓN ACTUALIZADA CORRECTAMENTE");
      this.salir();
    }
    else {
      alert("ERROR EN EL INGRESO DE DATOS");
    }
  }

  async guardarColeccion(coleccion:Coleccion) {
    const data = await this.connBackend.putColeccion(coleccion).toPromise();
    if(data.coleccion && data.coleccion.length > 0){
      return true;
    }
    else {
      return false;
    }
  }


  async eliminar(coleccion:Coleccion){
    if (await this.eliminarColeccion(coleccion)) {
      alert("COLECCIÓN ELIMINADA CORRECTAMENTE");
      this.salir();
    }
    else {
      alert("ERROR\n- Es posible que tenga Libros dentro de la colección,\npor lo que no es posible eliminarla");
    }
  }

  async eliminarColeccion(coleccion:Coleccion) {
    const data = await this.connBackend.deleteColeccion(coleccion).toPromise();
    if(data.coleccion && data.coleccion.length > 0){
      return true;
    }
    else {
      return false;
    }
  }
}
