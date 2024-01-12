import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

import { Usuario } from '../../models/usuario';
import { ConnBackendService } from '../../services/conn-backend.service';

@Component({
  selector: 'app-logged',
  templateUrl: './logged.component.html',
  styleUrl: './logged.component.css'
})
export class LoggedComponent {
  id_user: string = ''

  user_array: Array<Usuario> = new Array<Usuario>();

  constructor(private connBackend: ConnBackendService) { }

  async getUsuarios(){
    try{
      const data = await this.connBackend.getUsuarios().toPromise();
      alert('Datos de los usuarios consultados');
      this.user_array = data.usuarios;
    } catch(error) {
      console.error(error);
      return false;
    }
    return true;
  }
}
