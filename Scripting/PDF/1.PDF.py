import PyPDF2 as pdf

archivo = 'Scripting/PDF/pdfsBases/pdfUnido.pdf'

with open(archivo, 'rb') as miArchivo:
    print(miArchivo)
    print(type(miArchivo))
    # pasar esta información binaria
    # a un formato operable para pdf
    archivoPdf = pdf.PdfFileReader(miArchivo)
    print(archivoPdf)
    print(type(archivoPdf))

    # Información archivo pdf
    print(f'Info del archivo {archivo} es: {archivoPdf.getDocumentInfo()}')
    print(f'Destinatiros del archivo {archivo} es: {archivoPdf.getNamedDestinations()}')
    # Número de páginas
    print(f'Número páginas del archivo {archivo} es: {archivoPdf.getNumPages()}')

    # Obtener una página en específico
    pagina = archivoPdf.getPage(0)

    print(pagina)
    print(type(pagina))

    # Rotar una página
    # Sentido antihorario    
    pagina.rotateCounterClockwise(90)

    ### Escribir pdf

    writerPdf = pdf.PdfFileWriter()
    writerPdf.addPage(pagina)
    writerPdf.addBlankPage()

    with open('Scripting/PDF/pdfBlanco.pdf','wb') as pdfSalida:
        writerPdf.write(pdfSalida)





