import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Usuario } from '../../../models/usuario';
import { ConnBackendService } from '../../../services/conn-backend.service';
import { Tarjeta } from '../../../models/tarjeta';
import { Transaccion } from '../../../models/transaccion';
import { Comprador } from '../../../models/comprador';

@Component({
  selector: 'app-perfil',
  templateUrl: './perfil.component.html',
  styleUrl: './perfil.component.css'
})
export class PerfilComponent {

  constructor(private connBackend: ConnBackendService) { }

  // VARIABLES EXTERNAS
  @Input() user_input!: Usuario;
  @Input() user_tarjetas_input!: Array<Tarjeta>;
  @Input() user_transacciones_input!: Transaccion;
  @Input() user_compradores_input!: Array<Comprador>;


  // ABRIR Y CERRAR
  editarUsuario() {
    var hoja = document.getElementById('editarPerfil');
    this.refreshUsuario();
    hoja?.classList.toggle('inactivo');
  }
  abrirPublicaciones() {
    var hoja = document.getElementById('abrirPublicaciones');
    hoja?.classList.toggle('inactivo');
  }
  editarTarjetas() {
    var hoja = document.getElementById('editarTarjetas');
    hoja?.classList.toggle('inactivo');
  }
  abrirTabla() {
    var hoja = document.getElementById('abrirTabla');
    hoja?.classList.toggle('inactivo');
  }
  abrirDetalleTarjeta(id:any) {
    var hoja = document.getElementById(id);
    hoja?.classList.toggle('inactivo');
  }


  // EDICIÓN DE USUARIO
  nombre_user: string  = '';
  aPaterno_user: string = '';
  aMaterno_user: string = '';
  celular_user: string = '';
  direccion_user: string = '';
  correo_user: string = '';
  contra_user: string = '';


  // ACTUALIZACIÓN DE DATOS DEL USUARIO
  async refreshUsuario() {
    this.nombre_user = this.user_input.nom_user;
    this.aPaterno_user = this.user_input.a_pat_user;
    this.aMaterno_user = this.user_input.a_mat_user;
    this.celular_user = this.user_input.cel_user;
    this.correo_user = this.user_input.correo_user;
    this.contra_user = this.user_input.contra_user;
    this.direccion_user = this.user_input.direc_user;
  }
  async update() {
    this.cargando = true;
    try {
      await this.updateUsuario();
    } catch (error) {
      this.alerta('Error interno del sistema...');
    } finally {
      this.cargando = false;
    }
  }
  async updateUsuario() {
    var usuario = new Usuario(this.user_input.id_user, this.nombre_user, this.aPaterno_user, this.aMaterno_user, this.correo_user, this.contra_user, this.celular_user, this.direccion_user);
    var result = await this.guardarUsuario(usuario);
    if (result === 'COMPLETE') {
      this.user_input = usuario;
      this.alerta('Usuario actualizado correctamente...');
      this.cargando = false;
    }
    else {
      this.cargando = false;
      this.alerta(result)
    }
  }
  async guardarUsuario(usuario:Usuario) {
    try {
      const data = await this.connBackend.putUsuario(usuario).toPromise();
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


  // ACTUALIZACIÓN DE DATOS DE LA TARJETA
  monto_recarga: number = 0.0;
  numero_input: string = '';
  caducidad_input: string = '';
  cvv_input: string = '';
  saldo_input: number = 0.0;

  async recargarTarjeta(id:string, monto:number) {
    this.cargando = true;
    try {
      const data = await this.connBackend.recargarTarjeta(id, monto).toPromise();
      if ((data.success === true) && (data.message === 'COMPLETE')) {
        this.monto_recarga = 0.0;
        this.alerta('Se ha recargado la tarjeta solicitada...');
        await this.actualizarTarjetas();
        this.cargando = false;
      }
      else{
        this.cargando = false;
        this.alerta('Hubo un error al recargar la tarjeta...');
      }
    } catch (error) {
      this.cargando = false;
      this.alerta('Error interno del sistema...')
    } finally {
      this.cargando = false;
    }
  }
  async eliminarTarjeta(id:string) {
    this.cargando = true;
    try {
      const data = await this.connBackend.delTarjeta(id).toPromise();
      if ((data.success === true) && (data.message === 'COMPLETE')) {
        this.alerta('Se ha eliminado la tarjeta solicitada...');
        await this.actualizarTarjetas();
      }
      else{
        this.alerta('Hubo un error al eliminar la tarjeta...');
      }
    } catch (error) {
      this.alerta('Error interno del sistema...')
    } finally {
      this.cargando = false;
    }
  }
  async agregarTarjeta() {
    try {
      this.cargando = true;
      const data = await this.connBackend.addTarjeta(this.user_input.id_user, this.numero_input, this.caducidad_input, this.cvv_input, this.saldo_input).toPromise();
      if ((data.success === true) && (data.message === 'COMPLETE')) {
        this.alerta('Se ha registrado correctamente la tarjeta...');
        this.numero_input = '';
        this.caducidad_input = '';
        this.cvv_input = '';
        this.saldo_input = 0.0;
        this.terminarRegistrarTarjeta();
        await this.actualizarTarjetas();
      }
      else{
        this.alerta('Error: '+data.message);
      }
    } catch (error) {
      this.alerta('Error interno del sistema...')
    } finally {
      this.cargando = false;
    }
  }
  async actualizarTarjetas() {
    try {
      this.cargando = true;
      const data = await this.connBackend.getTarjetas(this.user_input.id_user).toPromise();
      console.log(data);
      this.user_tarjetas_input = data.tarjetas;
      if (data.success == true) {
        this.cargando = false;
        return true;
      }
      else {
        this.cargando = false;
        return false;
      }
    } catch (error) {
      this.cargando = false;
      console.error(error);
      return false;
    }
  }
  async cambiarPredeterminado(id_tarjeta:string) {
    try {
      this.cargando = true;
      const data = await this.connBackend.cambiarPredeterminado(this.user_input.id_user, id_tarjeta).toPromise();
      console.log(data);
      if ((data.success == true) && (data.message === 'COMPLETE')) {
        this.alerta('Tarjeta predeterminada cambiada...');
        this.cargando = false;
        await this.actualizarTarjetas();
        return true;
      }
      else {
        this.alerta('Error de actualización...');
        this.cargando = false;
        return false;
      }
    } catch (error) {
      console.error(error);
      this.alerta('Error interno...');
      this.cargando = false;
      return false;
    }
  }


  // MOSTRAR REGISTRO DE TARJETAS
  // Lógica de carga asíncrona  
  mostrarRegistro: boolean = false;

  async registrarTarjeta() {
    this.mostrarRegistro = true;
  }
  async terminarRegistrarTarjeta() {
    this.mostrarRegistro = false;
  }


  // CARGANDO
  cargando: boolean = false;


  // ALERTA
  mostrarAlerta: boolean = false;
  mensajeAlerta: string = '';

  async alerta(mensaje:string) {
    this.mensajeAlerta = mensaje;
    this.mostrarAlerta = true;
  }

  async continuar() {
    this.mostrarAlerta = false;
  }


  // ACTUALIZACIONES
  async actualizarTarjetasBD() {
    this.cargando = true;
    try {
      await this.actualizarTarjetas();
    } catch (error) {
      this.alerta('Error interno del sistema...')
    } finally {
      this.cargando = false;
    }
  }
  async actualizarTransaccionesBD() {
    this.cargando = true;
    try {
      await this.actualizarTransacciones();
    } catch (error) {
      this.alerta('Error interno del sistema...')
    } finally {
      this.cargando = false;
    }
  }
  async actualizarTransacciones(){
    try {
      this.cargando = true;
      const data = await this.connBackend.getTransaccion(this.user_input.id_user).toPromise();
      console.log(data);
      var transacciones: Array<Transaccion> = data.transaccion;
      if (transacciones && (transacciones.length > 0)) {
        this.user_transacciones_input = transacciones[0];
        return true;
      }
      else {
        this.user_transacciones_input = new Transaccion('0', '0', '0');
        return false;
      }
    } catch (error) {
      console.error(error);
      this.user_transacciones_input = new Transaccion('0', '0', '0');
      return false;
    }
  }
  async actualizarCompradoresBD() {
    this.cargando = true;
    try {
      await this.actualizarCompradores();
    } catch (error) {
      this.alerta('Error interno del sistema...')
    } finally {
      this.cargando = false;
    }
  }
  async actualizarCompradores(){
    try {
      this.cargando = true;
      const data = await this.connBackend.getCompradores(this.user_input.id_user).toPromise();
      console.log(data);
      var compradores: Array<Comprador> = data.compradores;
      if (compradores && (compradores.length > 0)) {
        this.user_compradores_input = compradores;
        return true;
      }
      else {
        this.user_compradores_input = new Array<Comprador>();
        return false;
      }
    } catch (error) {
      console.error(error);
      this.user_compradores_input = new Array<Comprador>();
      return false;
    }
  }
  async actualizarTodo(){
    try {
      this.cargando = true;
      await this.refreshUsuario();
      await this.actualizarTarjetasBD();
      await this.actualizarCompradoresBD();
      await this.actualizarTransaccionesBD();
      this.cargando = false;
    } catch (error) {
      console.error(error);
      this.cargando = false;
    }
  }
}
