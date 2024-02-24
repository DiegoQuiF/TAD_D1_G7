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
import { DataDashboardComponent } from './principal/data-dashboard/data-dashboard.component';
import { HighchartsChartModule } from 'highcharts-angular';
import { Figura1Component } from './principal/data-dashboard/figura1/figura1.component';
import { Figura2Component } from './principal/data-dashboard/figura2/figura2.component';
import { Figura3Component } from './principal/data-dashboard/figura3/figura3.component';
import { Figura4Component } from './principal/data-dashboard/figura4/figura4.component';
import { Figura5Component } from './principal/data-dashboard/figura5/figura5.component';

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
      DataDashboardComponent,
      Figura1Component,
      Figura2Component,
      Figura3Component,
      Figura4Component,
      Figura5Component
    ],
    imports: [
      BrowserModule,
      AppRoutingModule,
      HttpClientModule,
      FormsModule,
      HighchartsChartModule
    ],
    providers: [],
    bootstrap: [AppComponent]
  })
  export class AppModule { }