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
  selector: 'app-figura5',
  templateUrl: './figura5.component.html',
  styleUrl: './figura5.component.css'
})

export class Figura5Component {

  constructor(private connBackend:ConnBackendService){};

  graficoActual: Highcharts.Options = {};
  matPorFecha: typeof Highcharts = Highcharts;

  info = [[0, 0]];
  categorias = ['0'];

  ngOnInit(): void {
    this.crearGraficoDispersión();
    this.getInfo();
  }

  async getInfo() {
    const data = await this.connBackend.getVentasTotales().toPromise();
    console.log(data);
    if(data.ventasTotales && data.ventasTotales.length > 0) {
      this.categorias = await data.ventasTotales.map((item: { Id: number; Ventas: number }) => item.Id);
      this.info = data.ventasTotales.map((venta: { Id: number; Ventas: number }) => [venta.Id, venta.Ventas]);
    }
    else {
      this.info = [[0, 0]];
      this.categorias = ['0'];
    }
    this.crearGraficoDispersión();
  }

  crearGraficoDispersión() {
    this.graficoActual = {
      chart: {
        type: 'scatter',
        height: 300
      },
      title: {
        text: 'Ventas por usuario'
      },
      xAxis: {
        title: {
          text: 'Id Usuario'
        },
        categories: this.categorias
      },
      yAxis: {
        title: {
          text: 'Total de ventas'
        }
      },
      series: [{
        type: 'scatter',
        name: 'Datos',
        data: this.info
      }]
    };
  }
}
