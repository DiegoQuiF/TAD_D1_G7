export class Material {
    idMat: string;
    titulo: string;
    autor: string;
    publicacion: string;
    idioma: string;
    procedencia: string;
    original: string;
    electronico: string;
    precioE: string;
    fisico: string;
    precioF: string;
    stockF: string;

    constructor(id:string, tit:string, aut:string, pub:string, idi:string, pro:string, ori:string, elec:string, pre:string, fis:string, prf:string, sto:string){
            this.idMat = id;
            this.titulo = tit;
            this.autor = aut;
            this.publicacion = pub;
            this.idioma = idi;
            this.procedencia = pro;
            this.original = ori;
            this.electronico = elec;
            this.precioE = pre;
            this.fisico = fis;
            this.precioF = prf;
            this.stockF = sto;
        }
}




