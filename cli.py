# cli.py
import gettext
import sys
import locale
from datetime import date
from babel.dates import format_date
from babel.numbers import format_number

# 1. Configuração do Gettext (Tradução de Strings)
# 'cli' é o nome do domínio (nome do arquivo de tradução)
# 'locale' é a pasta onde os arquivos ficarão
gettext.bindtextdomain('cli', 'locale')
gettext.textdomain('cli')
_ = gettext.gettext

if __name__ == '__main__':
    # Pegamos o locale do sistema para usar nas funções do Babel
    # Se der erro no Windows, pode forçar locale='pt_BR' para testar
    
    # 2. Data (Formatada pelo Babel)
    today = date.today()
    # format_date usa as configurações regionais do sistema automaticamente
    print(format_date(today, format='long')) 

    # 3. Número (Formatado pelo Babel)
    number = 240000000000.32212
    print(format_number(number))

    # 4. Strings marcadas com _() para tradução
    # Note que usamos _("") dentro do input e do print
    print(_("Input your name: "))
    name = input() 
    
    print(_("Hello {}").format(name))