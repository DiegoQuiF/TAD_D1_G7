export class Transaccion {
    nro_publicaciones: string;
    nro_compras: string;
    recaudado: string;

    constructor(pub:string, com:string, rec:string){
        this.nro_publicaciones = pub;
        this.nro_compras = com;
        this.recaudado = rec;
    }
}