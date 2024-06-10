import pandas as pd

from files_service import read_valuation_from_file, save_in_file

def get_stock_info():

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
