from typing import Any, List, Optional

from pydantic import BaseModel
from bikeshare_model.processing.validation import DataInputSchema


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    #predictions: Optional[List[int]]
    predictions: Optional[int]


class MultipleDataInputs(BaseModel):
    inputs: List[DataInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {   'dteday': '2012-11-05',
                        'season': 'winter',
                        'hr': "6am",
                        'holiday': 'No',
                        'weekday':'Mon',
                        'workingday': 'Yes',
                        'weathersit':'Mist',
                        'temp': 6.1,
                        'atemp': 49,
                        'hum': 19.02,
                        'windspeed': 19.0012,
                        'casual': 139,
                        'registered': 139
                    }
                ]
                
            }
        }