import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Usuario } from '../../models/usuario';
import { ConnBackendService } from '../../services/conn-backend.service';

@Component({
  selector: 'app-logueado',
  templateUrl: './logueado.component.html',
  styleUrl: './logueado.component.css'
})
export class LogueadoComponent {
  @Input() user_input!: Usuario;
  @Output() mensajeSalir = new EventEmitter<string>();


  constructor(private connBackend: ConnBackendService) { }

  salir() {
    this.mensajeSalir.emit('Abrir login');
  }

  async updateUsuario() {
    if (await this.guardarUsuario(this.user_input)) {
      alert("USUARIO ACTUALIZADO CORRECTAMENTE");
    }
    else {
      alert("ERROR EN EL INGRESO DE DATOS");
    }
  }

  async guardarUsuario(usuario:Usuario) {
    const data = await this.connBackend.putUsuario(usuario).toPromise();
    if(data.usuario && data.usuario.length > 0){
      return true;
    }
    else {
      return false;
    }
  }
}
