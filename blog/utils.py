from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    
    def fetch_pdf_resources(uri, rel):
        if uri.find(settings.MEDIA_URL) != -1:
            path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ''))
        elif uri.find(settings.STATIC_URL) != -1:
            path = os.path.join(settings.STATIC_ROOT, uri.replace(settings.STATIC_URL, ''))
        else:
            path = None
        return path
        
    def fetch_resources(uri, rel):
        find_file_in_path_using_uri
        return path


    pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')), result, encoding='utf-8',link_callback=fetch_pdf_resources)

    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def convertHtmlToPdf(sourceHtml, outputFilename):
    result = BytesIO()
    resultFile = open(outputFilename, "w+b") 
    pisaStatus = pisa.CreatePDF(sourceHtml, result,  encoding='UTF-8') 
    if not pisaStatus.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

    


