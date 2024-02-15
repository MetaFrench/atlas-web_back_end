import pymongo

def list_all(mongo_collection):
  """
  List all documents in a mongo collection
  
  Args:
    mongo_collection: pymongodb collection object
  
  Returns:
    docs: list of documents
  """

  docs = []

  for doc in mongo_collection.find():
    docs.append(doc)
  
  return docs