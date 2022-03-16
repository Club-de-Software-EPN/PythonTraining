import PyPDF2

archivoPdf = PyPDF2.PdfFileReader((open('Scripting/PDF/unionEjemplo.pdf', 'rb')))
marcaAgua = PyPDF2.PdfFileReader((open('Scripting/PDF/marcaAgua.pdf', 'rb')))
paginaMarcaAgua = marcaAgua.getPage(0)
salida = PyPDF2.PdfFileWriter()

for numeroPagina in range(archivoPdf.getNumPages()):
    page = archivoPdf.getPage(numeroPagina)
    page.mergePage(paginaMarcaAgua)
    salida.addPage(page)
with open('Scripting/PDF/resultadoFinal.pdf','wb') as archivoFinal:
    salida.write(archivoFinal)



