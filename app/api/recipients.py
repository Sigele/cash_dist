from fastapi import FastAPI

app = FastAPI()
path = "/recipients"

# POST, GET, PUT, DELETE

# GET - find an existing recipient by int id
@app.get("{path}/{recipient_id}")
async def get_recipient(recipient_id: int):
  return {"recipient_id": recipient_id}
  
# POST - create a new recipient
# what would be the parameter here? Nothing? What information do we expect to come with the request?
@app.post("{path}")
async def create_recipient():
  return {"message": "Welcome!"}

# PUT - update an existing recipient
# need to include the value that we want to update in the req
@app.put("{path}/{recipient_id}")
async def update_recipient(recipient_id: int):
  return {"message": "Recipient updated!"}

# DELETE - delete a recipient
@app.delete("{path}/{recipient_id}")
async def delete_recipient(recipient_id: int):
  return {f"message": "Recipient {recipient_id} deleted!"}