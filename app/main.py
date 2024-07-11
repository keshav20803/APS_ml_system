import uvicorn
from fastapi import FastAPI
import pickle
import script

with open('my_dict', 'rb') as f3:
    mydict = pickle.load(f3)

app = FastAPI()

@app.get('/output')
def output():
    anslist , count = script.main()

    return {'list': anslist, 'count': count}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
