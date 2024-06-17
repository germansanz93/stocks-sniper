import pandas as pd

from src.services.morningstar_service import call_morningstar_valuation, call_morningstar_stock_id, search_ticker
from src.services.files_service import assert_directory_existence, create_directory, save_in_file, \
    read_valuation_from_file


def search_stock(search_input):
    search_results = search_ticker(search_input)
    return search_results

def get_stock_info(ticker):
    # container = call_morningstar_valuation(ticker)
    # print(container)
    is_data_present = assert_directory_existence(ticker)
    if not is_data_present:
        dir = create_directory(ticker)
        stock_response = call_morningstar_stock_id(ticker)
        save_in_file(f'{dir}/{ticker}-search.json', stock_response)
        stock_id = stock_response['page']['performanceID']
        valuation = call_morningstar_valuation(stock_id)
        save_in_file(f'{dir}/{ticker}-valuation.json', valuation)
    else:
        print('Files for that stock are already present..')


def stock_data():
    # container = call_morningstar_valuation()
    # save_in_file('sbux.json', container)
    container = read_valuation_from_file('../sbux.json')

    df = pd.DataFrame(container)

    # df = df.drop('Collapsed', axis=1)

    df = df.drop('userType')
    df = df.drop('footer')

    save_in_file('../primer-dataframe.json', df.to_dict())
    rows = df['Collapsed']['rows']
    columns = df['Collapsed']['columnDefs']

    price_sales = [rows[0]['label']] + rows[0]['datum']

    content = []

    for i in range(len(rows)):
        content.append([rows[i]['label']] + rows[i]['datum'])
    clean_df = pd.DataFrame(content)
    clean_df.columns = columns
    clean_df = clean_df.set_index(['Calendar'])
    print(clean_df)
