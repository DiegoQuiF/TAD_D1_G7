import { Component, Output, EventEmitter } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ConnBackendService } from '../../services/conn-backend.service';
import { Usuario } from '../../models/usuario';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
  @Output() mensajeEnviado = new EventEmitter<string>();
  @Output() usuarioLogin = new EventEmitter<Usuario>();

  constructor( private connBackend: ConnBackendService) { }

  usuario_: Array<Usuario> = new Array<Usuario>();

  correo_user: string = '';
  contra_user: string = '';

  async verificarDatos(correo_input:string, contra_input:string) {
    await this.getUsuario(correo_input, contra_input);
    if(this.usuario_ && this.usuario_.length > 0) {
      alert('Sesión iniciada como: ' + this.usuario_[0].nom_user + ' ' + this.usuario_[0].a_pat_user);
      this.usuarioLogin.emit(this.usuario_[0]);
      this.mensajeEnviado.emit('Abrir logged');
    }
    else {
      alert('Usuario no encontrado');
    }
  }

  async getUsuario(correo: string, contra: string) {
    try {
      const data = await this.connBackend.getUsuario(correo, contra).toPromise();
      console.log(data);
      this.usuario_ = data.usuario;
    } catch (error) {
      console.error(error);
    }
  }
}
