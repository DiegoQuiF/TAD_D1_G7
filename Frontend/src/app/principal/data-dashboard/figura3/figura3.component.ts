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
  selector: 'app-figura3',
  templateUrl: './figura3.component.html',
  styleUrl: './figura3.component.css'
})
export class Figura3Component {

  constructor(private connBackend:ConnBackendService){};

  graficoActual: Highcharts.Options = {};
  matPorFecha: typeof Highcharts = Highcharts;

  info = [{name:'Anonimo (123)', y:10}];

  ngOnInit(): void {
    this.crearGraficoCircular();
    this.getInfo();
  }

  async getInfo() {
    const data = await this.connBackend.getMaterialesPorUsuario().toPromise();
    console.log(data);
    if(data.materialesPorUsuario && data.materialesPorUsuario.length > 0) {
      this.info = data.materialesPorUsuario;
    }
    else {
      this.info = [{name:'Anonimo (123)', y:10}];
    }
    this.crearGraficoCircular();
  }

  crearGraficoCircular() {
    this.graficoActual = {
      chart: {
        type: 'pie',
        height: 320,
        width: 600
      },
      title: {
        text: 'Cantidad de material bibliográfico por usuario'
      },
      plotOptions: {
        pie: {
          allowPointSelect: true,
          cursor: 'pointer',
          dataLabels: {
            enabled: true,
            format: '<b>{point.name}</b>: {point.percentage:.1f} %'
          }
        }
      },
      series: [{
        type: 'pie',
        name: 'Datos',
        data: this.info
      }]
    };
  }
}
