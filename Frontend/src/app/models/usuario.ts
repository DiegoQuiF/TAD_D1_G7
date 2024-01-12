export class Usuario {
    id_user: string;
    nom_user: string;
    a_pat_user: string;
    a_mat_user: string;
    correo_user: string;
    contra_user: string;
    cel_user: string;

    constructor(id:string, nom:string, a_pat:string, a_mat:string, correo:string,
        contra:string, cel:string){
            this.id_user = id;
            this.nom_user = nom;
            this.a_pat_user = a_pat;
            this.a_mat_user = a_mat;
            this.correo_user = correo;
            this.contra_user = contra;
            this.cel_user = cel;
        }
}