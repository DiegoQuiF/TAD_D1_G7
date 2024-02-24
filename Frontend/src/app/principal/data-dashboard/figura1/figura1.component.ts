import { Component, OnInit } from '@angular/core';
import { ConnBackendService } from '../../../services/conn-backend.service';

@Component({
  selector: 'app-figura1',
  templateUrl: './figura1.component.html',
  styleUrl: './figura1.component.css'
})
export class Figura1Component {

  constructor(private connBackend:ConnBackendService){};

  info = [{usuarios:'0', materiales:'0', ventas:'0', metrica:'0'}];

  ngOnInit(): void {
    this.getInfo();
  }

  async getInfo() {
    const data = await this.connBackend.getMetricas().toPromise();
    console.log(data);
    if(data.metricas && data.metricas.length > 0) {
      this.info = data.metricas;
    }
    else {
      this.info = [{usuarios:'0', materiales:'0', ventas:'0', metrica:'0'}];
    }
  }
}
