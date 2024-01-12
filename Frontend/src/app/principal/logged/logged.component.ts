import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

import { Usuario } from '../../models/usuario';
import { ConnBackendService } from '../../services/conn-backend.service';

@Component({
  selector: 'app-logged',
  templateUrl: './logged.component.html',
  styleUrl: './logged.component.css'
})
export class LoggedComponent {
  @Input() user_input!: Usuario;

  user_array: Array<Usuario> = new Array<Usuario>();
  user_select: Usuario = new Usuario('-', '-', '-', '-', '-', '-', '-');

  opciones: NodeListOf<Element> | undefined;

  constructor(private connBackend: ConnBackendService) { }

  async verUsuarios(){
    if (await this.getUsuarios()) {
      var guardadito = document.getElementById('Guardado');
      var eliminadito = document.getElementById('Eliminado');
      eliminadito?.classList.remove('abierto');
      eliminadito?.classList.remove('cerrado');
      eliminadito?.classList.add('cerrado');

      guardadito?.classList.remove('abierto');
      guardadito?.classList.remove('cerrado');
      guardadito?.classList.add('cerrado');

      this.user_select = new Usuario('-', '-', '-', '-', '-', '-', '-');

      alert("DATOS ACTUALIZADOS CORRECTAMENTE");
    }
    else {
      alert("ERROR INTERNO");
    }
  }


  async getUsuarios(){
    try{
      const data = await this.connBackend.getUsuarios().toPromise();
      this.user_array = data.usuarios;
    } catch(error) {
      console.error(error);
      return false;
    }
    return true;
  }

  seleccionarUsuario(usuario: Usuario) {
    this.user_select = usuario;
    alert('USUARIO SELECCIONADO:\n- Nombre: ' + this.user_select.nom_user +
      '\n- Apellidos: ' + this.user_select.a_pat_user + ' ' + this.user_select.a_mat_user +
      '\n- Correo: ' + this.user_select.correo_user +
      '\n- Num. celular: ' + this.user_select.cel_user);
  }

  async regUpdateUsuario(usuario: Usuario) {
    if (await this.guardarUsuario(usuario)) {
      var guardadito = document.getElementById('Guardado');
      var eliminadito = document.getElementById('Eliminado');
      eliminadito?.classList.remove('abierto');
      eliminadito?.classList.remove('cerrado');
      eliminadito?.classList.add('cerrado');

      guardadito?.classList.remove('abierto');
      guardadito?.classList.remove('cerrado');
      guardadito?.classList.add('cerrado');

      alert("USUARIO ACTUALIZADO CORRECTAMENTE");
    }
    else {
      alert("ERROR EN EL INGRESO DE DATOS");
    }
  }

  async eliminarUsuario(usuario: Usuario) {
    if (await this.eliminaUsuario(usuario)) {

      var guardadito = document.getElementById('Guardado');
      var eliminadito = document.getElementById('Eliminado');
      eliminadito?.classList.remove('abierto');
      eliminadito?.classList.remove('cerrado');
      eliminadito?.classList.add('cerrado');

      guardadito?.classList.remove('abierto');
      guardadito?.classList.remove('cerrado');
      guardadito?.classList.add('cerrado');

      alert("USUARIO ELIMINADO CORRECTAMENTE");
    }
    else {
      alert("ERROR EN LA ELIMINACIÓN DEL USUARIO");
    }
  }

  async guardarUsuario(usuario:Usuario) {
    const data = await this.connBackend.putUsuario(usuario).toPromise();
    if(data.usuario && data.usuario.length > 0){
      await this.getUsuarios();
      return true;
    }
    else {
      return false;
    }
  }

  async eliminaUsuario(usuario:Usuario) {
    const data = await this.connBackend.deleteUsuario(usuario.id_user).toPromise();
    if(data.usuario && data.usuario.length > 0){
      this.user_select = new Usuario('-', '-', '-', '-', '-', '-', '-');
      await this.getUsuarios();
      return true;
    }
    else {
      return false;
    }
  }

  guardado() {
    if (this.user_select.id_user != "-"){
      var guardadito = document.getElementById('Guardado');
      var eliminadito = document.getElementById('Eliminado');
      guardadito?.classList.remove('abierto');
      guardadito?.classList.remove('cerrado');
      guardadito?.classList.add('abierto');

      eliminadito?.classList.remove('abierto');
      eliminadito?.classList.remove('cerrado');
      eliminadito?.classList.add('cerrado');
    }
    else {
      alert("SELECCIONE UN USUARIO");
    }
  }

  eliminado() {
    if (this.user_select.id_user != "-"){
      var guardadito = document.getElementById('Guardado');
      var eliminadito = document.getElementById('Eliminado');
      eliminadito?.classList.remove('abierto');
      eliminadito?.classList.remove('cerrado');
      eliminadito?.classList.add('abierto');

      guardadito?.classList.remove('abierto');
      guardadito?.classList.remove('cerrado');
      guardadito?.classList.add('cerrado');
    }
    else {
      alert("SELECCIONE UN USUARIO");
    }
}



}
