import { Component, Input } from '@angular/core';
import { Usuario } from '../../../models/usuario';
import { ConnBackendService } from '../../../services/conn-backend.service';

@Component({
  selector: 'app-perfil',
  templateUrl: './perfil.component.html',
  styleUrl: './perfil.component.css'
})
export class PerfilComponent {
  @Input() user_input!: Usuario;

  constructor(private connBackend: ConnBackendService) { }

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
