import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Usuario } from '../models/usuario';
import { ConnBackendService } from '../services/conn-backend.service';
import { Tarjeta } from '../models/tarjeta';
import { Coleccion } from '../models/coleccion';

@Component({
  selector: 'app-principal',
  templateUrl: './principal.component.html',
  styleUrl: './principal.component.css'
})
export class PrincipalComponent {
  constructor( private connBackend: ConnBackendService) { }

  user_log: any;
  user_tarjetas_log: any;
  user_colecciones_log: any;
  
  async recibirUserLog(usuario: Usuario) {
    this.user_log = usuario;
  }
  async recibirUserTarjetasLog(tarjetas: Array<Tarjeta>) {
    this.user_tarjetas_log = tarjetas;
  }
  async recibirUserColeccionesLog(colecciones: Array<Coleccion>) {
    this.user_colecciones_log = colecciones;
  }
  async recibirMensajes(mensaje: string) {
    if(mensaje == 'Logueado'){
      var hojaLoginRegister = document.getElementById('hojaLoginRegister');
      var hojaLogueado = document.getElementById('hojaLogueado');
      hojaLoginRegister?.classList.toggle('cerrado');
      hojaLogueado?.classList.toggle('cerrado');
    }
    else if(mensaje == 'Admin'){
      var hojaLoginRegister = document.getElementById('hojaLoginRegister');
      var hojaAdmin = document.getElementById('hojaAdmin');
      hojaLoginRegister?.classList.toggle('cerrado');
      hojaAdmin?.classList.toggle('cerrado');
    }
    else if(mensaje == 'Salir'){
      var hojaLoginRegister = document.getElementById('hojaLoginRegister');
      var hojaLogueado = document.getElementById('hojaLogueado');
      hojaLogueado?.classList.toggle('cerrado');
      hojaLoginRegister?.classList.toggle('cerrado');
    }
    else {
      alert("ERROR DEL SISTEMA");
    }
  }
}
