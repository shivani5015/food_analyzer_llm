# AI-Powered Nutrition & Food Intelligence 

**food analyzer LLM** is an end-to-end multimodal AI application that transforms raw food images into detailed nutritional breakdowns
, health verdicts, and dietary advice. Built with **FastAPI**, **Google Gemini Vision API**, and **Jinja2**, it simplifies meal analysis through visual understanding.

---

##  Core Capabilities

* **Automated Visual Identification:** Recognizes dishes and ingredients directly from uploaded images.
* **Nutritional Estimation:** Approximates key macro and micro-nutrients:
  * Calories (kcal)
  * Protein, Carbohydrates, Fats, & Fiber (g)
  * Key Vitamins & Minerals
* **Health Verdict:** Categorizes meals as **Healthy** or **Unhealthy** with reasoning.
* **Dietary Recommendations:** Generates actionable suggestions to optimize meal balance.
* **Secure Architecture:** Uses environment variables for API key security and clean error handling.

---

##  System Architecture & Workflow

```text
  [ User Interface ]  --->  Uploads Food Image (.jpg/.png)
          │
          ▼
   [ FastAPI Server ] ---> Processes payload & images via PIL
          │
          ▼
 [ Gemini Multimodal ] ---> Analyzes visual features & prompts
          │
          ▼
 [ Structured Output ] ---> Renders Identification, Nutrition Table,
                             Verdict, & Actionable Health Tips
