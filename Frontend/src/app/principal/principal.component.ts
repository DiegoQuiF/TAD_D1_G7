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
      var hojaLoginRegister = document.getElementById('hojaLoginRegister');
      var hojaLogged = document.getElementById('hojaLogged');
      hojaLoginRegister?.classList.remove('abierto');
      hojaLoginRegister?.classList.add('cerrado');
      hojaLogged?.classList.remove('cerrado');
      hojaLogged?.classList.add('abierto');
    }
    else {
      alert("ERROR DEL SISTEMA");
    }
  }

  async recibirLog(usuario: Usuario) {
    this.usuario_logeado = usuario;
  }
}
