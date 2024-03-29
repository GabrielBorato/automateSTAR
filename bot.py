from botcity.core import DesktopBot
from botcity.web import WebBot, Browser, By
from botcity.web.browsers.chrome import Chrome
from datetime import datetime, timedelta
from webdriver_manager.chrome import ChromeDriverManager
WebBot.browser = Browser.CHROME
driver_path = ChromeDriverManager().install()
WebBot.driver_path = driver_path
desktop_bot = DesktopBot()
webbot = WebBot()
data_atual = datetime.now()
webbot.browse("https://urano.hinova.com.br/sga/sgav4_starassociacao/v5/login.php")
webbot.maximize_window()
webbot.click_at(x= 872, y= 520)
webbot.tab()
webbot.tab()
webbot.enter()
webbot.find_element('usuario', By.ID).send_keys('Matheus')
webbot.find_element('senha', By.ID).send_keys('Math100#')
webbot.tab()
webbot.enter()
webbot.wait(5000)
webbot.click_at(x= 872, y= 520)
webbot.tab()
webbot.enter()
webbot.browse("https://urano.hinova.com.br/sga/sgav4_starassociacao/relatorio/relatorioBoleto.php")
webbot.wait(5000)
mes_atual = data_atual.month
ano_atual = data_atual.year
mes_atual_str = f"{mes_atual:02d}"
data_atual = datetime.now()
data_inicial = f"01/{mes_atual:02d}/{ano_atual}"
data_vencimento1 = f"10/{mes_atual_str}/{ano_atual}"
data_vencimento2 = data_atual - timedelta(days=1)
data_vencimento2_formatada = data_vencimento2.strftime("%d/%m/%Y")
webbot.find_element('DataVencimento', By.ID).send_keys(data_inicial)
if data_atual.day < 10:
    webbot.find_element('DataVencimentoFinal', By.ID).send_keys(data_vencimento1)
else:
    webbot.find_element('DataVencimentoFinal', By.ID).send_keys(data_vencimento2_formatada)
webbot.find_element('chkTSituacaoBoleto', By.ID).click()
webbot.find_element('chkBoleto2', By.ID).click()
webbot.find_element('chkTTipoBoletoAll', By.ID).click()
webbot.find_element('chkTipoBoletoAll5', By.ID).click()
webbot.find_element('cmbLayoutRelatorio', By.ID).click()
webbot.type_down()
webbot.type_down()
webbot.type_down()
webbot.enter()
webbot.find_element('cmbOrdenacao1', By.ID).click()
webbot.type_down()
webbot.enter()
webbot.tab()
webbot.tab()
webbot.tab()
webbot.tab()
webbot.type_down()
webbot.enter()
webbot.wait(1000000)
