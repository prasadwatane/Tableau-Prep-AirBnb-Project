
import pandas as pd

def add_tv_internet_columns(df):
    def parse_amenities(x):
        if isinstance(x, str):
            try:
                # Remove braces, split by comma
                return [item.strip().strip('"') for item in x.strip('{}').split(',')]
            except Exception:
                return []
        return []

    def has_tv(amenities):
        return int('TV' in amenities)

    def has_internet(amenities):
        return int('Wireless Internet' in amenities or 'Internet' in amenities)

    def has_airconditioner(amenities):
        return int('Air conditioning' in amenities)


    parsed = df['amenities'].apply(parse_amenities)
    df['TV'] = parsed.apply(has_tv)
    df['Internet'] = parsed.apply(has_internet)
    df['Air Conditioner'] = parsed.apply(has_airconditioner)

    return df.drop(columns=['amenities'])


def get_output_schema():
  return pd.DataFrame({
    'id' : prep_int(),
    'TV' : prep_int(),
    'Internet' : prep_int(),
    'Air Conditioner' : prep_int(),
    'log_price': prep_decimal(),
    'property_type': prep_string(),
    'room_type': prep_string(),
    'accommodates': prep_int(),
    'bathrooms': prep_int(),
    'bed_type': prep_string()
})