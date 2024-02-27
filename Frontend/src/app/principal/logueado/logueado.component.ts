import { Component, EventEmitter, Input, Output, ViewChild } from '@angular/core';
import { Usuario } from '../../models/usuario';
import { ConnBackendService } from '../../services/conn-backend.service';
import { Coleccion } from '../../models/coleccion';
import { MaterialCompleto } from '../../models/material-completo';
import { Tarjeta } from '../../models/tarjeta';
import { Material } from '../../models/material';
import { Transaccion } from '../../models/transaccion';
import { Comprador } from '../../models/comprador';
import { PerfilComponent } from './perfil/perfil.component';
import { MaterialCategoria } from '../../models/material-categoria';
import { Categoria } from '../../models/categoria';
import { ColeccionesComponent } from './colecciones/colecciones.component';

@Component({
  selector: 'app-logueado',
  templateUrl: './logueado.component.html',
  styleUrl: './logueado.component.css'
})
export class LogueadoComponent {

  constructor(private connBackend: ConnBackendService) { }


  // VARIABLES EXTERNAS
  @Input() user_input!: Usuario;
  @Input() user_tarjetas_input!: Array<Tarjeta>;
  @Input() user_transacciones_input!: Transaccion;
  @Input() user_colecciones_input!: Array<Coleccion>;
  @Input() user_materiales_input!: Array<Material>;
  @Input() user_compradores_input!: Array<Comprador>;
  @Input() user_carrito_input!: Array<MaterialCompleto>;
  @Input() user_comprados_input!: Array<MaterialCompleto>;
  @Input() user_material_categorias_input !: Array<MaterialCategoria>;
  @Input() categorias_input !: Array<Categoria>;

  @Output() mensajeSalir = new EventEmitter<string>();
  

  // ABRIR VENTANAS
  async abrirPerfil() {
    var hoja = document.getElementById('hojaPerfil');
    var lista = document.getElementById('listaPerfil');
    await this.cerrarHojas();
    lista?.classList.toggle('active');
    hoja?.classList?.toggle('cerrado');
  }
  async abrirComunidad() {
    var hoja = document.getElementById('hojaComunidad');
    var lista = document.getElementById('listaComunidad');
    await this.cerrarHojas();
    lista?.classList.toggle('active');
    hoja?.classList?.toggle('cerrado');
  }
  async abrirColecciones() {
    var hoja = document.getElementById('hojaColecciones');
    var lista = document.getElementById('listaColecciones');
    await this.cerrarHojas();
    lista?.classList.toggle('active');
    hoja?.classList?.toggle('cerrado');
  }
  async abrirTienda() {
    this.cargando = true;
    var hoja = document.getElementById('hojaTienda');
    var lista = document.getElementById('listaTienda');
    await this.cerrarHojas();
    await this.obtenerMaterialesCompletos();
    this.materialesFisicos = this.materiales_array.filter(
      (material: MaterialCompleto) => material.fisicoMat === 'Si'
    );
    this.materialesDigitales = this.materiales_array.filter(
      (material: MaterialCompleto) => material.electronicoMat === 'Si'
    );
    await this.obtenerCategoriasTienda();
    await this.getColeccionesDisp();
    this.cargando = false;
    lista?.classList.toggle('active');
    hoja?.classList?.toggle('cerrado');
  }
  async abrirMensajes() {
    var hoja = document.getElementById('hojaMensajes');
    var lista = document.getElementById('listaMensajes');
    await this.cerrarHojas();
    lista?.classList.toggle('active');
    hoja?.classList?.toggle('cerrado');
  }
  async cerrarHojas() {
    var hojas = document.getElementsByClassName("hojas");
    for (var i = 0; i < hojas.length; i++) {
      var hoja = hojas[i];
      if (hoja.classList.contains('cerrado')) {
        //Listo
      }
      else {
        hoja.classList.toggle('cerrado');
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
  async getColeccionesDisp() {
    this.filtroColeccion = new Array<Coleccion>();
    const idSet = new Set<string>();
    for(var i=0; i<this.materialesFisicos.length; i++){
      if(!idSet.has(this.materialesFisicos[i].idCol)){
        var coleccion = new Coleccion(this.materialesFisicos[i].idCol, this.materialesFisicos[i].nombreCol.substring(0, 12)+'...', '', '', '');
        idSet.add(coleccion.id_coleccion);
        this.filtroColeccion.push(coleccion);
      }
    }
  }


  // SALIR AL INICIO DE SESIÓN
  async salir() {
    var hoja = document.getElementById('hojaPerfil');
    var lista = document.getElementById('listaPerfil');
    await this.cerrarHojas();
    hoja?.classList.toggle('cerrado');
    lista?.classList.toggle('active');
    this.mensajeSalir.emit('Salir');
  }
  

  // CARGA DE LA PÁGINA
  cargando: boolean = false;


  // ALERTA DE LA PÁGINA
  mostrarAlerta: boolean = false;
  mensajeAlerta: string = '';

  async alerta( mensaje:string ) {
    this.mensajeAlerta = mensaje;
    this.mostrarAlerta = true;
  }
  async continuar() {
    this.mensajeAlerta = '';
    this.mostrarAlerta = false;
  }


  // ACTUALIZAR PERFIL
  recibirActualizar(mensaje:string){
    if(mensaje === 'actualizarPerfil'){
      this.actualizarTodoPerfil();
      this.actualizarTodoColecciones();
    }
  }
  @ViewChild('perfilRef', { static: false }) perfil: PerfilComponent | undefined;
  ngAfterViewInit() {
  }
  actualizarTodoPerfil() {
    if (this.perfil) {
      this.perfil.actualizarTodo();
    }
  }
  @ViewChild('coleccionesRef', { static: false }) colecciones: ColeccionesComponent | undefined;
  actualizarTodoColecciones() {
    if (this.colecciones) {
      this.colecciones.actualizarTodo();
    }
  }


  // COLECCIONES
  user_colecciones: Array<Coleccion> = new Array<Coleccion>();
  materiales_array: Array<MaterialCompleto> = new Array<MaterialCompleto>();
  materialesFisicos: Array<MaterialCompleto> = new Array<MaterialCompleto>();
  filtroColeccion: Array<Coleccion> = new Array<Coleccion>();
  carrito: Array<MaterialCompleto> = new Array<MaterialCompleto>();
  materialesDigitales: Array<MaterialCompleto> = new Array<MaterialCompleto>();
  categorias_tienda: Array<MaterialCategoria> = new Array<MaterialCategoria>();
  



  async obtenerColecciones(){
    try {
      const data = await this.connBackend.getColeccion(this.user_input.id_user).toPromise();
      console.log(data);
      this.user_colecciones = data.coleccion;
    } catch (error) {
      console.error(error);
    }
  }

  async obtenerCategoriasTienda(){
    try {
      const data = await this.connBackend.getCategoriasTienda(this.user_input.id_user).toPromise();
      console.log(data);
      if (data.categoriasTienda.length>0 && data.categoriasTienda){
        this.categorias_tienda = data.categoriasTienda;
      }
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

  async getColecciones() {
    this.cargando = true;
    try {
      await this.obtenerColecciones();
    } catch (error) {
      this.alerta('Error interno del sistema...');
    } finally {
      this.cargando = false;
    }
  }
}
