import { Component, Input } from '@angular/core';
import { Usuario } from '../../../models/usuario';
import { ConnBackendService } from '../../../services/conn-backend.service';
import { Tarjeta } from '../../../models/tarjeta';

@Component({
  selector: 'app-perfil',
  templateUrl: './perfil.component.html',
  styleUrl: './perfil.component.css'
})
export class PerfilComponent {
  @Input() user_input!: Usuario;
  @Input() tarjeta_input!: Array<Tarjeta>;
  nombre_user: string  = '';
  aPaterno_user: string = '';
  aMaterno_user: string = '';
  celular_user: string = '';
  correo_user: string = '';
  contra_user: string = '';
  direccion_user: string = '';
  
  monto_recarga: number = 0.0;

  numero_input: string = '';
  caducidad_input: string = '';
  cvv_input: string = '';
  saldo_input: number = 0.0;

  // mostrar alerta
  isAlert: boolean = false;
  mensajeAlert: string = '';

  constructor(private connBackend: ConnBackendService) { }

  editarUsuario() {
    var hoja = document.getElementById('editarPerfil');
    this.refreshUsuario();
    hoja?.classList.toggle('inactivo');
  }

  refreshUsuario() {
    this.nombre_user = this.user_input.nom_user;
    this.aPaterno_user = this.user_input.a_pat_user;
    this.aMaterno_user = this.user_input.a_mat_user;
    this.celular_user = this.user_input.cel_user;
    this.correo_user = this.user_input.correo_user;
    this.contra_user = this.user_input.contra_user;
    this.direccion_user = this.user_input.direc_user;
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

  
  async updateUsuario() {
    var usuario = new Usuario(this.user_input.id_user, this.nombre_user, this.aPaterno_user, this.aMaterno_user, this.correo_user, this.contra_user, this.celular_user, this.direccion_user);
    var result = await this.guardarUsuario(usuario);
    if (result == 'COMPLETE') {
      this.user_input = usuario;
      this.alert('Usuario actualizado correctamente...');
    }
    else {
      this.alert('Error: '+result)
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
        return 'Error interno del sistema';
      }
    } catch (error) {
      console.error(error);
      return 'Error interno del sistema'
    }
  }

  async eliminarTarjeta(id:string) {
    this.isLoading = true;
    try {
      const data = await this.connBackend.delTarjeta(id).toPromise();
      if ((data.success === true) && (data.message === 'COMPLETE')) {
        this.alert('Se ha eliminado la tarjeta solicitada...');
        await this.actualizarTarjetas();
      }
      else{
        this.alert('Hubo un error al eliminar la tarjeta...');
      }
    } catch (error) {
      this.alert('Error interno del sistema...')
    } finally {
      this.isLoading = false;
    }
  }

  async recargarTarjeta(id:string, monto:number) {
    this.isLoading = true;
    try {
      const data = await this.connBackend.recargarTarjeta(id, monto).toPromise();
      if ((data.success === true) && (data.message === 'COMPLETE')) {
        this.monto_recarga = 0.0;
        this.alert('Se ha recargado la tarjeta solicitada...');
        await this.actualizarTarjetas();
      }
      else{
        this.alert('Hubo un error al recargar la tarjeta...');
      }
    } catch (error) {
      this.alert('Error interno del sistema...')
    } finally {
      this.isLoading = false;
    }
  }

  async registrarTarjeta() {
    this.isRegister = true;
  }

  async terminarRegistrarTarjeta() {
    this.isRegister = false;
  }

  async agregarTarjeta() {
    try {
      this.isLoading = true;
      const data = await this.connBackend.addTarjeta(this.user_input.id_user, this.numero_input, this.caducidad_input, this.cvv_input, this.saldo_input).toPromise();
      if ((data.success === true) && (data.message === 'COMPLETE')) {
        this.alert('Se ha registrado correctamente la tarjeta...');
        this.numero_input = '';
        this.caducidad_input = '';
        this.cvv_input = '';
        this.saldo_input = 0.0;
        this.terminarRegistrarTarjeta();
        await this.actualizarTarjetas();
      }
      else{
        this.alert('Error: '+data.message);
      }
    } catch (error) {
      this.alert('Error interno del sistema...')
    } finally {
      this.isLoading = false;
    }
  }

  async actualizarTarjetas() {
    try {
      this.isLoading = true;
      const data = await this.connBackend.getTarjetas(this.user_input.id_user).toPromise();
      console.log(data);
      this.tarjeta_input = data.tarjetas;
      if (data.success == true) {
        this.isLoading = false;
        return true;
      }
      else {
        this.isLoading = false;
        return false;
      }
    } catch (error) {
      console.error(error);
      this.isLoading = false;
      return false;
    }
  }

  async cambiarPredeterminado(id_tarjeta:string) {
    try {
      this.isLoading = true;
      const data = await this.connBackend.cambiarPredeterminado(this.user_input.id_user, id_tarjeta).toPromise();
      console.log(data);
      if ((data.success == true) && (data.message === 'COMPLETE')) {
        this.alert('Tarjeta predeterminada cambiada...');
        this.isLoading = false;
        await this.actualizarTarjetas();
        return true;
      }
      else {
        this.alert('Error de actualización...');
        this.isLoading = false;
        return false;
      }
    } catch (error) {
      console.error(error);
      this.alert('Error interno...');
      this.isLoading = false;
      return false;
    }
  }



  // Lógica de carga asíncrona
  isLoading: boolean = false;
  isRegister: boolean = false;

  async update() {
    this.isLoading = true;
    try {
      await this.updateUsuario();
    } catch (error) {
      this.alert('Error interno del sistema...');
    } finally {
      this.isLoading = false;
    }
  }

  async alert(mensaje:string) {
    this.mensajeAlert = mensaje;
    this.isAlert = true;
  }

  async continuar() {
    this.isAlert = false;
  }
}
