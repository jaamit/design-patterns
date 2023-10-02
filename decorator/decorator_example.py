app = FastAPI(redoc_url = None)

def handle_exceptions(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except openai.error.InvalidRequestError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except openai.error.AuthenticationError as e:
            raise HTTPException(status_code=401, detail="OpenAI API Authenication failed")
        except openai.error.RateLimitError as e:
            raise HTTPException(status_code=429, detail="OpenAI API request exceeded rate limit")
        except openai.error.ServiceUnavailableError as e:
            raise HTTPException(status_code=503, detail=str(e))
        except openai.error.APIError as e:
            raise HTTPException(status_code=500, detail="OpenAI API returned an API Error")
        except Exception as e:
            raise HTTPException(status_code=500, detail="An unexpected error occurred")
    return wrapper

@app.post("/api/v1/demo")
@handle_exceptions
async def do_something():
  // do some work
  // return response
  return "OK"
