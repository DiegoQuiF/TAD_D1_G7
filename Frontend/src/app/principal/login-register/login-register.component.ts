import { Component, EventEmitter, Output } from '@angular/core';
import { FormsModule } from '@angular/forms';

// Servicios
import { ConnBackendService } from '../../services/conn-backend.service';

//Modelos
import { Usuario } from '../../models/usuario';


@Component({
  selector: 'app-login-register',
  templateUrl: './login-register.component.html',
  styleUrl: './login-register.component.css'
})


export class LoginRegisterComponent {

  constructor(private connBackend: ConnBackendService) { }

  // Variables de inicio de sesión
  correo_user = 'pedrito@gmail.com';      // Correo ingresado por el usuario
  contra_user = 'pedrito';                // Contraseña ingresada por el usuario
  usuario_login: Array<Usuario> = new Array<Usuario>();

  // Variables de registro
  nombre_reg: string = '';
  aPat_reg: string = '';
  aMat_reg: string = '';
  celular_reg: string = '';
  correo_reg: string = '';
  contra_reg: string = '';

  // Variables globales
  @Output() mensajeEnviado = new EventEmitter<string>();
  @Output() usuarioLogin = new EventEmitter<Usuario>();

  //Validar campos del register desde el front
  patronNombresPropios = /^[A-Z]([A-Z]|[a-z]|\s){0,49}$/;
  patronCorreo = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  patronCaracteresLibres = /^(.{1,50})$/;
  patronCelular = /^(9)(\d{8})$/;



  // Transiciones
  in_btn() {    // Tansición entre el formulario REGISTRARSE → INICIAR SESIÓN
    const container = document.getElementById("container-form");
    container?.classList.remove("sign-up-mode");
  }

  up_btn() {    // Transición entre el formulario INICIAR SESIÓN → REGISTRARSE
    const container = document.getElementById("container-form");
    container?.classList.add("sign-up-mode");
  }



  // Login - Inicio Sesión
  async validar_inicioSesion(correo_input: string, contra_input: string) {    // Realiza una acción si se encuentra o no al usuario
    if (await this.getUsuario_inicioSesion(correo_input, contra_input)) {
      this.usuarioLogin.emit(this.usuario_login[0]);
      this.mensajeEnviado.emit('Abrir logged');
      this.correo_user = '';
      this.contra_user = '';
    }
    else {
      alert('Usuario no encontrado');
    }
  }

  async getUsuario_inicioSesion(correo: string, contra: string) {   // Retorna true si el usuario existe, false si no existe u ocurre un error
    try {
      const data = await this.connBackend.getUsuario(correo, contra).toPromise();   // Mediante servicio backend consulta la existencia del usuario
      console.log(data);
      this.usuario_login = data.usuario;    // Obtiene el campo usuario de la data obtenida, si no se encontró un usuario sera vacio
      if (this.usuario_login.length > 0 && this.usuario_login) {    // Si el usuario existe retorna true, si no se encontró retorna falso
        return true;
      }
      else {
        return false;
      }
    } catch (error) {   // Capta los errores durante ejecución
      console.error(error);
      return false;
    }
  }



  // Register - Registro
  async registrar_registro(nombre_input: string, aPat_input: string, aMat_input: string, celular_input: string, correo_input: string, contra_input: string) {    // Realiza una acción si se logra registrar al usuario o no
    if (await this.postUsuario_registro(nombre_input, aPat_input, aMat_input, celular_input, correo_input, contra_input)) {
      alert("Usuario registrado correctamente");
      // Se autocompletan las credenciales del usuario recien registrado
      this.correo_user = this.correo_reg;
      this.contra_user = this.contra_reg;
      // Se limpia todos los datos de registro
      this.nombre_reg = '';
      this.aPat_reg = '';
      this.aMat_reg = '';
      this.celular_reg = '';
      this.correo_reg = '';
      this.contra_reg = '';
      // Se abre la ventana de login con las credenciales recien registradas
      this.in_btn();
    }
    else {
      alert('Error en el registro de datos:\n- Verifique la sintaxis en los campos asociados.\n- Verifique el Nro de celular o correo, puede que estén en uso.');
    }
  }

  async postUsuario_registro(nombre: string, aPat: string, aMat: string, celular: string, correo: string, contra: string) {   // Retorna true si el usuario fue registrado, false si no se registro u ocurrio un error
    try {
      const data = await this.connBackend.postUsuario(nombre, aPat, aMat, correo, contra, celular).toPromise();   // Mediante servicio backend se intenta registrar al usuario
      console.log(data);
      if (data.usuario.length > 0 && data.usuario) {    // Si el usuario se registro correctamente, el backend habría retornado un campo usuario por lo que retorna true, caso contrario retorna false
        return true;
      }
      else {
        return false;
      }
    } catch (error) {   // Capta los errores durante ejecución
      console.error(error);
      return false;
    }
  }


  // Lógica de carga asíncrona
  isLoading: boolean = false;

  async login(correo_input: string, contra_input: string) {
    this.isLoading = true;
    try {
      await this.validar_inicioSesion(correo_input, contra_input);
    } catch (error) {
      alert('Hubo un error al iniciar sesión...')
    } finally {
      this.isLoading = false;
    }
  }

  async register(nombre_input: string, aPat_input: string, aMat_input: string, celular_input: string, correo_input: string, contra_input: string) {
    this.isLoading = true;
    try {
      await this.registrar_registro(nombre_input, aPat_input, aMat_input, celular_input, correo_input, contra_input);
    } catch (error) {
      console.error('Hubo un error al registrarse...', error);
    } finally {
      this.isLoading = false;
    }
  }
}
