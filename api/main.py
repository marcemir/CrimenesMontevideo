# Script para ejecutar la API con uvicorn
# http://127.0.0.1:8000/

import uvicorn

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
