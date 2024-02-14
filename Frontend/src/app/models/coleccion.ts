export class Coleccion {
    id_coleccion: string;
    nombre: string;
    tipo: string;
    creacion: string;
    actualizacion: string;

    constructor(id:string, nom:string, tipo:string, crea:string, actu:string){
            this.id_coleccion = id;
            this.nombre = nom;
            this.tipo = tipo;
            this.creacion = crea;
            this.actualizacion = actu;
        }
}
