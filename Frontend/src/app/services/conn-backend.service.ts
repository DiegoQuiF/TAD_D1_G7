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

  private BASE_URL = 'https://paginatad01.onrender.com';
  //private BASE_URL = 'http://127.0.0.1:5000'

  constructor(private http:HttpClient) { }


  // Login-Register

  getUsuario(correo:string, contra:string):Observable<any>{     // Iniciar sesión
    const data = {
      correo: correo,
      contra: contra
    }
    return this.http.post(`${this.BASE_URL}/getUsuario`, data);
  }

  postUsuario(nombre_u:string, aPat:string, aMat:string, correo_u:string, contra_u:string, celular_u:string, direccion:string): Observable<any>{    // Registrarse
    const data = {
      nombre: nombre_u,
      paterno: aPat,
      materno: aMat,
      correo: correo_u,
      contra: contra_u,
      celular: celular_u,
      direccion: direccion
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
      direccion: usuario.direc_user,
      id: usuario.id_user
    }
    return this.http.put(`${this.BASE_URL}/guardarUsuario`, data);
  }

  getTarjetas(id: string):Observable<any>{
    const data = {
      id_user: id
    }
    return this.http.post(`${this.BASE_URL}/getTarjetas`, data);
  }

  delTarjeta(id:string):Observable<any> {
    return this.http.delete(`${this.BASE_URL}/eliminarTarjeta/${id}`);
  }

  recargarTarjeta(id:string, monto:number):Observable<any> {
    const data = {
      id_tarjeta: id,
      monto_tarjeta: monto
    }
    return this.http.post(`${this.BASE_URL}/recargarTarjeta`, data);
  }

  addTarjeta(id:string, numero:string, caducidad:string, cvv:string, saldo:number):Observable<any> {
    const data = {
      id_user: id,
      numero_tar: numero,
      caducidad_tar: caducidad,
      cvv_tar: cvv,
      saldo_tar: saldo
    }
    return this.http.post(`${this.BASE_URL}/registrarTarjeta`, data);
  }

  cambiarPredeterminado(id_usuario:string, id_tarjeta:string):Observable<any> {
    const data = {
      id_user: id_usuario,
      id_tarjeta: id_tarjeta
    }
    return this.http.post(`${this.BASE_URL}/cambiarPredeterminado`, data);
  }

  getColeccion(id:string):Observable<any>{
    const data = {
      id_user: id
    }
    return this.http.post(`${this.BASE_URL}/getColeccion`, data);
  }

  postColeccion(id_user:string, nombre_col:string, tipo_col:string): Observable<any>{
    const hoy = new Date();
    const dia = hoy.getDate().toString().padStart(2, '0');
    const mes = (hoy.getMonth() + 1).toString().padStart(2, '0');
    const anio = hoy.getFullYear().toString();
    const data = {
      id_user: id_user,
      nombre: nombre_col,
      tipo: tipo_col,
      creacion: `${dia}/${mes}/${anio}`,
      actualizacion: `${dia}/${mes}/${anio}`
    }
    return this.http.post(`${this.BASE_URL}/registrarColeccion`, data)
  }

  putColeccion(coleccion: Coleccion): Observable<any> {
    const hoy = new Date();
    const dia = hoy.getDate().toString().padStart(2, '0');
    const mes = (hoy.getMonth() + 1).toString().padStart(2, '0');
    const anio = hoy.getFullYear().toString();
    const data = {
      id_coleccion: coleccion.id_coleccion,
      nombre: coleccion.nombre,
      tipo: coleccion.tipo,
      actualizacion: `${dia}/${mes}/${anio}`
    }
    return this.http.put(`${this.BASE_URL}/guardarColeccion`, data);
  }

  postCarrito(idMat:string, idUser:string): Observable<any> {
    const data = {
      id_material: idMat,
      id_user: idUser
    }
    return this.http.post(`${this.BASE_URL}/registrarCarrito`, data)
  }

  getCarrito(idUser:string): Observable<any> {
    return this.http.get(`${this.BASE_URL}/getCarritoCompleto/${idUser}`)
  }

  postMaterial(material:Material, id:string): Observable<any>{
    const hoy = new Date();
    const dia = hoy.getDate().toString().padStart(2, '0');
    const mes = (hoy.getMonth() + 1).toString().padStart(2, '0');
    const anio = hoy.getFullYear().toString();

    const data = {
      idColeccion: id,
      titulo: material.titulo,
      autor: material.autor,
      fecha: `${dia}/${mes}/${anio}`,
      idioma: material.idioma,
      procedencia: material.procedencia,
      dispFisico: material.dispFisico,
      precioFisico: material.precioFisico,
      stockFisico: material.stockFisico,
      dispElec: material.dispElec,
      precioElec: material.precioElec,
    }

    return this.http.post(`${this.BASE_URL}/registrarLibro`, data)
  }

  getMaterialesCompletos(id:string):Observable<any>{
    return this.http.get(`${this.BASE_URL}/getMaterialesCompletos/${id}`);
  }

  postFactura(idMaterial:string, idUsuario:string): Observable<any>{
    const hoy = new Date();
    const dia = hoy.getDate().toString().padStart(2, '0');
    const mes = (hoy.getMonth() + 1).toString().padStart(2, '0');
    const mes1 = (hoy.getMonth() + 2).toString().padStart(2, '0');
    const anio = hoy.getFullYear().toString();
    const data = {
      fechaC: `${dia}/${mes}/${anio}`,
      fechaE: `${dia}/${mes1}/${anio}`,
      id_material: idMaterial,
      id_usuario: idUsuario
    }
    return this.http.post(`${this.BASE_URL}/registrarFactura`, data)
  }

  getUsuarios():Observable<any>{
    return this.http.get(`${this.BASE_URL}/getUsuarios`);
  }

  getLibros(id:string):Observable<any>{
    const data = {
      id_coleccion: id
    }
    return this.http.post(`${this.BASE_URL}/getMaterial`, data);
  }
  

  deleteUsuario(id:string):Observable<any>{
    return this.http.delete(`${this.BASE_URL}/eliminarUsuario/${id}`);
  }

  deleteColeccion(coleccion:Coleccion):Observable<any>{
    return this.http.delete(`${this.BASE_URL}/eliminarColeccion/${coleccion.id_coleccion}`);
  }

  deleteLibro(id:string):Observable<any>{
    return this.http.delete(`${this.BASE_URL}/eliminarMaterial/${id}`);
  }
}
