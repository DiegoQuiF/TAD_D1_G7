import { Component, EventEmitter, Output } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ConnBackendService } from '../../services/conn-backend.service';
import { Usuario } from '../../models/usuario';
import { Tarjeta } from '../../models/tarjeta';
import { Coleccion } from '../../models/coleccion';
import { Transaccion } from '../../models/transaccion';
import { Comprador } from '../../models/comprador';
import { Material } from '../../models/material';
import { MaterialCompleto } from '../../models/material-completo';
import { MaterialCategoria } from '../../models/material-categoria';
import { Categoria } from '../../models/categoria';

@Component({
  selector: 'app-login-register',
  templateUrl: './login-register.component.html',
  styleUrl: './login-register.component.css'
})

export class LoginRegisterComponent {

  constructor( private connBackend: ConnBackendService ) { }

  // VARIABLES EXTERNAS
  @Output() user_log = new EventEmitter<Usuario>();
  @Output() user_tarjetas_log = new EventEmitter<Array<Tarjeta>>();
  @Output() user_transacciones_log = new EventEmitter<Transaccion>();
  @Output() user_compradores_log = new EventEmitter<Array<Comprador>>();
  @Output() user_colecciones_log = new EventEmitter<Array<Coleccion>>();
  @Output() user_materiales_log = new EventEmitter<Array<Material>>();
  @Output() user_carrito_log = new EventEmitter<Array<MaterialCompleto>>();
  @Output() user_comprados_log = new EventEmitter<Array<MaterialCompleto>>();
  @Output() user_material_categorias_log = new EventEmitter<Array<MaterialCategoria>>();
  @Output() categorias_log = new EventEmitter<Array<Categoria>>();
  @Output() mensaje_log = new EventEmitter<string>();


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


  // TRANSICIÓN ENTRE INICIO DE SESIÓN Y REGISTRO
  in_btn() {    // REGISTRARSE → INICIAR SESIÓN
    const container = document.getElementById("container-form");
    container?.classList.remove("sign-up-mode");
  }

  up_btn() {    // INICIAR SESIÓN → REGISTRARSE
    const container = document.getElementById("container-form");
    container?.classList.add("sign-up-mode");
  }


  // INICIO DE SESIÓN (CREDENCIALES POR DEFECTO)
  user_correo = 'pedrito@gmail.com';
  user_contra = 'pedrito123';
  user: Usuario = new Usuario('', '', '', '', '', '', '', '');
  user_tarjetas: Array<Tarjeta> = new Array<Tarjeta>();
  user_transacciones: Transaccion = new Transaccion('0', '0', '0');
  user_colecciones: Array<Coleccion> = new Array<Coleccion>();
  user_materiales: Array<Material> = new Array<Material>();
  user_compradores: Array<Comprador> = new Array<Comprador>();
  user_carrito: Array<MaterialCompleto> = new Array<MaterialCompleto>();
  user_comprados: Array<MaterialCompleto> = new Array<MaterialCompleto>();
  user_material_categorias: Array<MaterialCategoria> = new Array<MaterialCategoria>();
  categorias: Array<Categoria> = new Array<Categoria>;

  async login( correo: string, contra: string ) {
    this.cargando = true;
    try {
      await this.iniciarSesion(correo, contra);
    } catch (error) {
      console.error(error);
      this.alerta('Hubo un error al intentar iniciar sesión...');
    } finally {
      this.cargando = false;
    }
  }
  async iniciarSesion( correo: string, contra: string ) {
    if ((correo === 'ADMIN') && (contra === 'ADMIN')) {
      this.mensaje_log.emit('Admin');
    }
    else {
      this.user = await this.getUsuario(correo, contra);
      if (this.user.id_user !== '') {
        this.user_tarjetas = await this.getTarjetas(this.user.id_user);
        this.user_colecciones = await this.getColecciones(this.user.id_user);
        this.user_materiales = await this.getMateriales(this.user.id_user);
        this.user_transacciones = await this.getTransacciones(this.user.id_user);
        this.user_compradores = await this.getCompradores(this.user.id_user);
        this.user_carrito = await this.getCarrito(this.user.id_user);
        this.user_comprados = await this.getComprados(this.user.id_user);
        this.user_material_categorias = await this.getMaterialCategoria(this.user.id_user);
        this.categorias = await this.getCategorias();
        this.user_correo = '';
        this.user_contra = '';
        this.user_log.emit(this.user);
        this.user_tarjetas_log.emit(this.user_tarjetas);
        this.user_transacciones_log.emit(this.user_transacciones);
        this.user_colecciones_log.emit(this.user_colecciones);
        this.user_compradores_log.emit(this.user_compradores);
        this.user_materiales_log.emit(this.user_materiales);
        this.user_carrito_log.emit(this.user_carrito);
        this.user_comprados_log.emit(this.user_comprados);
        this.user_material_categorias_log.emit(this.user_material_categorias);
        this.categorias_log.emit(this.categorias);
        this.mensaje_log.emit('Logueado');
      } else {
        this.alerta('No se ha encontrado al usuario con las credenciales proporcionadas...');
      }
    }
  }
  async getUsuario( correo:string, contra: string ) {
    try {
      const data = await this.connBackend.getUsuario(correo, contra).toPromise();
      console.log(data);
      var usuarios: Array<Usuario> = data.usuario;
      if ((usuarios.length > 0) && usuarios) {
        return usuarios[0];
      }
      else {
        return new Usuario('', '', '', '', '', '', '', '');
      }
    } catch (error) {
      console.error(error);
      return new Usuario('', '', '', '', '', '', '', '');
    }
  }
  async getTarjetas( id:string ) {
    try {
      const data = await this.connBackend.getTarjetas(id).toPromise();
      console.log(data);
      var tarjetas: Array<Tarjeta> = data.tarjetas;
      if ( data.success == true ) {
        if ( tarjetas.length > 0 && tarjetas ) {
          return tarjetas;
        }
        else {
          return new Array<Tarjeta>();
        }
      }
      else {
        return new Array<Tarjeta>();
      }
    } catch (error) {
      console.error(error);
      return new Array<Tarjeta>();
    }
  }
  async getColecciones( id:string ) {
    try {
      const data = await this.connBackend.getColeccion(id).toPromise();
      console.log(data);
      var colecciones: Array<Coleccion> = data.coleccion;
      if ( data.success == true ) {
        if ( colecciones.length > 0 && colecciones ) {
          return colecciones;
        }
        else {
          return new Array<Coleccion>();
        }
      }
      else {
        return new Array<Coleccion>();
      }
    } catch (error) {
      console.error(error);
      return new Array<Coleccion>();
    }
  }
  async getMateriales( id:string ) {
    try {
      const data = await this.connBackend.getMaterial(id).toPromise();
      console.log(data);
      var materiales: Array<Material> = data.material;
      if ( data.success == true ) {
        if ( materiales.length > 0 && materiales ) {
          return materiales;
        }
        else {
          return new Array<Material>();
        }
      }
      else {
        return new Array<Material>();
      }
    } catch (error) {
      console.error(error);
      return new Array<Material>();
    }
  }
  async getTransacciones( id:string ) {
    try {
      const data = await this.connBackend.getTransaccion(id).toPromise();
      console.log(data);
      var transaccion: Array<Transaccion> = data.transaccion;
      if ((transaccion.length > 0) && transaccion) {
        return transaccion[0];
      }
      else {
        return new Transaccion('0', '0', '0');
      }
    } catch (error) {
      console.error(error);
      return new Transaccion('0', '0', '0');
    }
  }
  async getCompradores( id:string ) {
    try {
      const data = await this.connBackend.getCompradores(id).toPromise();
      console.log(data);
      var compradores: Array<Comprador> = data.compradores;
      if ((compradores.length > 0) && compradores) {
        return compradores;
      }
      else {
        return new Array<Comprador>();
      }
    } catch (error) {
      console.error(error);
      return new Array<Comprador>();
    }
  }
  async getCarrito( id:string ) {
    try {
      const data = await this.connBackend.getCarrito(id).toPromise();
      console.log(data);
      var carrito: Array<MaterialCompleto> = data.carrito;
      if(carrito.length > 0 && carrito){
        return carrito;
      }
      else {
        return new Array<MaterialCompleto>();
      }
    } catch (error) {
      console.error(error);
      return new Array<MaterialCompleto>();
    }
  }
  async getComprados( id:string ) {
    try {
      const data = await this.connBackend.getComprados(id).toPromise();
      console.log(data);
      var comprados: Array<MaterialCompleto> = data.comprados;
      if(comprados.length > 0 && comprados){
        return comprados;
      }
      else {
        return new Array<MaterialCompleto>();
      }
    } catch (error) {
      console.error(error);
      return new Array<MaterialCompleto>();
    }
  }
  async getMaterialCategoria( id:string ) {
    try {
      const data = await this.connBackend.getMaterialCategoria(id).toPromise();
      console.log(data);
      var materialCategorias: Array<MaterialCategoria> = data.materialCategorias;
      if(materialCategorias.length > 0 && materialCategorias){
        return materialCategorias;
      }
      else {
        return new Array<MaterialCategoria>();
      }
    } catch (error) {
      console.error(error);
      return new Array<MaterialCategoria>();
    }
  }
  async getCategorias( ) {
    try {
      const data = await this.connBackend.getCategorias().toPromise();
      console.log(data);
      var categorias: Array<Categoria> = data.categorias;
      if(categorias.length > 0 && categorias){
        return categorias;
      }
      else {
        return new Array<Categoria>();
      }
    } catch (error) {
      console.error(error);
      return new Array<Categoria>();
    }
  }


  // REGISTRARSE
  nombre_reg: string = '';
  aPat_reg: string = '';
  aMat_reg: string = '';
  celular_reg: string = '';
  correo_reg: string = '';
  contra_reg: string = '';
  direccion_reg: string = '';

  patronLargo80 = /^(.){0,80}$/;
  patronLargo160 = /^(.){0,160}$/;
  patronContra = /^(.){8,80}$/;
  patronNombresPropios = /^[A-Z]([A-Z]|[a-z]|\s)*$/;
  patronCorreo = /^([a-z]|[A-Z]|\_|\.)+\@[a-zA-Z]+\.[a-zA-Z]+(\.([a-zA-Z])+)*$/;
  patronCelular = /^(9)(\d{8})$/;
  patronDireccion = /^([A-Z]|[a-z]|\s|\.|\d|\_)+$/;

  async register(nombre: string, aPat: string, aMat: string, celular: string, correo: string,
    contra: string, direccion:string) {
    this.cargando = true;
    try {
      await this.registrarse(nombre, aPat, aMat, celular, correo, contra, direccion);
    } catch (error) {
      console.error(error);
      this.alerta('Hubo un error al intentar registrarse en la aplicación...');
    } finally {
      this.cargando = false;
    }
  }
  async registrarse(nombre: string, aPat: string, aMat: string, celular: string, correo:string,
    contra: string, direccion:string) {
    var result = await this.postUsuario(nombre, aPat, aMat, celular, correo, contra, direccion);
    if (result === 'COMPLETE') {
      this.alerta('Usuario registrado correctamente...');
      // Se autocompletan las credenciales del usuario recien registrado
      this.user_correo = this.correo_reg;
      this.user_contra = this.contra_reg;
      // Se limpia todos los datos de registro
      this.nombre_reg = '';
      this.aPat_reg = '';
      this.aMat_reg = '';
      this.celular_reg = '';
      this.correo_reg = '';
      this.contra_reg = '';
      this.direccion_reg = '';
      // Se abre la ventana de login con las credenciales recien registradas
      this.in_btn();
    }
    else {
      this.alerta(result);
    }
  }
  async postUsuario(nombre: string, aPat: string, aMat: string, celular: string, correo: string,
    contra: string, direccion:string) {
    try {
      const data = await this.connBackend.postUsuario(nombre, aPat, aMat, correo, contra, celular, direccion).toPromise();
      console.log(data);
      if (data.success === true) {
        return data.message;
      }
      else {
        return 'Error interno del sistema...';
      }
    } catch (error) {
      console.error(error);
      return 'Error interno del sistema...';
    }
  }
}
