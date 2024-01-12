import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'

@Injectable({
  providedIn: 'root'
})
export class ConnBackendService {

  private BASE_URL = 'https://paginatad01.onrender.com';
  constructor(private http:HttpClient) { }

  getUsuarios():Observable<any>{
    return this.http.get(`${this.BASE_URL}/`);
  }
}
