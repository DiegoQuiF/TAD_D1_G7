import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Usuario } from '../models/usuario';
import { ConnBackendService } from '../services/conn-backend.service';
import { Tarjeta } from '../models/tarjeta';
import { Coleccion } from '../models/coleccion';
import { Transaccion } from '../models/transaccion';
import { Comprador } from '../models/comprador';
import { Material } from '../models/material';

@Component({
  selector: 'app-principal',
  templateUrl: './principal.component.html',
  styleUrl: './principal.component.css'
})
export class PrincipalComponent {
  constructor( private connBackend: ConnBackendService) { }

  user_log: Usuario = new Usuario('', '', '', '', '', '', '', '');
  user_tarjetas_log: Array<Tarjeta> = new Array<Tarjeta>();
  user_transacciones_log: Transaccion = new Transaccion('0', '0', '0');
  user_colecciones_log: Array<Coleccion> = new Array<Coleccion>();
  user_compradores_log: Array<Comprador> = new Array<Comprador>();
  user_materiales_log: Array<Material> = new Array<Material>();
  
  async recibirUserLog(usuario: Usuario) {
    this.user_log = usuario;
  }
  async recibirUserTarjetasLog(tarjetas: Array<Tarjeta>) {
    this.user_tarjetas_log = tarjetas;
  }
  async recibirUserTransaccionesLog(transaccion: Transaccion) {
    this.user_transacciones_log = transaccion;
  }
  async recibirUserCompradoresLog(compradores: Array<Comprador>) {
    this.user_compradores_log = compradores;
  }
  async recibirUserColeccionesLog(colecciones: Array<Coleccion>) {
    this.user_colecciones_log = colecciones;
  }
  async recibirUserMaterialesLog(materiales: Array<Material>) {
    this.user_materiales_log = materiales;
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
