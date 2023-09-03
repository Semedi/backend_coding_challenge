import uvicorn

# launch the application using python directy
# allows you to use interactive debugger like ipdb

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8081, reload=True)

