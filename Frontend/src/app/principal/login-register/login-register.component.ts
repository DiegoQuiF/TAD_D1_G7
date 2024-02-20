import { Component, EventEmitter, Output } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ConnBackendService } from '../../services/conn-backend.service';
import { Usuario } from '../../models/usuario';
import { Tarjeta } from '../../models/tarjeta';
import { Coleccion } from '../../models/coleccion';

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
  @Output() user_colecciones_log = new EventEmitter<Array<Coleccion>>();
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
  user: undefined | Usuario;
  user_tarjetas: undefined | Array<Tarjeta>;
  user_colecciones: undefined | Array<Coleccion>;

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

      if (this.user !== undefined) {
        this.user_tarjetas = await this.getTarjetas(this.user.id_user);
        this.user_colecciones = await this.getColecciones(this.user.id_user);
        this.user_correo = '';
        this.user_contra = '';
        this.user_log.emit(this.user);
        this.user_tarjetas_log.emit(this.user_tarjetas);
        this.user_colecciones_log.emit(this.user_colecciones);
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
        return undefined;
      }
    } catch (error) {
      console.error(error);
      return undefined;
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
          return undefined;
        }
      }
      else {
        return undefined;
      }
    } catch (error) {
      console.error(error);
      return undefined;
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
          return undefined;
        }
      }
      else {
        return undefined;
      }
    } catch (error) {
      console.error(error);
      return undefined;
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
