import bentoml
import pandas as pd
import numpy as np
from pydantic import BaseModel, Field

# --- ÉTAPE 1 : RÉCUPÉRER LE MODÈLE ---
model_ref = bentoml.sklearn.get("seattle_energy_model:latest")

# --- ÉTAPE 2 : SCHÉMA SWAGGER ---
class BuildingInput(BaseModel):
    PropertyGFATotal: float = Field(50000.0, gt=0)
    BuildingAge: float = Field(25.0, ge=0)
    PrimaryPropertyType: str = Field("Hotel")
    Neighborhood_Clean: str = Field("DOWNTOWN")

# --- ÉTAPE 3 : LE SERVICE ---
@bentoml.service(name="energy_predictor")
class EnergyService:
    def __init__(self):
        self.model = bentoml.sklearn.load_model("seattle_energy_model:latest")

    @bentoml.api
    def predict(self, data: BuildingInput) -> dict:
        # On crée le dictionnaire avec TOUTES les colonnes exigées par ton debug
        raw_dict = {
            "PropertyGFATotal": [data.PropertyGFATotal],
            "NumberofBuildings": [1],      # Valeur par défaut
            "NumberofFloors": [1],         # Valeur par défaut
            "BuildingAge": [data.BuildingAge],
            "GFA_per_Floor": [data.PropertyGFATotal], # Estimation simple
            "PrimaryPropertyType": [data.PrimaryPropertyType],
            "Neighborhood_Clean": [data.Neighborhood_Clean],
            "Is_MultiUse": [0],
            "Has_Gas": [0]
        }
        
        input_df = pd.DataFrame(raw_dict)

        try:
            # On laisse le pipeline faire le preprocessing
            prediction_log = self.model.predict(input_df)
            prediction_real = np.expm1(prediction_log[0])
            
            return {
                "prediction_kbtu": round(float(prediction_real), 2),
                "status": "success"
            }
        except Exception as e:
            return {
                "status": "error", 
                "message": str(e)
            }