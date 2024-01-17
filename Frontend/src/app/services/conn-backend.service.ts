import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'
import { Usuario } from '../models/usuario';

@Injectable({
  providedIn: 'root'
})
export class ConnBackendService {

  //private BASE_URL = 'https://paginatad01.onrender.com';
  private BASE_URL = 'http://127.0.0.1:5000'
  constructor(private http:HttpClient) { }

  getUsuarios():Observable<any>{
    return this.http.get(`${this.BASE_URL}/getUsuarios`);
  }

  getUsuario(correo:string, contra:string):Observable<any>{
    return this.http.get(`${this.BASE_URL}/getUsuario/${correo}/${contra}`)
  }


  postUsuario(nombre_u:string, aPat:string, aMat:string, correo_u:string, contra_u:string, celular_u:string): Observable<any>{
    const data = {
      nombre: nombre_u,
      paterno: aPat,
      materno: aMat,
      correo: correo_u,
      contra: contra_u,
      celular: celular_u
    }
    return this.http.post(`${this.BASE_URL}/registrarUsuario`, data);
  }

  putUsuario(usuario: Usuario): Observable<any> {
    const data = {
      nombre: usuario.nom_user,
      paterno: usuario.a_pat_user,
      materno: usuario.a_mat_user,
      correo: usuario.correo_user,
      contra: usuario.contra_user,
      celular: usuario.cel_user,
      id: usuario.id_user
    }
    return this.http.put(`${this.BASE_URL}/guardarUsuario`, data);
  }

  deleteUsuario(id:string):Observable<any>{
    return this.http.delete(`${this.BASE_URL}/eliminarUsuario/${id}`)
  }
}
