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
  selector: 'app-figura2',
  templateUrl: './figura2.component.html',
  styleUrl: './figura2.component.css'
})
export class Figura2Component implements OnInit {

  constructor(private connBackend:ConnBackendService){};

  graficoActual: Highcharts.Options = {};
  matPorFecha: typeof Highcharts = Highcharts;

  info = [{Anio:'2000', Total:0}];
  anios: string[] = ['2000'];
  totales: number[] = [0];

  ngOnInit(): void {
    this.crearGrafico();
    this.getInfo();
  }

  async getInfo() {
    const data = await this.connBackend.getMaterialesPorAnio().toPromise();
    console.log(data);
    if(data.materialesPorAnio && data.materialesPorAnio.length > 0) {
      this.info = data.materialesPorAnio;
    }
    else {
      this.info = [{Anio:'2000', Total:0}];
    }
    this.anios = await this.info.map(item => item.Anio);
    this.totales = await this.info.map(item => item.Total);
    this.crearGrafico();
  }

  async crearGrafico() {
    this.graficoActual = {
      chart: {
        type: 'line',
        height: 320,
        width: 600
      },
      title: {
        text: 'Año de publicación de los materiales'
      },
      xAxis: {
        categories: this.anios
      },
      yAxis: {
        title: {
          text: 'Cantidad'
        }
      },
      series: [{
        type: 'line',
        name: 'Materiales',
        data: this.totales
      }]
    };
  }
}
