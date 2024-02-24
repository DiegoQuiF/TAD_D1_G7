import { Component, OnInit } from '@angular/core';
import * as Highcharts from 'highcharts';
import HighchartsMore from 'highcharts/highcharts-more';
import HighchartsExporting from 'highcharts/modules/exporting';
import HighchartsExportData from 'highcharts/modules/export-data';
import { Chart } from 'angular-highcharts';
import { ConnBackendService } from '../../../services/conn-backend.service';

HighchartsMore(Highcharts);
HighchartsExporting(Highcharts);
HighchartsExportData(Highcharts);

@Component({
  selector: 'app-figura4',
  templateUrl: './figura4.component.html',
  styleUrl: './figura4.component.css'
})
export class Figura4Component {

  constructor(private connBackend:ConnBackendService){};

  graficoActual: Highcharts.Options = {};
  matPorFecha: typeof Highcharts = Highcharts;

  info = [{Fecha:'2000', Cantidad:0}];
  fechas: string[] = ['2000'];
  cantidades: number[] = [0];

  ngOnInit(): void {
    this.crearGraficoBarrasHorizontales();
    this.getInfo();
  }

  async getInfo() {
    const data = await this.connBackend.getFacturasPorFecha().toPromise();
    console.log(data);
    if(data.facturasPorFecha && data.facturasPorFecha.length > 0) {
      this.info = data.facturasPorFecha;
    }
    else {
      this.info = [{Fecha:'2000', Cantidad:0}];
    }
    this.fechas = await this.info.map(item => item.Fecha);
    this.cantidades = await this.info.map(item => item.Cantidad);
    this.crearGraficoBarrasHorizontales();
  }

  crearGraficoBarrasHorizontales() {
    this.graficoActual = {
      chart: {
        type: 'bar',
        height: 320,
        width: 600
      },
      title: {
        text: 'Cantidad de facturas por fecha'
      },
      xAxis: {
        categories: this.fechas
      },
      yAxis: {
        title: {
          text: 'Fecha'
        }
      },
      series: [{
        type: 'bar',
        name: 'Datos',
        data: this.cantidades
      }]
    };
  }
}
