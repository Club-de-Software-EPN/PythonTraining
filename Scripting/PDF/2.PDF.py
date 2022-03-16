# Unir pdfs
import PyPDF2

def unir_pdfs(listaPdfs: list, nombrePdf: str):
    merger = PyPDF2.PdfFileMerger()
    for pdf in listaPdfs:
        merger.append(pdf)
    merger.write('Scripting/PDF/'+nombrePdf+'.pdf')


lista = ['Scripting/PDF/pdfsBases/pdfUnido.pdf', 'Scripting/PDF/pdfsBases/pdfBlanco.pdf']
unir_pdfs(lista, 'unionEjemplo')