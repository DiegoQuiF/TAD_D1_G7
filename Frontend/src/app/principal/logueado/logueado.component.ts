import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Usuario } from '../../models/usuario';
import { ConnBackendService } from '../../services/conn-backend.service';
import { Coleccion } from '../../models/coleccion';
import { MaterialCompleto } from '../../models/material-completo';

@Component({
  selector: 'app-logueado',
  templateUrl: './logueado.component.html',
  styleUrl: './logueado.component.css'
})
export class LogueadoComponent {
  @Input() user_input!: Usuario;
  @Output() mensajeSalir = new EventEmitter<string>();
  
  coleccion_array: Array<Coleccion> = new Array<Coleccion>();
  materiales_array: Array<MaterialCompleto> = new Array<MaterialCompleto>();
  materialesFisicos: Array<MaterialCompleto> = new Array<MaterialCompleto>();
  materialesDigitales: Array<MaterialCompleto> = new Array<MaterialCompleto>();

  constructor(private connBackend: ConnBackendService) { }

  salir() {
    var hoja = document.getElementById('hojaPerfil');
    var lista = document.getElementById('listaPerfil');
    this.cerrarHojas();
    hoja?.classList.toggle('inactivo');
    lista?.classList.toggle('active');
    this.mensajeSalir.emit('Abrir login');
  }

  abrirPerfil() {
    var hoja = document.getElementById('hojaPerfil');
    var lista = document.getElementById('listaPerfil');
    this.cerrarHojas();
    lista?.classList.toggle('active');
    hoja?.classList?.toggle('inactivo');
  }

  abrirComunidad() {
    var hoja = document.getElementById('hojaComunidad');
    var lista = document.getElementById('listaComunidad');
    this.cerrarHojas();
    lista?.classList.toggle('active');
    hoja?.classList?.toggle('inactivo');
    
  }

  async abrirColecciones() {
    var hoja = document.getElementById('hojaColecciones');
    var lista = document.getElementById('listaColecciones');
    this.cerrarHojas();
    await this.obtenerColecciones();
    lista?.classList.toggle('active');
    hoja?.classList?.toggle('inactivo');
  }

  async abrirTienda() {
    var hoja = document.getElementById('hojaTienda');
    var lista = document.getElementById('listaTienda');
    this.cerrarHojas();
    await this.obtenerMaterialesCompletos();
    this.materialesFisicos = this.materiales_array.filter(
      (material: MaterialCompleto) => material.fisicoMat === 'Si'
    );
    this.materialesDigitales = this.materiales_array.filter(
      (material: MaterialCompleto) => material.electronicoMat === 'Si'
    );
    lista?.classList.toggle('active');
    hoja?.classList?.toggle('inactivo');
  }

  abrirMensajes() {
    var hoja = document.getElementById('hojaMensajes');
    var lista = document.getElementById('listaMensajes');
    this.cerrarHojas();
    lista?.classList.toggle('active');
    hoja?.classList?.toggle('inactivo');
  }

  cerrarHojas() {
    var hojas = document.getElementsByClassName("hojas");
    for (var i = 0; i < hojas.length; i++) {
      var hoja = hojas[i];
      if (hoja.classList.contains('inactivo')) {
        //Listo
      }
      else {
        hoja.classList.add('inactivo');
      }
    }
    var listas = document.getElementsByClassName("listas");
    for (var i = 0; i < listas.length; i++) {
      var lista = listas[i];
      if (lista.classList.contains('active')) {
        lista.classList.toggle('active');
      }
      else {
        //Listo
      }
    }
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

  async obtenerMaterialesCompletos(){
    try {
      const data = await this.connBackend.getMaterialesCompletos(this.user_input.id_user).toPromise();
      console.log(data);
      this.materiales_array = data.materiales;
    } catch (error) {
      console.error(error);
    }
  }
}
