import pandas as pd
import joblib

# Load the Model
pipeline = joblib.load('model.pkl')

if(pipeline):
    print("PKL Loaded")
else:
    print("PKL error Loaded")
    
    
encoder = pipeline.named_steps['preproc'].named_transformers_['cat'].named_steps['onehot'].categories_

print(encoder[1])



    
#datafromJS.    
# ['kms_driven', 'owner', 'power', 'brand','Original Price', 'year']
data = pd.DataFrame({
    "kms_driven": [40000], #datafromJS.kms_driven
    "owner": ["First Owner"],
    "power": [100],
    "brand": ["TVS"],
    "Original Price": [70000],
    "year": [2020]
})

print(data)


result =  pipeline.predict(data);

print(result)
