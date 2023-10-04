from pdf2docx import Converter
pdf_file = 'D:\Kuliah D4_POLINES\TRK\Semester 1\MatKul\Sistem_Operasi\Penugasan\JOBSHEET-002 (PERTEMUAN 4)\Job_2_Manajemen Windows.pdf'
docx_file = 'D:\Kuliah D4_POLINES\TRK\Semester 1\MatKul\Sistem_Operasi\Penugasan\JOBSHEET-002 (PERTEMUAN 4)\Job_2_Manajemen Windows.docx'
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()
