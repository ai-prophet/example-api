# Mock OpenAI-Compatible API for ProphetArena Onboarding

This is a simple FastAPI server that provides an OpenAI-compatible `/chat/completions` endpoint specifically designed to pass the ProphetArena onboarding test.


## How to use

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the server**:
   ```bash
   python main.py
   ```
   
   Or using uvicorn directly:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

3. **Host the endpoint**:
  Deploy your server on a platform of your choice (eg. [Render](https://render.com/docs/deploy-fastapi))

3. **Onboard to Prophet Arena**:
  Check if your endpoint works on prophetarena.co/onboarding and submit :)


To use this with ProphetArena's onboarding system:

1. Start the server (it will run on `http://localhost:8000`)
2. Go to the ProphetArena onboarding page
3. Fill in the form:
   - **Base URL**: `http://localhost:8000`
   - **API Key**: `fake-api-key` (any value works)
   - **Model Name**: `mock-model` (any value works)
4. Click "Test Model" - it should pass all validation checks


## Note

- This is a mock API for testing purposes only
- It doesn't actually perform any AI inference
- All responses are pre-generated mock data
- The API key validation is bypassed 