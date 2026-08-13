import os 
from io import BytesIO 
from fastapi import FastAPI, File , UploadFile ,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates 
from dotenv import load_dotenv 
from google import genai 
from PIL import Image 

load_dotenv() 
app = FastAPI(title="AI Neutrition")  
templates = Jinja2Templates(directory="templates") 

api_key= os.getenv("GEMINI_API_KEY") 
client = genai.Client(api_key=api_key)

@app.get("/", response_class=HTMLResponse) 
async def read_root(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context = {"result":None}
    )

@app.post("/analyze", response_class=HTMLResponse)
async def analyze_food(request: Request, file: UploadFile = File(...)):
    try:
        contents = await file.read() 
        image = Image.open(BytesIO(contents)) 
        ### Here we can specify our condition for LLM 
        prompt = (
            "Analyze the food item in this image and provide a response strictly in English with the following structure:\n\n"
            "### 1. Food Name\n"
            "Identify the food item and brief description.\n\n"
            "### 2. Nutritional Information\n"
            "Provide the nutrition values in a strict Markdown Table format with columns: Nutrient, Estimated Amount, Key Sources/Notes.\n"
            "Include Calories, Protein, Carbs, Fats, Fiber, and Key Vitamins/Minerals.\n\n"
            "### 3. Health Verdict\n"
            "State clearly whether it is **Healthy** or **Unhealthy** and provide key reasons.\n\n"
            "### 4. Health Tips\n"
            "Provide actionable suggestions to make this meal healthier or more balanced."
        )

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[image,prompt] 
        )
        result_text = response.text 

    except Exception as e : 
        result_text = f"Error occured: {str(e)}" 

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"result": result_text}
    )



