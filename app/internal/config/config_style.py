from openpyxl.styles import Font, Border, Side, PatternFill

TITLE_STYLE = Font(bold=True)
THIN_STYLE = Side(style="thin")
BORDDER_THIN= Border(left=THIN_STYLE, right=THIN_STYLE, top=THIN_STYLE, bottom=THIN_STYLE)
HEADER_FILL = PatternFill(start_color='366092', end_color='366092', fill_type='solid')
HEADERS = ['CompteNum', 'CompteLib', 'EcritureDate','EcritureLib','Solde', 'Nombre de Debit', 'Commentaire CAC']

HEADER_FONT = Font(name='Calibri', size=11, bold=True, color='FFFFFF')
HEADER_FONT_RED = Font(name='Calibri', size=11, bold=True, color='D53E0F')
