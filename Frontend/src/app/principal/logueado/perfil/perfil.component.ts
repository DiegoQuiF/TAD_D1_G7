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

  // mostrar alerta
  isAlert: boolean = false;
  mensajeAlert: string = '';

  constructor(private connBackend: ConnBackendService) { }

  async updateUsuario() {
    var result = await this.guardarUsuario(this.user_input);
    if (result = 'COMPLETE') {
      this.alert('Usuario actualizado correctamente...')
    }
    else {
      this.alert('Error: '+result)
    }
  }

  async guardarUsuario(usuario:Usuario) {
    try {
      const data = await this.connBackend.putUsuario(usuario).toPromise();
      console.log(data);
      if (data.success === true) {
        return data.message;
      }
      else {
        return 'Error interno del sistema';
      }
    } catch (error) {
      console.error(error);
      return 'Error interno del sistema'
    }
  }

  // Lógica de carga asíncrona
  isLoading: boolean = false;

  async update() {
    this.isLoading = true;
    try {
      await this.updateUsuario();
    } catch (error) {
      this.alert('Error interno del sistema...');
    } finally {
      this.isLoading = false;
    }
  }

  async alert(mensaje:string) {
    this.mensajeAlert = mensaje;
    this.isAlert = true;
  }

  async continuar() {
    this.isAlert = false;
  }
}
