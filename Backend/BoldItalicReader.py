import docx
from docx.shared import Pt

#Reads a document in docx format
document = docx.Document('base.docx')

#opens a file in html format
f = open('base.txt', 'a')
bolds=[]
italics=[]
f.write('<!DOCTYPE html>\n')
f.write('<html>\n')
f.write('<head>\n')
f.write('\t<title>'+'Title Goes Here'+'</title>\n')
f.write('</head>\n')
f.write('<body>\n')
#Reads a document para wise checks each word for bold adds <b></b> and for itlaic adds <i></i>
for para in document.paragraphs:
    f.write(' <p> ')
    for run in para.runs:
        if run.italic :
            run.text = '<i> '+run.text+' </i> '
        if run.bold :
            run.text = '<b> '+run.text+' </b> '
        if run.font.size > Pt(40):
            run.text = ' <h1> '+run.text+' </h1> '
        f.write(run.text)
    f.write(' </p> ')

f.write('\n</body>')
f.write('\n</html>')     
        
f.close()
boltalic_Dict={'bold_phrases':bolds,
            'italic_phrases':italics}