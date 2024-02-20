import { Component } from '@angular/core';
import { ConnBackendService } from '../../services/conn-backend.service';
import Highcharts from 'highcharts';

@Component({
  selector: 'data-dashboard',
  standalone: false,
  templateUrl: './data-dashboard.component.html',
  styleUrl: './data-dashboard.component.css'
})
export class DataDashboardComponent {

  //Los titulos de lso graficos de la izquierda
  menuItems = [
    { label: 'Materiales subidos \n por año de publicación', method: 'crearGraficoMatSubidosPorAnioPublic' },
    { label: 'Facturas por fecha', method: 'crearGraficoFacturasPorFecha' },
    { label: 'Materiales subidos por usuario', method: 'crearGraficoMaterialesPorUsuario' },
  ];

  listaMetodos: { [key: string]: Function } = {
    crearGraficoMatSubidosPorAnioPublic: this.crearGraficoMatSubidosPorAnioPublic.bind(this),
    crearGraficoFacturasPorFecha: this.crearGraficoFacturasPorFecha.bind(this),
    crearGraficoMaterialesPorUsuario: this.crearGraficoMaterialesPorUsuario.bind(this),
  };

  indiceTemporal: number = 0;

  matPorFecha: typeof Highcharts = Highcharts;
  graficoActual: Highcharts.Options = {
    series: [{
      data: [],
      type: 'line'
    }]
  };


  ngOnInit() {
    this.crearGraficoMatSubidosPorAnioPublic();
  }

  constructor(private connBackend: ConnBackendService) {
  }


  //Crea un grafico que muestra la cantidad de materiales bibliograficos que hay en la app publicados en el mismo año
  async crearGraficoMatSubidosPorAnioPublic() {
    try {
      const data = await this.connBackend.getMaterialesPorAnio().toPromise();
      //Se debe colocar el nombre de la información json en JSON.parse(data.(<nombre>))
      const datosParseados = JSON.parse(data.materialesPorAnio);

      //Transformamos los datos a una estructura adecueda para el grafico

      // Eje Y
      const datosGrafico = datosParseados.map((item: { anio: number; cantidad_materiales: number }) => ({
        name: item.anio.toString(),
        y: item.cantidad_materiales
      }));

      // Eje X 
      const years = datosParseados.map((item: { anio: number }) => item.anio.toString());

      //Creación del grafico y colocación de los datos 
      const graficoMatSubPorFecha: Highcharts.Options = {
        title: {
          text: "Cantidad de materiales publicados por año"
        },
        xAxis: {
          categories: years, // Configurar las categorías del eje X con los años
          title: {
            text: 'Año' // Título al eje X
          }
        },
        yAxis: {
          title: {
            text: 'Cantidad' // Título del eje Y
          }
        },
        series: [{
          data: datosGrafico,
          type: 'line'
        }]
      };

      //Se actualiza el grafico actual por el creado 
      this.graficoActual = graficoMatSubPorFecha;

      
      console.log(datosGrafico);
    } catch (error) {
      console.error(error);
    }
  }

  //Crea un grafico que muestra la cantidad de facturas con las mismas fechas(DD/MM/YYYY) de creación 
  async crearGraficoFacturasPorFecha() {
    try {
      const data = await this.connBackend.getFacturasPorFecha().toPromise();
      //Se debe colocar el nombre de la información json en JSON.parse(data.(<nombre>))
      const datosParseados = JSON.parse(data.facturasPorFecha);

      //Transformamos los datos a una estructura adecueda para el grafico

      // Eje Y
      const datosGrafico = datosParseados.map((item: { fechacompra: string; cantidad_facturas: number }) => ({
        name: item.fechacompra.toString(),
        y: item.cantidad_facturas
      }));

      // Eje X 
      const years = datosParseados.map((item: { fechacompra: string }) => item.fechacompra.toString());

      //Creación del grafico y colocación de los datos 
      const graficoFacturaPorFecha: Highcharts.Options = {
        title: {
          text: "Cantidad de facturas creadas por fecha"
        },
        xAxis: {
          categories: years, // Configurar las categorías del eje X con los años
          title: {
            text: 'Fecha de creación' // Título al eje X
          }
        },
        yAxis: {
          title: {
            text: 'Cantidad' // Título del eje Y
          }
        },
        series: [{
          data: datosGrafico,
          type: 'line'
        }]
      };

      //Se actualiza el grafico actual por el creado 
      this.graficoActual = graficoFacturaPorFecha;

      console.log(datosGrafico);
    } catch (error) {
      console.error(error);
    }
  }

  //Crea un grafico que muestra la cantidad materiales bibliograficos subidos por usuarios
  async crearGraficoMaterialesPorUsuario() {
    try {
      const data = await this.connBackend.getMaterialesPorUsuario().toPromise();
      //Se debe colocar el nombre de la información json en JSON.parse(data.(<nombre>))
      const datosParseados = JSON.parse(data.materialesPorUsuario);

      //Transformamos los datos a una estructura adecueda para el grafico

      // Eje Y
      const datosGrafico = datosParseados.map((item: { idusuario: number; cantidad_materiales: number }) => ({
        name: item.idusuario.toString(),
        y: item.cantidad_materiales
      }));

      // Eje X 
      const years = datosParseados.map((item: { idusuario: number }) => item.idusuario.toString());

      //Creación del grafico y colocación de los datos 
      const graficoFacturaPorFecha: Highcharts.Options = {
        title: {
          text: "Cantidad de materiales bibliograficos subidos por usuarios"
        },
        xAxis: {
          categories: years, // Configurar las categorías del eje X con los años
          title: {
            text: 'Id de los usuarios' // Título al eje X
          }
        },
        yAxis: {
          title: {
            text: 'Cantidad' // Título del eje Y
          }
        },
        series: [{
          data: datosGrafico,
          type: 'line'
        }]
      };

      //Se actualiza el grafico actual por el creado 
      this.graficoActual = graficoFacturaPorFecha;

      console.log(datosGrafico);
    } catch (error) {
      console.error(error);
    }
  }

  cambiarGrafico(index: number, event: Event) {

    event.preventDefault(); // Evita el comportamiento predeterminado del enlace 

    //Forma antigua y no dinamica para llamar a los metodos y cambiar de grafico    
    /*
    switch (index) {
      case 0:
        this.crearGraficoMaterialesPorUsuario();
        break;
      case 1:
        this.crearGraficoFacturasPorFecha();
        break;
      case 2:
        this.crearGraficoMaterialesPorUsuario();
        break;
      default:
        break;
    }
    */

    // Obtener el nombre del método asociado al ítem seleccionado
    const methodName: string = this.menuItems[index].method;
    console.log(methodName)
    // Llamar dinámicamente al método correspondiente
    this.ejecutarMetodo(methodName);

    this.indiceTemporal = index;
  }

  ejecutarMetodo(name: string) {
    if (this.listaMetodos[name]) {
      return this.listaMetodos[name]();
    }

    throw new Error(`Method '${name}' is not implemented.`);
  }
}