export class Material {
    idMaterial: string;
    titulo: string;
    autor: string;
    fecha: string;
    idioma: string;
    procedencia: string;
    dispFisico: string;
    precioFisico: string;
    stockFisico: string;
    dispElec: string;
    precioElec: string;

    constructor(id:string, tit:string, aut:string, pub:string, idi:string, pro:string, fis:string, prf:string, sto:string, elec:string, pre:string){
            this.idMaterial = id;
            this.titulo = tit;
            this.autor = aut;
            this.fecha = pub;
            this.idioma = idi;
            this.procedencia = pro;
            this.dispFisico = fis;
            this.precioFisico = prf;
            this.stockFisico = sto;
            this.dispElec = elec;
            this.precioElec = pre;
        }
}




