import { Component, Input } from '@angular/core';
import { Coleccion } from '../../../models/coleccion';
import { Usuario } from '../../../models/usuario';
import { ConnBackendService } from '../../../services/conn-backend.service';

@Component({
  selector: 'app-colecciones',
  templateUrl: './colecciones.component.html',
  styleUrl: './colecciones.component.css'
})
export class ColeccionesComponent {
  @Input() coleccion_array: Array<Coleccion> = new Array<Coleccion>();
  @Input() user_input!: Usuario;
  
  coleccion_selected: Coleccion = new Coleccion("-", "-", "Privada", "-", "-");
  mensajeCrear: string = 'Crear Coleccion';

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
}
