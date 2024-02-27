export class Categoria {
    idCTC: string;
    idTC: string;
    nombreTC: string;
    idC: string;
    nombreC:string

    constructor(idCTC:string, idTC:string, nombreTC:string, idC:string, nombreC:string){
        this.idCTC = idCTC;
        this.idTC = idTC;
        this.nombreTC = nombreTC;
        this.idC = idC;
        this.nombreC = nombreC;
    }
}