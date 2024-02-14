import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

import { PrincipalComponent } from './principal/principal.component';
import { LoginRegisterComponent } from './principal/login-register/login-register.component';
import { LogueadoComponent } from './principal/logueado/logueado.component';
import { PerfilComponent } from './principal/logueado/perfil/perfil.component';
import { ComunidadComponent } from './principal/logueado/comunidad/comunidad.component';
import { ColeccionesComponent } from './principal/logueado/colecciones/colecciones.component';
import { TiendaComponent } from './principal/logueado/tienda/tienda.component';
import { MensajesComponent } from './principal/logueado/mensajes/mensajes.component';
import { CrearColeccionComponent } from './principal/logueado/colecciones/crear-coleccion/crear-coleccion.component';
import { EditarEliminarColeccionComponent } from './principal/logueado/colecciones/editar-eliminar-coleccion/editar-eliminar-coleccion.component';


@NgModule({
    declarations: [		
      AppComponent,
      PrincipalComponent,
      LoginRegisterComponent,
      LogueadoComponent,
      PerfilComponent,
      ComunidadComponent,
      ColeccionesComponent,
      TiendaComponent,
      MensajesComponent,
      CrearColeccionComponent,
      EditarEliminarColeccionComponent
    ],
    imports: [
      BrowserModule,
      AppRoutingModule,
      HttpClientModule,
      FormsModule
    ],
    providers: [],
    bootstrap: [AppComponent]
  })
  export class AppModule { }