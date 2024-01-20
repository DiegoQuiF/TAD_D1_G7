import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

import { PrincipalComponent } from './principal/principal.component';
import { LoggedComponent } from './principal/logged/logged.component';
import { LoginRegisterComponent } from './principal/login-register/login-register.component';
import { LogueadoComponent } from './principal/logueado/logueado.component';

@NgModule({
    declarations: [		
      AppComponent,
      PrincipalComponent,
      LoggedComponent,
      LoginRegisterComponent,
      LogueadoComponent
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