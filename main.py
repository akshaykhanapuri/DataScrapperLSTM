from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd


def get_data(driver, df, page, pageNo):
    driver.get('https://www.moneycontrol.com/financials/relianceindustries/'+page+'/RI/' + pageNo + '#RI')
    rows = driver.find_elements(By.TAG_NAME, 'tr')

    col1 = []
    col2 = []
    col3 = []
    col4 = []
    col5 = []
    col6 = []

    for row in rows:

        if (row.find_elements(By.XPATH, './td[2]')):
            col1.append(row.find_element(By.XPATH, './td[1]').text)
            col2.append(row.find_element(By.XPATH, './td[2]').text)
            col3.append(row.find_element(By.XPATH, './td[3]').text)
            col4.append(row.find_element(By.XPATH, './td[4]').text)
            col5.append(row.find_element(By.XPATH, './td[5]').text)
            col6.append(row.find_element(By.XPATH, './td[6]').text)

    if pageNo == '1':
        df[col1[0]] = col1[1:]
        df[col2[0]] = col2[1:]
        df[col3[0]] = col3[1:]
        df[col4[0]] = col4[1:]
        df[col5[0]] = col5[1:]
        df[col6[0]] = col6[1:]

    else:
        # We don't have to add the first column to the dataframe again. Hence, starting from col2 for 2nd page onwards
        df[col2[0]] = col2[1:]
        df[col3[0]] = col3[1:]
        df[col4[0]] = col4[1:]
        df[col5[0]] = col5[1:]
        df[col6[0]] = col6[1:]


if __name__ == '__main__':

    # At the moment the variables page and lastPageNo have been hardcoded with the following mapping

    """
    * Balance Sheet data = balance-sheetVI
    * Profit & Loss data = profit-lossVI
    * Quarterly results data =  quarterly-results
    * Cash flow data = cash-flowVI
    * Ratios = ratiosVI
    """
    page = "balance-sheetVI"

    """
    * 5 for all the data except Quarterly results
    * 17 for quarterly results
    """
    lastPageNo = 5

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)

    df = pd.DataFrame()
    for pageNo in range(1,lastPageNo):
        get_data(driver, df, page, str(pageNo))

    df.to_csv(page+".csv")
    driver.quit()
