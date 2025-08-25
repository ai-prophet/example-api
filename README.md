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

4. **Onboard to Prophet Arena**:
  Check if your endpoint works on prophetarena.co/onboarding and submit :)


## Note

- This is a mock API for testing purposes only
- It doesn't actually perform any AI inference, all responses are pre-generated mock data
- The API key validation is bypassed 
