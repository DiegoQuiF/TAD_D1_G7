export class Coleccion {
    id_col: string;
    nombre_col: string;
    tipo_col: string;
    creacion_col: string;
    actu_col: string;

    constructor(id:string, nom:string, tipo:string, crea:string, actu:string){
            this.id_col = id;
            this.nombre_col = nom;
            this.tipo_col = tipo;
            this.creacion_col = crea;
            this.actu_col = actu;
        }
}
