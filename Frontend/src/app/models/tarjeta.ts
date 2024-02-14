export class Tarjeta {
    id: string;
    numero: string;
    caducidad: string;
    cvv: string;
    saldo: string;
    predeterminada: string;

    constructor(id:string, num:string, cad:string, cvv:string, sal:string, pre:string){
            this.id = id;
            this.numero = num;
            this.caducidad = cad;
            this.cvv = cvv;
            this.saldo = sal;
            this.predeterminada = pre;
        }
}