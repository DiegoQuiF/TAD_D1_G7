export class MaterialCompleto {
    idMat: string;
    tituloMat: string;
    autorMat: string;
    originalMat: string;
    idiomaMat: string;
    electronicoMat: string;
    precioEMat: string;
    fisicoMat: string;
    precioFMat: string;
    idCol: string;
    nombreCol: string;
    tipoCol: string;
    idUsu: string;
    nombreUsu: string;
    aPatUsu: string;
    aMatUsu: string;

    constructor(idMat:string, tituloMat:string, autorMat:string, originalMat:string, idiomaMat:string, electronicoMat:string, precioEMat:string,
        fisicoMat:string, precioFMat:string, idCol:string, nombreCol:string, tipoCol:string, idUsu:string, nombreUsu:string, aPatUsu:string, aMatUsu:string){
            this.idMat = idMat;
            this.tituloMat = tituloMat;
            this.autorMat = autorMat;
            this.originalMat = originalMat;
            this.idiomaMat = idiomaMat;
            this.electronicoMat = electronicoMat;
            this.precioEMat = precioEMat;
            this.fisicoMat = fisicoMat;
            this.precioFMat = precioFMat;
            this.idCol = idCol;
            this.nombreCol = nombreCol;
            this.tipoCol = tipoCol;
            this.idUsu = idUsu;
            this.nombreUsu = nombreUsu;
            this.aPatUsu = aPatUsu;
            this.aMatUsu = aMatUsu;
        }
}
