import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Usuario } from '../models/usuario';
import { ConnBackendService } from '../services/conn-backend.service';

@Component({
  selector: 'app-principal',
  templateUrl: './principal.component.html',
  styleUrl: './principal.component.css'
})
export class PrincipalComponent {
  constructor( private connBackend: ConnBackendService) { }

  usuario_logeado: any;

  recibirMensaje(mensaje: string) {
    if(mensaje == 'Abrir logged'){
      var hojaLogin = document.getElementById('hojaLogin');
      var hojaLogged = document.getElementById('hojaLogged');
      hojaLogin?.classList.remove('abierto');
      hojaLogin?.classList.add('cerrado');
      hojaLogged?.classList.remove('cerrado');
      hojaLogged?.classList.add('abierto');
    }
    else if(mensaje == 'Abrir login') {
      var hojaLogin = document.getElementById('hojaLogin');
      var hojaRegister = document.getElementById('hojaRegister');
      hojaRegister?.classList.remove('abierto');
      hojaRegister?.classList.add('cerrado');
      hojaLogin?.classList.remove('cerrado');
      hojaLogin?.classList.add('abierto');
    }
    else if(mensaje == 'Abrir register'){
      var hojaLogin = document.getElementById('hojaLogin');
      var hojaRegister = document.getElementById('hojaRegister');
      hojaLogin?.classList.remove('abierto');
      hojaLogin?.classList.add('cerrado');
      hojaRegister?.classList.remove('cerrado');
      hojaRegister?.classList.add('abierto');
    }
    else {
      alert("ERROR DEL SISTEMA");
    }
  }

  async recibirLog(usuario: Usuario) {
    this.usuario_logeado = usuario;
  }
}
