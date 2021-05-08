import arrow
import pandas

from typing import Union
from generated.proto.config_pb2 import Stock, OtherCurrencies

def patch_missing_data(df: pandas.DataFrame, entity: Union[Stock, OtherCurrencies]):
    today = arrow.now().floor("day")
    current_date = arrow.get(entity.first_transaction)
    while True:
        if current_date >= today:
            return df

        date_string = current_date.format("YYYY-MM-DD")
        if date_string not in df.index:
            previous_date_string = current_date.shift(days=-1).format("YYYY-MM-DD")
            # Known issue: SGX day is ahead of IBKR date.
            single_row_df = df.loc[previous_date_string]
            single_row_df = single_row_df.rename(
                index={
                    pandas.Timestamp(
                        previous_date_string, tz=None
                    ): pandas.Timestamp(date_string, tz=None)
                }
            )
            df = df.append(single_row_df)

        current_date = current_date.shift(days=1)
