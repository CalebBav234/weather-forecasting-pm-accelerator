from src.data_loader import load_weather_dataset
from src.validation import (
    validate_duplicates,
    validate_missing_values,
    validate_schema,
)

df = load_weather_dataset()

validate_schema(df)
validate_missing_values(df)
validate_duplicates(df)

print("Validation completed successfully.")