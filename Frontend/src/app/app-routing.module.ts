import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DataDashboardComponent } from './principal/data-dashboard/data-dashboard.component';
import { PrincipalComponent } from './principal/principal.component';

const routes: Routes = [
  { path: '', component: PrincipalComponent },
  { path: 'datos', component: DataDashboardComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }