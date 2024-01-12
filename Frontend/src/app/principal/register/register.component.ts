import { Component, EventEmitter, Output } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ConnBackendService } from '../../services/conn-backend.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrl: './register.component.css'
})
export class RegisterComponent {
  @Output() mensajeEnviadoVolver = new EventEmitter<string>();
  
  constructor(private connBackend: ConnBackendService) { }

  nombre_user: string = '';
  aPat_user: string = '';
  aMat_user: string = '';
  correo_user: string = '';
  contra_user: string = '';
  celular_user: string = '';

  async registrarUsuario(nom:string, pat:string, mat:string, cor:string, con:string, cel:string) {
    if (await this.postUsuario(nom, pat, mat, cor, con, cel)) {
      alert("USUARIO REGISTRADO CORRECTAMENTE");
      this.enviarMensaje();
    }
    else {
      alert("ERROR EN EL INGRESO DE DATOS");
    }
  }

  async postUsuario(nom:string, pat:string, mat:string, cor:string, con:string, cel:string){
    const data = await this.connBackend.postUsuario(nom, pat, mat, cor, con, cel).toPromise();
    console.log(data);
    if(data.usuario && data.usuario.length > 0){
      return true;
    }
    else {
      return false;
    }
  }

  enviarMensaje(){
    this.mensajeEnviadoVolver.emit('Abrir login');
  }
}
