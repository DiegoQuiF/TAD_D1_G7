export class Comprador {
    catalogo: string;
    comprador: string;
    fechaCompra: string;
    fechaEntrega: string;
    subtotal: string;
    titulo: string;

    constructor(cat:string, com:string, fec:string, fee:string, sub:string, tit:string){
        this.catalogo = cat;
        this.comprador = com;
        this.fechaCompra = fec;
        this.fechaEntrega = fee;
        this.subtotal = sub;
        this.titulo = tit;
    }
}