import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Coleccion } from '../../../../models/coleccion';
import { ConnBackendService } from '../../../../services/conn-backend.service';
import { Usuario } from '../../../../models/usuario';

@Component({
  selector: 'app-crear-coleccion',
  templateUrl: './crear-coleccion.component.html',
  styleUrl: './crear-coleccion.component.css'
})
export class CrearColeccionComponent {
  @Output() mensaje = new EventEmitter<string>();
  @Input() user_input!:Usuario;

  coleccion_nueva: Coleccion = new Coleccion('', '', 'Privada', '', '');

  constructor(private connBackend: ConnBackendService) { }

  async crearColeccion(nombre:string, tipo:string){
    if(await this.postColeccion_registro(nombre, tipo)){
      alert("Colección creada correctamente");
      this.coleccion_nueva = new Coleccion('', '', 'Privada', '', '');
      this.salir();
    }
    else{
      alert('Error en el registro de datos:\n- Verifique la sintaxis del nombre.\n- Seleccione un tipo valido.');
    }
  }

  salir(){
    this.mensaje.emit('Salir');
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
}
