import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'
import { Usuario } from '../models/usuario';
import { Coleccion } from '../models/coleccion';
import { Material } from '../models/material';

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

  getMaterialesCompletos(id:string):Observable<any>{
    return this.http.get(`${this.BASE_URL}/getMaterialesCompletos/${id}`);
  }

  getUsuario(correo:string, contra:string):Observable<any>{
    const data = {
      correo_user: correo,
      contra_user: contra
    }
    return this.http.post(`${this.BASE_URL}/getUsuario`, data);
  }

  getLibros(id:string):Observable<any>{
    const data = {
      id_coleccion: id
    }
    return this.http.post(`${this.BASE_URL}/getMaterial`, data);
  }

  getColeccion(id:string):Observable<any>{
    const data = {
      id_user: id
    }
    return this.http.post(`${this.BASE_URL}/getColeccion`, data);
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

  postColeccion(id_user:string, nombre_col:string, tipo_col:string): Observable<any>{
    const hoy = new Date();
    const dia = hoy.getDate().toString().padStart(2, '0');
    const mes = (hoy.getMonth() + 1).toString().padStart(2, '0');
    const anio = hoy.getFullYear().toString();
    const data = {
      id_user: id_user,
      nombre_col: nombre_col,
      tipo_col: tipo_col,
      creacion_col: `${dia}/${mes}/${anio}`,
      actualizacion_col: `${dia}/${mes}/${anio}`
    }
    return this.http.post(`${this.BASE_URL}/registrarColeccion`, data)
  }

  postMaterial(material:Material, id:string): Observable<any>{
    const hoy = new Date();
    const dia = hoy.getDate().toString().padStart(2, '0');
    const mes = (hoy.getMonth() + 1).toString().padStart(2, '0');
    const anio = hoy.getFullYear().toString();

    const data = {
      titulo: material.titulo,
      autor: material.autor,
      hoy: `${dia}/${mes}/${anio}`,
      idioma: material.idioma,
      procedencia: material.procedencia,
      fechaO: material.original,
      electronico: material.electronico,
      precioE: material.precioE,
      fisico: material.fisico,
      precioF: material.precioF,
      stockF: material.stockF,
      id_coleccion: id
    }
    return this.http.post(`${this.BASE_URL}/registrarLibro`, data)
  }

  postFactura(idMaterial:string, idUsuario:string): Observable<any>{
    const hoy = new Date();
    const dia = hoy.getDate().toString().padStart(2, '0');
    const mes = (hoy.getMonth() + 1).toString().padStart(2, '0');
    const anio = hoy.getFullYear().toString();
    const data = {
      pagado: "No",
      fecha: `${dia}/${mes}/${anio}`,
      id_material: idMaterial,
      id_usuario: idUsuario
    }
    return this.http.post(`${this.BASE_URL}/registrarFactura`, data)
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

  putColeccion(coleccion: Coleccion): Observable<any> {
    const hoy = new Date();
    const dia = hoy.getDate().toString().padStart(2, '0');
    const mes = (hoy.getMonth() + 1).toString().padStart(2, '0');
    const anio = hoy.getFullYear().toString();
    const data = {
      id_coleccion: coleccion.id_col,
      nombre_coleccion: coleccion.nombre_col,
      tipo_coleccion: coleccion.tipo_col,
      actualizacion_coleccion: `${dia}/${mes}/${anio}`
    }
    return this.http.put(`${this.BASE_URL}/guardarColeccion`, data);
  }

  deleteUsuario(id:string):Observable<any>{
    return this.http.delete(`${this.BASE_URL}/eliminarUsuario/${id}`);
  }

  deleteColeccion(coleccion:Coleccion):Observable<any>{
    return this.http.delete(`${this.BASE_URL}/eliminarColeccion/${coleccion.id_col}`);
  }

  deleteLibro(id:string):Observable<any>{
    return this.http.delete(`${this.BASE_URL}/eliminarMaterial/${id}`);
  }
}
