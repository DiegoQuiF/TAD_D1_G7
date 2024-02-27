import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { ConnBackendService } from '../../services/conn-backend.service';
import Highcharts from 'highcharts';

@Component({
  selector: 'data-dashboard',
  templateUrl: './data-dashboard.component.html',
  styleUrl: './data-dashboard.component.css'
})

export class DataDashboardComponent {
  
  constructor( private connBackend:ConnBackendService ) {};

  @Output() mensajeSalir = new EventEmitter<string>();

  mostrarOPC( opc:string , sel:string ){
    var hoja = document.getElementById(opc);
    var seleccion = document.getElementById(sel);
    this.cerrarTodasOPC();
    seleccion?.classList.toggle('activo');
    hoja?.classList.toggle('cerrado');
  }
  cerrarTodasOPC(){
    var figuras = document.getElementsByClassName('figura');
    for (var i = 0; i < figuras.length; i++) {
      var figura = figuras[i];
      if (figura.classList.contains('cerrado')) {
        //Listo
      }
      else {
        figura.classList.toggle('cerrado');
      }
    }
    var selecciones = document.getElementsByClassName('seleccion');
    for (var i = 0; i < selecciones.length; i++) {
      var seleccion = selecciones[i];
      if (seleccion.classList.contains('activo')) {
        seleccion.classList.toggle('activo');
      }
      else {
        //Listo
      }
    }
  }

  salir() {
    this.mensajeSalir.emit('Salir1');
  }
}