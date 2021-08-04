from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt, RGBColor, Inches
from docx.oxml.ns import qn
from docx.oxml.xmlchemy import OxmlElement
from docx.oxml.shared import qn

# Nuevo documento
document = Document()

'''Scip obtenido de StackOverflow-->'''
sec_pr = document.sections[0]._sectPr # obtener las propiedades de la seccion
# crear los bordes
pg_borders = OxmlElement('w:pgBorders')
# especifica cómo se debe calcular la posición relativa de los bordes
pg_borders.set(qn('w:offsetFrom'), 'page')
for border_name in ('top', 'left', 'bottom', 'right',): # escogemos los bordes
    border_el = OxmlElement(f'w:{border_name}')
    border_el.set(qn('w:val'), 'single') # una sola línea
    border_el.set(qn('w:sz'), '4') # para conocer el significado de los atributos restantes, consulte los documentos
    border_el.set(qn('w:space'), '24')
    border_el.set(qn('w:color'), 'auto')
    pg_borders.append(border_el) # registre un borde único a el borde 
sec_pr.append(pg_borders) # aplicar cambios de borde a la sección
''' <--Scip obtenido de StackOverflow'''

# Establecer el estilo del documento "Normal"
document.styles['Normal'].font.size = Pt(12)
document.styles['Normal'].font.color.rgb = RGBColor(0x00, 0x00, 0x00)
document.styles['Normal'].font.name = u'Arial'
document.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'Arial')
# Establezca el estilo del documento "Título"
document.styles['Heading 2'].font.size = Pt(20)
document.styles['Heading 2'].font.color.rgb = RGBColor(0x00, 0x00, 0x00)
document.styles['Heading 2'].font.name = u'Arial'
document.styles['Heading 2']._element.rPr.rFonts.set(qn('w:eastAsia'), u'Arial')
document.styles['Heading 2'].font.bold = False

institucion = 'Instituto Politecnico Nacional \n'
escuela = 'UPIICSA\n'
materia= 'un texto sustituto\n'
investigacion= 'un texto sustituto\n'
profesor = 'un texto sustituto\n'
alumno = 'Gudiño Alanis Cesar\n'
grupo = 'un texto sustituto\n'
boleta = '2021601757\n'

argumentos = [institucion , escuela, materia, investigacion, profesor, alumno, grupo, boleta]

for i in argumentos:
    p = document.add_paragraph(i , style='Heading 2')
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    '''p.paragraph_format.space_after'''
document.add_page_break()
document.save(r'C:\Users\cesar\Documents\GitHub\-100DaysOfCode-\ portada.docx')