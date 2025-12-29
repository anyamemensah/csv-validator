import polars as pl
import pandera.polars as pa
from functools import partial
from pandera.polars import PolarsData

genericIntBoolField = partial(pa.Field, coerce=True, nullable=True, isin=[0,1])
admission_type_values = ['Alternative', 'Special Admit', 'Criteria-Based', 
                         'Catchment', 'Citywide', 'Neighborhood', 'Virtual', 
                         'Citywide With Criteria']
governance_values = ['District', 'Charter', 'Contracted']

class DataSchema(pa.DataFrameModel):
    school_id: int = pa.Field(nullable=False, unique=True, coerce=True)
    school_year: str = pa.Field(nullable=False, coerce=True)
    standardized_school_name: str = pa.Field(nullable=False, coerce=True)
    original_school_name: str = pa.Field(nullable=False, coerce=True)
    year_school_opened: int = pa.Field(nullable=True, gt=0, coerce=True)
    is_elementary_school: int = genericIntBoolField()
    is_middle_school: int = genericIntBoolField()
    is_high_school: int = genericIntBoolField()
    is_other_school: int = genericIntBoolField()
    admission_type: str = pa.Field(nullable=True, isin=admission_type_values,coerce=True)
    governance: str = pa.Field(nullable=True, isin=governance_values, coerce=True)
    serves_grade_k: int = genericIntBoolField()
    serves_grade_1: int = genericIntBoolField()
    serves_grade_2: int = genericIntBoolField()
    serves_grade_3: int = genericIntBoolField()
    serves_grade_4: int = genericIntBoolField()
    serves_grade_5: int = genericIntBoolField()
    serves_grade_6: int = genericIntBoolField()
    serves_grade_7: int = genericIntBoolField()
    serves_grade_8: int = genericIntBoolField()
    serves_grade_9: int = genericIntBoolField()
    serves_grade_10: int = genericIntBoolField()
    serves_grade_11: int = genericIntBoolField()
    serves_grade_12: int = genericIntBoolField()

    @pa.check("school_id")
    def is_four_chars(cls, data: PolarsData) -> pl.LazyFrame:
        """
        Validates that every value in the 'school_id' column is 
        exactly four characters long.
        """
        return (
            data.lazyframe
                .select(pl.col(data.key).cast(pl.Utf8)
                    .str.len_chars()
                    .eq(4))
                )

